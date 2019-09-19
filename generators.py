from data_models import COLORS


def counter(n):
    """Generates enless sequence from 1 to `n` and back to 1"""
    i = 1
    direction = False
    while True:
        yield i
        if 1 < i < 5:
            if direction:
                i += 1
            else:
                i -= 1
        else:
            direction = not direction
            if i == 1:
                i += 1
            else:
                i -= 1


def colorizer(n):
    """Iterates forth and back on 5 colors
    `n:int` used to return each color n time before switch to next color

    `direction:bool` shows what to do with index. If `direction` is `True` the
    index is incremented, if `False` the index is decremented
    """
    colors_numb = len(COLORS)

    while True:
        for i in range(colors_numb):
            for _ in range(n):
                yield COLORS[i]
