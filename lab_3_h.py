import log_functions as lf


def lab3h():
    while True:
        try:
            line = input()
            try:
                domain = lf.give_domain_name(line)
                if domain[-3:] == ".pl":
                    print(line)
            except RuntimeError:
                pass
        except EOFError:
            break


if __name__ == "__main__":
    lab3h()
