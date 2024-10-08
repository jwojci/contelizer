import datetime


# Weights for calculating the validity of PESEL
WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

# Map for determining the century and month adjustment based on the first digit of the month
CENTURY_MAP = {
    "0": (1900, 0),
    "1": (1900, 0),
    "8": (1800, 80),
    "9": (1800, 80),
    "2": (2000, 20),
    "3": (2000, 20),
    "4": (2100, 40),
    "5": (2100, 40),
    "6": (2200, 60),
    "7": (2200, 60),
}


def verify_pesel_and_get_date_info(pesel):
    if verify_pesel_numerically(pesel):
        date_info = verify_pesel_by_date_and_get_birth_date(pesel)
        if date_info:
            return date_info
    return False


def verify_pesel_numerically(pesel):
    weighted_sum = 0
    control_number = int(pesel[-1])

    for i in range(len(WEIGHTS)):
        weighted_sum += int(pesel[i]) * WEIGHTS[i]

    weighted_sum = weighted_sum % 10
    return (10 - weighted_sum) % 10 == control_number


def verify_pesel_by_date_and_get_birth_date(pesel):
    pesel_year = int(pesel[0:2])
    pesel_month = int(pesel[2:4])
    pesel_day = int(pesel[4:6])

    # Determine the century and adjustment value based on the first digit of the month
    century, adjustment = CENTURY_MAP.get(str(pesel_month // 10), (None, None))

    if century is None:
        return False

    # Adjust the month to get the actual month
    month = pesel_month - adjustment

    # Calculate the full year
    year = century + pesel_year

    # Validate if the date is correct
    try:
        birth_date = datetime.date(year, month, pesel_day)
        if birth_date > datetime.date.today():
            return False
    except ValueError:
        return False
    return {"year": year, "month": f"{month:02}", "day": f"{pesel_day:02}"}


def get_pesel_information(pesel, date_info):
    year = date_info.get("year")
    month = date_info.get("month")
    day = date_info.get("day")

    gender = "female" if int(pesel[9]) % 2 == 0 else "male"

    return {"gender": gender, "birth_date": f"{day}.{month}.{year}"}
