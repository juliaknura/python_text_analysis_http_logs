from datetime import datetime


def give(txt, pos, element_type):
    split_line = txt.split(" ")
    if len(split_line) < abs(pos):
        raise RuntimeError(f"Invalid log -- {element_type} cannot be read")
    return split_line[pos]


def give_code(txt):
    return give(txt, -2, "code")


def give_size(txt):
    return_value = give(txt, -1, "size")
    if return_value == "-":
        return 0
    else:
        return int(return_value)


def give_path(txt):
    return give(txt, 6, "path")


def give_domain_name(txt):
    return give(txt, 0, "domain name")


def give_full_date(txt):
    returned_val = give(txt, 3, "date")
    return returned_val[1:]


def give_day(txt):
    returned_val = give_full_date(txt)
    return returned_val[:11]


def give_hour(txt):
    returned_val = give_full_date(txt)
    return returned_val[12:]


def compare(hour1, hour2):
    if int(hour1[:2]) < int(hour2[:2]):
        return 1
    elif int(hour1[:2]) > int(hour2[:2]):
        return -1
    elif int(hour1[3:5]) < int(hour2[3:5]):
        return 1
    elif int(hour1[3:5]) > int(hour2[3:5]):
        return -1
    elif int(hour1[6:]) < int(hour2[6:]):
        return 1
    elif int(hour1[6:]) > int(hour2[6:]):
        return -1
    else:
        return 0


def condition_first_bigger(hour, hour1, hour2):
    return compare(hour, hour1) == -1 or compare(hour, hour2) == 1 or compare(hour, hour1) == 0 \
        or compare(hour, hour2) == 0


def condition_second_bigger(hour, hour1, hour2):
    return (compare(hour, hour1) == -1 and compare(hour, hour2) == 1) or compare(hour, hour1) == 0 \
        or compare(hour, hour2) == 0


def to_datetime_format(date):
    dt = datetime(int(date[7:]), month_change_format(date[3:6]), int(date[:2]))
    return dt


month_dictionary = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}


def month_change_format(month_string):
    return month_dictionary.get(month_string)
