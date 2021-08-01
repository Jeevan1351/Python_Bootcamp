def get_lot():
    line = input()[2:-2]
    return [tuple(t[1:-1].split("\', \'")) for t in line.split('), (')]    


def lot_to_cs(listOfTuples):
    string = ""
    for (a, b) in listOfTuples:
        string += a+"="+b+";"
    return string


def display(l):
    print(l)


def main():
    lot = get_lot()
    cs = lot_to_cs(lot)
    display(cs)


main()
