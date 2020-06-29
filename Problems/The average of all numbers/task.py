a = int(input())
b = int(input())
c = 0
d = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        c += 1
        d += i
print(d / c)
