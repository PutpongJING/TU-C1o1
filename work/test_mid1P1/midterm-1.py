#6510742460 Putthipong Soongsuwan
z = 0
x = int(input("Input x: "))
y = int(input("Input y: "))
if x % y != 0:
    y -= 2
    z += x
z+=1
print(f"z = {z}")
print(f"y = {y}")