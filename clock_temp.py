import datetime
import time

from data_models import DIGITS, SEPAR
from generators import colorizer, counter
from utils import print_time, screen_cleaner


def main():
    current_digits = []
    cntr = counter(5)
    color = colorizer(10)
    blinker = False
    while True:
        current_time = datetime.datetime.now().strftime("%H%M%S")
        separator = SEPAR[next(cntr)]
        current_digits.append(DIGITS[int(current_time[0])])
        current_digits.append(DIGITS[int(current_time[1])])
        current_digits.append(separator)
        current_digits.append(DIGITS[int(current_time[2])])
        current_digits.append(DIGITS[int(current_time[3])])
        current_digits.append(separator)
        current_digits.append(DIGITS[int(current_time[4])])
        current_digits.append(DIGITS[int(current_time[5])])
        clr = next(color)
        print_time(current_digits[::-1], clr)
        time.sleep(0.2)
        screen_cleaner()
        current_digits = []
        blinker = not blinker


if __name__ == "__main__":
    main()
