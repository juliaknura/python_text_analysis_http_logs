import log_functions as lf
import sys


def lab3a_alt(code_type):
    count = 0
    line_number = 0

    while True:
        try:
            line_number += 1
            line = input()
            try:
                code = lf.give_code(line)
                if code == code_type:
                    count += 1
            except RuntimeError as error:
                print(f"Exception at line: {line_number} ", end="-- ")
                print(error.args)
        except EOFError:
            break
    return count


if __name__ == "__main__":
    code_type = sys.argv[1]
    total_count = lab3a_alt(code_type)
    print(f"Count of {code_type} error code: {total_count}")
