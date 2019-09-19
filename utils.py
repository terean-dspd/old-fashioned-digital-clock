import os


def print_time(time, color):
    """Prints the current time

    A `time` is a list of lists. Each list element is list it self.

    A `color` is `colorama.Fore` object
    """
    print("\n\n\n\n")
    for row in range(0, 5):
        print(color + time[0][row]+time[1][row]+" "+time[2][row] + " " +
              time[3][row]+time[4][row]+" "+time[5][row] + " " +
              time[6][row]+time[7][row])


def screen_cleaner():
    """
    Detects operation system and clear the terminal
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
