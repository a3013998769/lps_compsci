def prime(n):
    list = []
    x = range(2,n)
    for i in x:
        y = n % i
        if i == 0:
            list.append(n)
print("welcome to the primelister!")
print("In this program, it will list all of the prime numbers between 2 and 10000.")
number = range(2,10000)
for num in number:
  prime(num)
  
