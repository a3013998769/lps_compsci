def isPrime(n): #Create a method that will be used to calculate the prime numbers
    x = range(2,n) #Set x equal to numbers in order from 2 to 10000
    for i in x: #Get the numbers out of the range
        y = n % i #Find the reminders
        if y == 0: 
            return False #Return false if the reminderis zero
        if y != 0 and i == n-1:
            return True #Return true if y is unequal to zero and i is equal to n-1 
print("welcome to the primelister!")
print("In this program, it will list all of the prime numbers between 2 and 10000.")
number = range(2,10000) #Set the range
b = open("Primes.txt", "w")
for num in number: #Get the numbers out
    if isPrime(num):
        b.write(str(num) + " ") #Write the prime numbers
