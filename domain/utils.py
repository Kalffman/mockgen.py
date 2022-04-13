import datetime
import re
import random


def resolve_full_name(full_name: str) -> str:
    full_name = re.sub(' +', ' ', full_name)

    full_name_arr = re.split('\\s', full_name)

    spaces = len(full_name_arr) - 1

    if spaces >= 2:
        full_name_arr.insert(random.randint(-2, -1), "DE")

        full_name = " ".join(full_name_arr)

    elif spaces > 1:
        full_name_arr.insert(-1, "DE")

        full_name = " ".join(full_name_arr)

    return full_name


async def random_date(years: int = 0, months: int = 0, days: int = 0):
    today = datetime.date.today()

    start_date = datetime.date(today.year - years, today.month - months, today.day - days)

    date_interval = today - start_date

    interval = date_interval.days

    return start_date + datetime.timedelta(days=random.randrange(interval))
