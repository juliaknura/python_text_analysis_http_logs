import log_functions as ls


def lab3b():
    total_sum = 0
    line_number = 0

    while True:
        try:
            line_number += 1
            line = input()
            try:
                answer_bytes = ls.give_size(line)
                if answer_bytes < 0:
                    continue
                total_sum = total_sum + answer_bytes
            except RuntimeError as rerror:
                print(f"Exception at line: {line_number} ", end="-- ")
                print(rerror.args)
            except ValueError as verror:
                print(f"Exception at line: {line_number} ", end="-- ")
                print(verror.args)
        except EOFError:
            break
    return total_sum


if __name__ == "__main__":
    total_sum = lab3b()
    print(f"The total size of all data sent to hosts equals {(total_sum/(10**9))} GB")
