
def a_1():
    n = int(input("Enter a integer number: "))
    s = 0

    for i in range(n):
        three = i * 3
        five = i * 5
        if three > n: break
        if i % 5 != 0: s += three
        if five < n: s += five

    print(s)

def a_2():
    n = int(input("Enter a integer number: "))

    threes = sum([i for i in range(0,n,3)])
    fives = sum([i for i in range(0,n,5)])
    overlapped = sum([i for i in range(0,n,15)])

    print(threes + fives - overlapped)


if __name__ == "__main__":
    a_1()
    a_2()