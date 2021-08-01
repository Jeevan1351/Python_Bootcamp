l = float(input("Enter the length of the tromboloid: "))
b = float(input("Enter the breadth of the tromboloid: "))
h = float(input("Enter the height of the tromboloid: "))
k = (l+b+h)**2

volume = h**2 * b**2 / k**0.5

r = (3/4 * volume)**(1/3)

print("Volume of tromboloid: {:.3f}".format(round(volume, 3)))
print("The radius of sphere with equivalent volume is: {:.3f}".format(round(r, 3)))
