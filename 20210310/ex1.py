a = [i for i in range(1,21)]
print(a)
b = [i for i in a if i%2 == 0]
print(b)
c = [i for i in a if i%2 == 1]
print(c)
a = a[::2]
print(a)