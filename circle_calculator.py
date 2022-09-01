#6510742460 พุฒิพงศ์ ซุงสุวรรณ
print("1.Circle Area\n2.Circumference")
Input_Radius = int(input("Your choice: "))
Radius = float(input("Input Radius: "))
PI = 3.14
if Input_Radius == 1:
    Circle_area = PI * (Radius ** 2)
    print(f"Circle Area: {Circle_area}")
if Input_Radius == 2:
    Cirecumference =2 * PI *Radius
    print(f"Cirecumference: {Cirecumference}")