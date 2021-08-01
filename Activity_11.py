def input_number():
    n = int(input())
    return n


def add(a, b):
    return a+b


def display(a, b, sum):
    print(f"{a} + {b} = {sum}")

def main():
    a = input_number()
    b = input_number()
    summation = add(a, b)
    display(a, b, summation)

main()
