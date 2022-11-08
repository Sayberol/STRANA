import numpy as np


def find_max_multiply(array):
    absolute_value = np.abs(array)
    absolute_value.sort()
    if len(absolute_value) > 1:
        return absolute_value[-1] * absolute_value[-2]
    else:
        return absolute_value[0]


if __name__ == '__main__':
    print(find_max_multiply([-5, 0, 15, -10, -12]))
