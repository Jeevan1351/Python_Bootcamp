def get_lot():
    return input()


def lot_to_cs(listOfTuples):
    string = ""
    for (a, b) in listOfTuples:
        string += a+"="+b+";"
    return string


def display(l):
    print(l)


def main():
    cs = get_lot()
    lot = lot_to_cs(cs)
    display(lot)


main()
