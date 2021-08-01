def get_cs():
    return input()


def cs_to_lot(string):
    separated = string.split(';')
    listOt = []
    for i in separated:
        listOt.append(tuple(i.split('=')))
    return listOt


def display(l):
    print(l)


def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    display(lot)


main()
