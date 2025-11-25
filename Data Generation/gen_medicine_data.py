import pandas as pd
import uuid
from utils.consts.medicine import medicine_data

diagnosis_df = pd.read_csv("department_treatment.csv")

columns = [
    "medicine_id",
    "diagnosis_id",
    "name",
    "compound",
    "uses",
    "side_effects",
    "department",
]


def generate_medicine_data():
    medicine_df = pd.DataFrame(columns=columns)
    for diagnosis, medicine_data_list in medicine_data.items():
        id_value = diagnosis_df.loc[
            diagnosis_df["diagnosis"] == diagnosis, "diagnosis_id"
        ].values[0]
        for med in medicine_data_list:
            medicine_df.loc[len(medicine_df)] = {
                "medicine_id": str(uuid.uuid4()),
                "diagnosis_id": id_value,
                "name": med["name"],
                "compound": med["compound"],
                "uses": med["uses"],
                "side_effects": med["side_effects"],
                "department": med["department"],
            }
    medicine_df.to_csv("medicine.csv", index=False)


generate_medicine_data()
