print('%.2f' % (21/4))
num = int(input())

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("This number is not prime")
           break
   else:
       print("This number is prime")

else:
   print("This number is not prime")
