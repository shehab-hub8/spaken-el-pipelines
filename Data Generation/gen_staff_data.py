import pandas as pd
import random
import uuid
import ast

from utils.consts.staff import (
    staff_data,
    department_roles,
    specialization_qualification,
)
from utils.random_NID import (
    generate_random_contact_number,
    generate_random_egyptian_id,
    extract_age_from_id,
    generate_random_egyptian_address,
)

from utils.consts.names import first_names_male, first_names_female, last_names

hospital_df = pd.read_csv("hospitals.csv")


def generate_staff_hospital():
    staff_df = pd.DataFrame(columns=staff_data)
    hospital_df["departments"] = hospital_df["departments"].apply(ast.literal_eval)
    for index, row in hospital_df.iterrows():

        counter_doctors = 0
        # generate 3 - 7 general doctors for each department
        print(row["governorate"], "Yooooo")
        for department in row["departments"]:
            print(row["governorate"], "Here")
            for i in range(random.randint(3, 7)):
                ID = generate_random_egyptian_id()
                age = extract_age_from_id(ID)
                while age < 25 and age > 70:
                    ID = generate_random_egyptian_id()
                    age = extract_age_from_id(ID)

                gender = random.choice(["Male", "Female"])

                if gender == "Male":
                    first_name = random.choice(first_names_male)
                else:
                    first_name = random.choice(first_names_female)
                last_name = random.choice(last_names)
                full_name = f"{first_name}, {last_name}"

                max_experience = max(0, age - 22)
                years_experience = random.randint(0, min(max_experience, 40))

                specialization = random.choice(
                    department_roles.get(department, ["General Practitioner"])
                )
                qualification = specialization_qualification.get(specialization, "MD")

                on_leave = False
                if random.random() < 0.05:
                    on_leave = True

                staff_df.loc[len(staff_df)] = {
                    "staff_id": str(uuid.uuid4()),
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": full_name,
                    "gender": gender,
                    "age": age,
                    "contact_number": generate_random_contact_number(),
                    "role": "Doctor",
                    "department": department,
                    "specialization": specialization,
                    "qualification": qualification,
                    "years_experience": years_experience,
                    "shift": random.choice(["Morning", "Evening", "Night"]),
                    "hospital_id": row["hospital_id"],
                    "city": row["city"],
                    "governorate": row["governorate"],
                    "on_leave": on_leave,
                    "address": generate_random_egyptian_address(row["governorate"]),
                }
                counter_doctors += 1

        for _ in range(counter_doctors * random.randint(2, 3)):
            ID = generate_random_egyptian_id()
            age = extract_age_from_id(ID)
            while age < 25 and age > 70:
                ID = generate_random_egyptian_id()
                age = extract_age_from_id(ID)

            gender = random.choice(["Male", "Female"])

            if gender == "Male":
                first_name = random.choice(first_names_male)
            else:
                first_name = random.choice(first_names_female)
            last_name = random.choice(last_names)
            full_name = f"{first_name}, {last_name}"

            max_experience = max(0, age - 22)
            years_experience = random.randint(0, min(max_experience, 40))

            specialization = random.choice(
                department_roles.get(department, ["General Practitioner"])
            )
            qualification = specialization_qualification.get(specialization, "MD")

            on_leave = False
            if random.random() < 0.05:
                on_leave = True

            staff_df.loc[len(staff_df)] = {
                "staff_id": str(uuid.uuid4()),
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "gender": gender,
                "age": age,
                "contact_number": generate_random_contact_number(),
                "role": "Nurse",
                "department": "General",
                "specialization": "General Nurse",
                "qualification": "BSc Nursing",
                "years_experience": years_experience,
                "shift": random.choice(["Morning", "Evening", "Night"]),
                "hospital_id": row["hospital_id"],
                "city": row["city"],
                "governorate": row["governorate"],
                "on_leave": on_leave,
                "address": generate_random_egyptian_address(row["governorate"]),
            }
        
        for _ in range(random.randint(1, 4)):
            ID = generate_random_egyptian_id()
            age = extract_age_from_id(ID)
            while age < 25 and age > 70:
                ID = generate_random_egyptian_id()
                age = extract_age_from_id(ID)

            gender = random.choice(["Male", "Female"])

            if gender == "Male":
                first_name = random.choice(first_names_male)
            else:
                first_name = random.choice(first_names_female)
            last_name = random.choice(last_names)
            full_name = f"{first_name}, {last_name}"

            max_experience = max(0, age - 22)
            years_experience = random.randint(0, min(max_experience, 40))

            specialization = random.choice(
                department_roles.get(department, ["General Practitioner"])
            )
            qualification = specialization_qualification.get(specialization, "MD")

            on_leave = False
            if random.random() < 0.05:
                on_leave = True

            staff_df.loc[len(staff_df)] = {
                "staff_id": str(uuid.uuid4()),
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "gender": gender,
                "age": age,
                "contact_number": generate_random_contact_number(),
                "role": "Pharmacist",
                "department": "Pharmacy",              # Pharmacists belong to the Pharmacy department
                "specialization": "Pharmacist",       # General pharmacist specialization
                "qualification": "BSc Pharmacy",    
                "years_experience": years_experience,
                "shift": random.choice(["Morning", "Evening", "Night"]),
                "hospital_id": row["hospital_id"],
                "city": row["city"],
                "governorate": row["governorate"],
                "on_leave": on_leave,
                "address": generate_random_egyptian_address(row["governorate"]),
            }
            
        for _ in range(random.randint(10, 15)):
            ID = generate_random_egyptian_id()
            age = extract_age_from_id(ID)
            while age < 25 and age > 70:
                ID = generate_random_egyptian_id()
                age = extract_age_from_id(ID)

            gender = random.choice(["Male", "Female"])

            if gender == "Male":
                first_name = random.choice(first_names_male)
            else:
                first_name = random.choice(first_names_female)
            last_name = random.choice(last_names)
            full_name = f"{first_name}, {last_name}"

            max_experience = max(0, age - 22)
            years_experience = random.randint(0, min(max_experience, 40))

            specialization = random.choice(
                department_roles.get(department, ["General Practitioner"])
            )
            qualification = specialization_qualification.get(specialization, "MD")

            on_leave = False
            if random.random() < 0.05:
                on_leave = True

            staff_df.loc[len(staff_df)] = {
                "staff_id": str(uuid.uuid4()),
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "gender": gender,
                "age": age,
                "contact_number": generate_random_contact_number(),
                "role": "Maintaince",
                "department": "Maintaince",              # Pharmacists belong to the Pharmacy department
                "specialization": random.choice(["Cleaner", "General Maintenance"]),       # General pharmacist specialization
                "qualification": "High School Diploma",    
                "years_experience": years_experience,
                "shift": random.choice(["Morning", "Evening", "Night"]),
                "hospital_id": row["hospital_id"],
                "city": row["city"],
                "governorate": row["governorate"],
                "on_leave": on_leave,
                "address": generate_random_egyptian_address(row["governorate"]),
            }
            
        for _ in range(random.randint(7, 12)):
            ID = generate_random_egyptian_id()
            age = extract_age_from_id(ID)
            while age < 25 and age > 70:
                ID = generate_random_egyptian_id()
                age = extract_age_from_id(ID)

            gender = random.choice(["Male", "Female"])

            if gender == "Male":
                first_name = random.choice(first_names_male)
            else:
                first_name = random.choice(first_names_female)
            last_name = random.choice(last_names)
            full_name = f"{first_name}, {last_name}"

            max_experience = max(0, age - 22)
            years_experience = random.randint(0, min(max_experience, 40))

            specialization = random.choice(
                department_roles.get(department, ["General Practitioner"])
            )
            qualification = specialization_qualification.get(specialization, "MD")

            on_leave = False
            if random.random() < 0.05:
                on_leave = True

            staff_df.loc[len(staff_df)] = {
                "staff_id": str(uuid.uuid4()),
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "gender": gender,
                "age": age,
                "contact_number": generate_random_contact_number(),
                "role": random.choice(["Receptionist", "Finance"]),
                "department": "Administration",             
                "specialization": "Diploma / BSc in Administration",
                "years_experience": years_experience,
                "shift": random.choice(["Morning", "Evening", "Night"]),
                "hospital_id": row["hospital_id"],
                "city": row["city"],
                "governorate": row["governorate"],
                "on_leave": on_leave,
                "address": generate_random_egyptian_address(row["governorate"]),
            }
    staff_df.to_csv("staff.csv", index=False)
            
            
    

if __name__ == "__main__":
    generate_staff_hospital()
