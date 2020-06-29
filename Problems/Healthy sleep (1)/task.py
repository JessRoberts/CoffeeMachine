recommended = int(input())
over = int(input())
sleep = int(input())

if recommended <= sleep <= over:
    print("Normal")
elif sleep > over >= recommended:
    print ("Excess")
else:
    print("Deficiency")
