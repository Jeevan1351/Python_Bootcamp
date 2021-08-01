import math

def input_dimensions():
    l = float(input("Enter the length of the tromboloid: "))
    b = float(input("Enter the breadth of the tromboloid: "))
    h = float(input("Enter the height of the tromboloid: "))
    return l, b, h

def vol_comp(l, b, h):        
    k = (l+b+h)**2
    volume = h**2 * b**2 / k**0.5
    r = (3/4 * math.pi* volume)**(1/3)
    return volume, r

def display(ans):
    volume, r = ans
    print("Volume of tromboloid: {:.3f}".format(round(volume, 3)))
    print("The radius of sphere with equivalent volume is: {:.3f}".format(round(r, 3)))

def main():
    length, breadth, height = input_dimensions()
    display(vol_comp(length, breadth, height))

main()
