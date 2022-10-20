#6510742460 Putthipong Soongsuwan
from urllib.request import DataHandler


def print_less(x, a_list):
    print(', '.join([str(f'a = {a}') for a in a_list if a<x]))

print_less(50, [50, 51, 99, 79, 47, 83, 90, 39, 90, 25])
a, list_1 = 55, list(range(30, 100, 15))
print_less(a, list_1)