#6510742460 Putthipong Soongsuwan
char_input = str(input("Enter a character : "))
if ord(char_input) >= ord('A') and ord(char_input) <= ord('Z'):
    print(f"{char_input} is an uppercase letter")
elif ord(char_input) >= ord('a') and ord(char_input) <= ord('z'):
    print(f"{char_input} is a lowercase letter")
else:
    print(f"{char_input} is not a letter")