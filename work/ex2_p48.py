# 6510742460 Putthipong Soongsuwan
def print_even(a_list):
    for i in a_list:
        if i % 2 != 1:
            print(i, end=' ')
    print("")
print_even([1,2,3,4,5])
list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 21, 20]
list_2 = list(range(20, 0, -3))
print_even(list_1)
print_even(list_2)