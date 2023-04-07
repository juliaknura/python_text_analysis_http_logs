import log_functions as lf


def lab3e(filter_condition):
    while True:
        try:
            line = input()
            try:
                code = lf.give_code(line)
                if code == filter_condition:
                    print(line)
            except RuntimeError:
                pass
        except EOFError:
            break


if __name__ == "__main__":
    lab3e("200")
