#6510742460 พุฒิพงศ์ ซุงสุวรรณ
print("1.Circle Area\n2.Circumference")
Input_Choice = int(input("Your choice: "))
PI = 3.14
if Input_Choice == 1:
    Radius = float(input("Input Radius: "))
    Circle_area = PI * (Radius ** 2)
    print(f"Circle Area: {Circle_area}")
elif Input_Choice == 2 :
    Radius = float(input("Input Radius: "))
    Cirecumference =2 * PI *Radius
    print(f"Cirecumference: {Cirecumference}")
else :
    print("error")