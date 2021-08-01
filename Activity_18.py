def get_cs():
    return input()


def cs_to_dict(cs):
    my_dict = {}
    for pair in cs.split(';'):
        l, r = pair.split('=')
        my_dict[l] = r
    return my_dict


def display(c):
    print(c)


def main():
    cs = get_cs()
    d = cs_to_dict(cs)
    display(d)


main()
