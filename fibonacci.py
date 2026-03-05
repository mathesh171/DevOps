n = int(input())
a, b = 0, 1

for i in range(0, n):
    print(a, end=" ")
    d = a + b
    a, b = b, d
