import log_functions as lf


def lab3a():
    count = [0, 0, 0]
    line_number = 0
    while True:
        try:
            line_number += 1
            line = input()
            try:
                code = lf.give_code(line)
                if code == "200":
                    count[0] += 1
                elif code == "302":
                    count[1] += 1
                elif code == "404":
                    count[2] += 1
            except RuntimeError as error:
                print(f"Exception at line: {line_number} ", end="-- ")
                print(error.args)
        except EOFError:
            break
    return count


if __name__ == "__main__":
    count_tab = lab3a()
    print(f"Count of 200 error code: {count_tab[0]}")
    print(f"Count of 302 error code: {count_tab[1]}")
    print(f"Count of 404 error code: {count_tab[2]}")
