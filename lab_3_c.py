import log_functions as ls


def lab3c():
    max_path = ""
    max_size = 0
    line_number = 0
    while True:
        try:
            line_number += 1
            line = input()
            try:
                current_path = ls.give_path(line)
                current_size = ls.give_size(line)
                if current_size > max_size:
                    max_path = current_path
                    max_size = current_size
            except RuntimeError as err:
                print(f"Exception at line: {line_number} ", end="-- ")
                print(err.args)
        except EOFError:
            break
    return max_path, max_size


if __name__ == "__main__":
    final_path, final_size = lab3c()
    print(f"The biggest resource has path: {final_path} and size: {final_size}")
    