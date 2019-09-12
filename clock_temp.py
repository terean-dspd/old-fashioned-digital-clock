import datetime
import time
import os


def counter(n):
    i = 1
    while True:
        if i <= n:
            yield i
            i += 1
        else:
            i = 1
            yield i


def colorizer(n, c):
    i = 1
    color = 1
    while True:
        if i <= n:
            yield f"color 0{color}"
            i += 1
        else:
            i = 1
            if color <= c:
                yield f"color 0{color}"
                color += 1
            else:
                color = 1
                yield f"color 0{color}"


digits = {
    0: [
        " ████████",
        " ██    ██",
        " ██    ██",
        " ██    ██",
        " ████████"
    ],
    1: [
        " █████   ",
        "    ██   ",
        "    ██   ",
        "    ██   ",
        " ████████"
    ],
    2: [
        " ████████",
        "       ██",
        " ████████",
        " ██      ",
        " ████████"
    ],
    3: [
        " ████████",
        "       ██",
        " ████████",
        "       ██",
        " ████████"
    ],
    4: [
        " ██    ██",
        " ██    ██",
        " ████████",
        "       ██",
        "       ██"
    ],
    5: [
        " ████████",
        " ██      ",
        " ████████",
        "       ██",
        " ████████"
    ],
    6: [
        " ████████",
        " ██      ",
        " ████████",
        " ██    ██",
        " ████████"
    ],
    7: [
        " ████████",
        "       ██",
        "       ██",
        "       ██",
        "       ██"
    ],
    8: [
        " ████████",
        " ██    ██",
        " ████████",
        " ██    ██",
        " ████████"
    ],
    9: [
        " ████████",
        " ██    ██",
        " ████████",
        "       ██",
        " ████████"
    ]}
separ = {
    1: [
        "  ██ ",
        "     ",
        "     ",
        "     ",
        "     "
    ],
    2: [
        "     ",
        "  ██ ",
        "     ",
        "     ",
        "     "
    ],
    3: [
        "     ",
        "     ",
        "  ██ ",
        "     ",
        "     "
    ],
    4: [
        "     ",
        "     ",
        "     ",
        "  ██ ",
        "     "
    ],
    5: [
        "     ",
        "     ",
        "     ",
        "     ",
        "  ██ "
    ]}


def print_time(dig):
    print("\n\n\n\n")
    for row in range(0, 5):
        print(dig[0][row]+dig[1][row]+" "+dig[2][row] + " " +
              dig[3][row]+dig[4][row]+" "+dig[5][row] + " " +
              dig[6][row]+dig[7][row])


def main():
    os.system('cls')
    current_digits = []
    cntr = counter(5)
    color = colorizer(5, 8)
    blinker = False
    # os.system('clear') # linux
    while True:
        current_time = datetime.datetime.now().strftime("%H%M%S")
        separator = separ[next(cntr)]
        current_digits.append(digits[int(current_time[0])])
        current_digits.append(digits[int(current_time[1])])
        current_digits.append(separator)
        current_digits.append(digits[int(current_time[2])])
        current_digits.append(digits[int(current_time[3])])
        current_digits.append(separator)
        current_digits.append(digits[int(current_time[4])])
        current_digits.append(digits[int(current_time[5])])
        print_time(current_digits)
        time.sleep(0.2)
        current_digits = []
        blinker = not blinker
        clr = next(color)
        os.system(clr)  # set color
        os.system('cls')  # clear screen


if __name__ == "__main__":
    main()
