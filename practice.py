print("Welcome to my numberical guessing game.")
print("For what number which between 1 and 1000 would you like to multiply?")
number = int(input())
print("For what number do you want to be the upper limit of the multiplication?")
upper_limit = int(input())
times = 0
while number >= 1 and number <= 1000 and number * times <= upper_limit:
	number2 = number * times
	print(str(times) + " times " + str(number) + " equal " + str(number2))
	times = int(times + 1)
if number * times >= upper_limit:
	print("Thanks for using my program!")
	print("There are " + str(times - 1) + " integer multiples of " + str(number) + " that are less than " + str(upper_limit) + ".")
