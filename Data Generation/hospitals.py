import pandas as pd
import random
import uuid

from utils.consts.hospitals import (
    hospital_details,
    hospital_columns,
    essential_departments,
    department_to_services,
    essential_departments,
    optional_departments,
)


def generate_hospital_data():

    hospital_df = pd.DataFrame(columns=hospital_columns)

    for hospital_name, hospital_data in hospital_details.items():

        hospital_departments = essential_departments + random.sample(
            optional_departments, random.randint(1, 4)
        )
        hospital_services = []

        for dept in hospital_departments:
            hospital_services.extend(department_to_services.get(dept, []))

        # unique services only (remove dupicates)
        hospital_services = list(set(hospital_services))

        hospital_df.loc[len(hospital_df)] = {
            "hospital_id": str(uuid.uuid4()),
            "hospital_name": hospital_name,
            "hospital_address": hospital_data["street"],
            "governorate": hospital_data["governorate"],
            "city": hospital_data["city"],
            "street": hospital_data["street"],
            "region": hospital_data["region"],
            "hospital_type": (
                "university"
                if "university" in hospital_name.lower()
                else random.choice(["public", "private"])
            ),
            "contact_number": f"+20{random.randint(1000000000, 9999999999)}",
            "hospital_capacity": random.randint(50, 500),
            "current_occupancy": random.randint(0, 50),
            "emergency_services": random.choice([True, False]),
            "ICU_capacity": random.randint(5, 50),
            "ambulance_count": random.randint(0, 10),
            "services": hospital_services,
            "departments": hospital_departments,
        }

    hospital_df.to_csv("hospitals.csv", index=False)

if __name__ == "__main__":
    generate_hospital_data()