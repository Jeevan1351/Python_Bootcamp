def get_values():
    line = input().split()
    dicts = {line[i]:line[i+1] for i in range(0, len(line), 2)}
    return dicts

def display(a):
    print(a)


def sorting(given):
    return dict(sorted(given.items(), key = lambda x: x[1]))

def main():
    d = get_values()
    sorted_d = sorting(d)
    display(sorted_d)

main()
