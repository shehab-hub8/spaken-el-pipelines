from datetime import datetime, timedelta, timezone
import random
import pandas as pd

from utils.random_NID import (
    generate_random_egyptian_id,
    extract_age_from_id,
    generate_random_contact_number,
    generate_random_egyptian_address,
)
from utils.consts.names import first_names_female, first_names_male, last_names
from utils.consts.diagnosis_treatments import departemnet_diagnosis_treatment


hospital_df = pd.read_csv("hospitals.csv")


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

    departement_admitted = random.choice(hospital_random["departments"])
    diagnosis_treatment = random.choice(
        departemnet_diagnosis_treatment[departement_admitted]
    )
    diagnosis = diagnosis_treatment["diagnosis"]
    treatment = random.choice(diagnosis_treatment["details"]["treatments"])

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
    pass
