from datetime import datetime, timedelta, timezone
import random
import pandas as pd
import ast

from utils.random_NID import (
    generate_random_egyptian_id,
    extract_age_from_id,
    generate_random_contact_number,
    generate_random_egyptian_address,
)
from utils.consts.names import first_names_female, first_names_male, last_names


hospital_df = pd.read_csv("hospitals.csv")
diagnosis_treatment_df = pd.read_csv("department_treatment.csv")
medicine_df = pd.read_csv("medicine.csv")
staff_df = pd.read_csv("staff.csv")
merged_medicine_diagnosis = pd.merge(
    medicine_df, diagnosis_treatment_df, on="diagnosis_id"
)


def corrupt_data(patient_data):

    if random.random() < 0.05:
        patient_data["age"] = random.randint(130, 200)

    if random.random() < 0.05:
        patient_data["contact_number"] = str(random.randint(1000, 9999))

    for record in patient_data["records"]:

        if random.random() < 0.03:
            record["diagnosis"] = ""
        if random.random() < 0.03:
            record["treatment"] = ""

    return patient_data


def generate_patient_event():
    """ """
    admission_time = datetime.now(timezone.utc) - timedelta(hours=random.randint(1, 72))
    discharge_time = datetime.now(timezone.utc) + timedelta(hours=random.randint(1, 72))

    patient_NID = generate_random_egyptian_id()
    age = extract_age_from_id(patient_NID)

    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        first_name = random.choice(first_names_male)
    else:
        first_name = random.choice(first_names_female)
    last_name = random.choice(last_names)
    full_name = f"{first_name}, {last_name}"

    hospital_random = hospital_df.sample(n=1).iloc[0]
    ICU_admission = random.choice([True, False])

    departement_admitted = random.choice(
        hospital_random["departments"].apply(ast.literal_eval)
    )
    filtered = diagnosis_treatment_df[
        diagnosis_treatment_df["department"] == departement_admitted
    ]

    row_dt = filtered.sample(1).iloc[0]

    diagnosis = row_dt["diagnosis"]
    treatment = random.choice(row_dt["treatments"].apply(ast.literal_eval))
    doctors_in_hospital_department = staff_df[
        (staff_df["role"] == "Doctor")
        & (staff_df["hospital_id"] == hospital_random["hospital_id"])
        & (staff_df["department"] == departement_admitted)
    ]
    doctor_id = doctors_in_hospital_department.sample(1).iloc[0]["id"]

    medicines_available = merged_medicine_diagnosis[
        merged_medicine_diagnosis["diagnosis"] == diagnosis
    ]
    medicine_taken = medicines_available.sample(1).iloc[0]["name"]

    patient_data = {
        "patient_id": patient_NID,
        "gender": gender,
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "city": hospital_random["city"],
        "governorate": hospital_random["governorate"],
        "address": generate_random_egyptian_address(hospital_random["governorate"]),
        "age": age,
        "contact_number": generate_random_contact_number(),
        "records": [
            {
                "admission_time": admission_time.isoformat(),
                "discharge_time": discharge_time.isoformat(),
                "hospital_id": hospital_random["hospital_id"],
                "department": departement_admitted,
                "ICU_admission": ICU_admission,
                "diagnosis": diagnosis,
                "treatment": treatment,
                "arrival_mode": random.choice(["Walk-in", "Ambulance", "Referral"]),
                "doctor_id": doctor_id,
                "medicine_takem": medicine_taken,
                "severity_level": (
                    random.choice(["High", "Critical"])
                    if ICU_admission
                    else random.choice(["Low", "Moderate", "High", "Critical"])
                ),
            }
        ],
    }

    patient_data = corrupt_data(patient_data)

    return patient_data


# Main Function of Generation
if __name__ == "__main__":
    generate_patient_event()
