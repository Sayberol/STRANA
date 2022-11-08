def find_max_multiply(array):
    if len(array) < 2:
        return
    absolute_values = [abs(i) for i in array]
    value = max(absolute_values)
    first_index = absolute_values.index(value)
    absolute_values[first_index] = 0
    value = max(absolute_values)
    second_index = absolute_values.index(value)
    return array[first_index] * array[second_index]


if __name__ == '__main__':
    print(find_max_multiply([-5, 0, 15, -10, -12]))
