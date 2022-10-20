#6510742460 Putthipong Soongsuwan
from urllib.request import DataHandler


def print_less(x, a_list):
    for i in a_list:
        if int(x) > int(i):
            print(i, end = ' ')
    print("")
print_less(50, [50, 51, 99, 79, 47, 83, 90, 39, 90, 25])
a, list_1 = 55, list(range(30, 100, 15))
print_less(a, list_1)