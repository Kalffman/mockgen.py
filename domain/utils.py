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
