l = float(input("Enter the length of the tromboloid: "))
b = float(input("Enter the breadth of the tromboloid: "))
h = float(input("Enter the height of the tromboloid: "))
k = float(input("Enter the Characteristic constant of the tromboloid: "))

volume = h**2 * b**2 / k**0.5

r = 3 / 4 * (volume**(1/3))

print(f"Volume of tromboloid: {volume}")
print(f"The radius of sphere with equivalent volume is: {r}")
