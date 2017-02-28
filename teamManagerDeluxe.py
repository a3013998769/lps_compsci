
class Player(object): #create the class

  def __init__(self, name, age, goals, position): #create the method contains name, age, goals, and position
    self.name = name #set each values of the method
    self.age = age
    self.goals = goals
    self.position = position
    
  def getstats(self): #create the method of getting the summary of the new teammate
    stats = ("name: " + str(self.name) + "\n" + "age: " + str(self.age) + "\n" + "goals: " + str(self.goals) + "\n" + "position: " + str(self.position)
    
    
loop = True #Create a loop
myplayers = [] #Create a list of myplayers
goalsamount = 0 #Calculate the amount of goals
goalsnumber = 0 #Calculate the amount of the number of goals 
agesamount = 0 #calculate the amount of goals
agesnumber = 0 #calculate the amount of the number of ages

while loop == True:
  print("Welcome to the teamManagerDeluxe! Which performance do you want to use?") #The new things of the Deluxe version. I added two more options.
  print("(1)I want to start a new team.")
  Print("(2)I want to open a file with an existing team.")
  answer1 = int(input())
  
  if answer == 1:
    print("What do you want to do to your new team? Please enter your choice and press enter.") #Starting asking user questions and do the next steps by their reactions.
    print("(1)I want to add a new player.")
    print("(2)I want to check the list of players.")
    print("(3)I want to calculate the average goals of members.")
    print("(4)I want to calculate the average age of members.")
    print("(5)I want to save my player list to a file.")
    print("(0)I want to exit.") #If you enter 0, you will exit from this program.
  
    answer = int(input()) #The user's answer should be an integer.
    if answer == 0:
      print("Thanks for using this program.")
      loop = False #The explanation is as same as line 28's.
    if answer == 1:
      print("What's your new player's name?") #Asking step by step.
      answer1 = input()
      print("So, what's your new player's age?")
      answer2 = input()
      print("What's your player's goals?")
      answer3 = input()
      print("What's your player's position?")
      answer4 = input()
      newplayer = Player(answer1, answer2, answer3, answer4)
      print(newplayer.getstats()) #Starting getting the new player's imformation.
      myplayers.append(newplayer) #Add a new item to the list of "myplayers".
      goalsamount =  goalsamount + int(answer3) #Try to calculate the amount of goals.
      goalsnumber = goalsnumber + 1 #Try to calculate the people.
      agesamount = agesamount + int(answer2) #Try to calculate the amount of ages.
      agesnumber = agesnumber + 1 #As same as line 44's explanation.
    if answer == 2:
      for lists in myplayers:
        print(lists.getstats()) #Getting the list and their introductions of each player.
    if answer == 3:
      averagegoals = goalsamount / goalsnumber 
      print("The average of teammates' goals is " + str(averagegoals) + ".") #calculate the average number of goals and print it.
    if answer == 4:
      averageages = agesamount / agesnumber
      print("The average of teammates' ages is " + str(averageages) + ".") #calculate  the average number of ages and print it. 
    if answer == 5:
      print("What's your file's name?")
      filename = input()
