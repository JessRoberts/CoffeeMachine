a = int(input())
b = int(input())
h = int(input())
if a <= h <= b:
    print("Normal")
else:
    if a < h > b:
        print("Excess")
    else:
        print("Deficiency")
