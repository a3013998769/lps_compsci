print("Welcome to my number guessing game.")
print("For what number which between 20 and 100 would you like to multiply?")
number = int(input())
times = 0
while number > 20 and number < 100 and number * times < 1000:
	number2 = number * times
	print(str(times) + " times " + str(number) + " equal " + str(number2))
	times = int(times + 1)
if number2 > 1000:
	print("Thanks for using my program!")
