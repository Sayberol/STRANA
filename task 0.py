m = 5
n = 5

arr = [[0] * m for i in range(n)]

result = ''

for i in range(len(arr)):
    arr[i][len(arr) - 1 - i] = 1

    line = ' '.join(str(item) for item in arr[i])
    result = result + line + ' \n'


if __name__ == '__main__':
    print(result)
