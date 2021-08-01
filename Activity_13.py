def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def input_number():
    return int(input())

def display(n):
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


def main():
    a = input_number()
    display(a)

main()
