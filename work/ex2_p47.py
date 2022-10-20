#6510742460 Putthipong Soongsuwan
def print_digit(a_string):
    for i in a_string:
        if i.isdigit():
            print(i, end=' ')
    print('')
print_digit("24 hours in 1 day, 7 days in a week.")
message = 'I met a man with 7 wives. Each wife had 7 sack.'
print_digit(message)