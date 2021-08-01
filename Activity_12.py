def input_numbers():
    line = input().split()
    numbers = [int(i) for i in line]
    return numbers

def maxi(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    return n3

def display(n1, n2, n3, min):
    print(f"{min} is the greatest number among {n1}, {n2} and {n3}.")

def main():
    a, b, c = input_numbers()
    min = maxi(a, b, c)
    display(a, b, c, min)

main()
