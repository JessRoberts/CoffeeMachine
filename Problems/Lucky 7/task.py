i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
print(i)

numbers = range(int(input()))
for number in numbers:
    number = int(input())
    if number % 7 == 0:
        print(number ** 2)
