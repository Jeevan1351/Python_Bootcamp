  
def get_cs():
    return input()


def cs_to_dict(cs):
    my_dict = {l:r for l,r in (t.split('=') for t in cs.split(';'))}
    return my_dict


def display(c):
    print(c)


def main():
    cs = get_cs()
    d = cs_to_dict(cs)
    display(d)


main()
