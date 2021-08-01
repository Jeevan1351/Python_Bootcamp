def words():
    w = input().split()
    c_w = [word for word in w]
    return w, c_w

def main():
    wrds, c_words = words()
    wrds.sort()
    print(wrds)
    print(c_words)
    print(sorted(c_words))

main()
