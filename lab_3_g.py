import log_functions as lf
from datetime import datetime


def lab3g(weekday):
    while True:
        try:
            line = input()
            try:
                date = lf.give_day(line)
                dt = lf.to_datetime_format(date)
                if dt.isoweekday() == weekday:
                    print(line)
            except RuntimeError:
                pass
            except ValueError:
                pass
        except EOFError:
            break


if __name__ == "__main__":
    lab3g(5)
