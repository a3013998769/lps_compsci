print("welcome to my simple game.")
print("In this game, you can guess my number, it is bigger than 64 and less than 89.")
fave = 75
guess = raw_input()
guess = int(guess)

if guess >= 76:
	print("Sorry, this answer is incorrect, you can try again.")

if guess < 75:
	print("sorry, this is answer is incorrect, you can try again.")
	
if guess == 75:
	print("Great, you get the answer.")	






