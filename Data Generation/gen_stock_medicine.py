import pandas as pd
import uuid
from datetime import datetime, timezone
import random
import ast

hospital_df = pd.read_csv("hospitals.csv")
medicine_df = pd.read_csv("medicine.csv")
hospital_df["departments"] = hospital_df["departments"].apply(ast.literal_eval)

columns = [
    "hospital_id",
    "department",
    "medicine_id",
    "stock_quantity",
    "last_updated",
]


def generate_stock_data():
    stock_df = pd.DataFrame(columns=columns)
    for _, hospital in hospital_df.iterrows():
        hospital_id = hospital["hospital_id"]
        for dept in hospital["departments"]:
            print(dept)
            dept_meds = medicine_df[
                medicine_df["department"].str.strip().str.lower()
                == dept.strip().lower()
            ]

            if dept_meds.empty:
                print(
                    f"No medicines found for department '{dept}' in hospital '{hospital['hospital_name']}'"
                )

            for medicine_id in dept_meds["medicine_id"]:
                stock_df.loc[len(stock_df)] = {
                    "hospital_id": hospital_id,
                    "department": dept,
                    "medicine_id": medicine_id,
                    "stock_quantity": random.randint(10, 200),
                    "last_updated": datetime.now(timezone.utc),
                }

    stock_df.to_csv("stock_medicine.csv", index=False)


generate_stock_data()
