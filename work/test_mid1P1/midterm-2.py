#6510742460 Putthipong Soongsuwan
x_input = int(input("Enter x : "))
x_i = 0
while x_input != 0 :
    x_i = x_i+x_input % 10
    x_input = (x_input-x_input%10)/10 
print(f"The total sum of all digits: {int(x_i)}")