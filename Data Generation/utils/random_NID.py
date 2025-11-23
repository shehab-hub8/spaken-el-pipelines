import random
import datetime
from .consts.cities import gov_codes, governorate_data

def generate_random_egyptian_id():
    # century choice
    century = random.choice([2, 3])

    # birthday between (1940, 2024)
    start_date = datetime.date(1940, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    birthday = start_date + datetime.timedelta(days=random_days)

    # Extract Day Month Year
    YY = str(birthday.year)[2:]
    MM = f"{birthday.month:02d}"
    DD = f"{birthday.day:02d}"

    gov = f"{random.choice(gov_codes):02d}"

    serial = f"{random.randint(0, 999):02d}"

    checksum = str(random.randint(0, 9))

    return f"{century}{YY}{MM}{DD}{gov}{serial}{checksum}"


def extract_age_from_id(ID):
    C = ID[0]
    YY = ID[1:3]
    MM = ID[3:5]
    DD = ID[5:7]

    year = ""

    if C == 2:
        year = "19"
    else:
        year = "20"

    year += YY

    birthdate = datetime.date(int(year), int(MM), int(DD))
    today = datetime.date.today()

    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )

    return age


def generate_random_contact_number():
    return random.choice(["010", "011", "012", "015"]) + str(
        random.randint(10000000, 99999999)
    )


def generate_random_egyptian_address(gov):
    print(gov)
    gov_data = governorate_data[gov]
    street = random.choice(gov_data["streets"])
    building_number = random.randint(1, 200)
    district = random.choice(gov_data["districts"])
    return f"{building_number} {street}, {district}, {gov}"


print(generate_random_contact_number())
