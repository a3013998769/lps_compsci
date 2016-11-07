print("How much do the nachos cost?")
nacho_price = int(raw_input())
print("How much do you have in your pocket?")
cash = int(raw_input())

if nacho_price > cash:
	print("Sorry, no ncahos for you!")
if nacho_price < cash:
	print("Woot, nachos!")
if nacho_price == cash:
	print("That sure was lucky!")
print("Thanks for using nacho_buyer.py.")




print("Welcome to the convenience store!")
print("Enter your age:")
age = input()

age = int(age)

if age >= 18:
  print("Would you like to buy a lottery ticket?")

if age < 6:
  print("Would you like to buy a lollipop?")
