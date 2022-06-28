import numpy
import pandas as pd

def round_pred(y):
    print(y)
    rounded_y = numpy.around(y)
    print(rounded_y)
    return rounded_y

def re_rate(y : pd.Series):
    for i in range(0, len(y)):
        if y[i] <= 4:
            y[i] = 0
        elif y[i] >= 7:
            y[i] = 2
        else:
            y[i] = 1

    return y
