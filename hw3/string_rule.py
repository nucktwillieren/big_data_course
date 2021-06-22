n2ch = "".join([
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789-_",
])

ch2n = dict(zip(n2ch, range(len(n2ch))))

padding = "~"

def encode(string):
    data = ''.join(format(ord(x), '08b') for x in string)
    rem = len(data) % 6
    pad = 6 - rem
    encoded = ""
    if rem > 0: data = data + "0" * pad
    for i in range(0, len(data), 6):
        encoded += n2ch[int(data[i:i+6], 2)]
    padding_len = 4 - len(encoded) % 4
    encoded += padding*padding_len

    return encoded

def decode(string):
    count = string.count("~")
    string = string.rstrip("~")
    data = ''.join(format(ch2n[x], '06b') for x in string)[:-2*count]
    decoded = ""
    for i in range(0, len(data), 8):
        decoded += chr(int(data[i:i+8], 2))
    return decoded

def main():
    string = input("string: ")
    print("Input: ", string)
    encoded = encode(string)
    print("Encode: ", encoded)
    decoded = decode(encoded)
    print("Decode: ", decoded)



if __name__ == '__main__':
    main()
    