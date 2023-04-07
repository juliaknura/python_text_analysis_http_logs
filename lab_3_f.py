import log_functions as lf


def lab3f(hour1, hour2):
    while True:
        try:
            line = input()
            try:
                hour = lf.give_hour(line)
                if lf.compare(hour1, hour2) == 1:
                    if lf.condition_second_bigger(hour, hour1, hour2):
                        print(line)
                elif lf.condition_first_bigger(hour, hour1, hour2):
                    print(line)
            except RuntimeError:
                pass
        except EOFError:
            break


if __name__ == "__main__":
    lab3f("22:00:00", "06:00:00")
