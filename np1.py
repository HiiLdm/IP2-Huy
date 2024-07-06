import numpy as np

if __name__ == '__main__':
    n = int(input().strip())

    arr = np.arange(n)
    arr[arr % 2 != 0] = -1

    print(arr)
