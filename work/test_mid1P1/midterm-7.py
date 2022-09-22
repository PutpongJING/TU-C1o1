#6510742460 Putthipong Soongsuwan
hours_intput = int(input("Enter parking hours (>=0): "))
minutes_input = int(input("Enter parking minutes (0-59): "))
if hours_intput == 0:
    fee = 0
elif minutes_input != 0:
    fee = hours_intput*20 + 20
else:
    fee = hours_intput*20
print(f"Parking for {hours_intput} hour and {minutes_input} min. The fee is {fee} baht.")