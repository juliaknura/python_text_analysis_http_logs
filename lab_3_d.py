import log_functions as lf


def lab3d():
    line_number = 0
    all_resources = 0
    graphics = 0
    while True:
        try:
            line_number += 1
            line = input()
            try:
                path = lf.give_path(line)
                all_resources += 1
                if path.find(".gif") != -1 or path.find(".jpg") != -1 or path.find(".jpeg") != -1 \
                        or path.find(".xbm") != -1:
                    graphics += 1
            except RuntimeError as err:
                print(f"Exception at line: {line_number} ", end="-- ")
                print(err.args)
        except EOFError:
            break
    return graphics/all_resources


if __name__ == "__main__":
    ratio = lab3d()
    print(f"The ratio of graphic file downloads to all downloads is {round(ratio,2)}")
