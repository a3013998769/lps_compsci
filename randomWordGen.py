wordsFile = open('words.txt', 'r')
myWord = wordsFile.readline()
wordslist = []
while myWord != '':
    # as long as there are more words,
    # put the word in the list & read another.
    
    wordslist.append(myWord)
    myWord = wordsFile.readline()
print("Welcome to this file. In this file, you will choose a random number and we will print the word that matches the number in the dictionary.")
print("Would you like to play this game? y/n")
choose = str(raw_input())
if choose == "y":
    loop = True
    while loop == True:
        print("Which number would you like to choose for the lowest number?")
        answer1 = int(raw_input())
        print("Which number would you like to choose for the highest number?")
        answer2 = int(raw_input())
        print("OK. Here it is.")
        import random
        myRandNum = random.randint(answer1,answer2)
        print(str(wordslist[myRandNum]))
        print("Do you want to keep playing? y/n")
        choose2 = str(raw_input())
        if choose2 == "n":
            print("Thanks for using this program.")
            loop = False
        if choose2 == "y":
            print("OK. Let's keep going.")
if choose == "n":
    print("Thanks for using this program.")
