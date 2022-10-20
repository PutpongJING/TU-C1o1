#6510742460 Putthipong Soongsuwan
num_wheels = int(input("Please input number of wheels of your vehicle: "))
toll_way = int(input("Distance of your toll way (km): "))
if num_wheels == 4:
    if toll_way < 10:
        a =40
    elif toll_way > 50:
        a =60
    else :
        a =50
elif num_wheels > 10:
    if toll_way < 10:
        a =80
    elif toll_way > 50:
        a =90
    else :
        a =100
else :
    if toll_way < 10:
        a =60
    elif toll_way > 50:
        a =70
    else :
        a =80
print(f"Total cost of your toll is {a} THB")