from utils.consts.diagnosis_treatments import departemnet_diagnosis_treatment
import pandas as pd
import uuid


def generate_diagnosis_treatment():
    diagnosis_treatment_df = pd.DataFrame(
        columns=["diagnosis_id", "department", "diagnosis", "description", "treatments"]
    )
    for department, diagnosises in departemnet_diagnosis_treatment.items():
        for items in diagnosises:
            diagnosis_treatment_df.loc[len(diagnosis_treatment_df)] = {
                "diagnosis_id": str(uuid.uuid4()),
                "department": department,
                "diagnosis": items["diagnosis"],
                "description": items["details"]["description"],
                "treatments": items["details"]["treatments"],
            }
    diagnosis_treatment_df.to_csv("department_treatment.csv", index=False)


if __name__ == "__main__":
    generate_diagnosis_treatment()
