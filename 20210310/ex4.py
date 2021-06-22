import sys

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("n: "))
        
    if n % 6 == 0:
        print("2和3的公倍數")
    elif n % 3 == 0:
        print("3的倍數")
    elif n % 2 == 0:
        print("2的倍數")
    else:
        print("都不是")

if __name__ == "__main__":
    main()