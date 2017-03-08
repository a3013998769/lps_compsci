
class Player(object): #create the class

  def __init__(self, name, age, goals, position): #create the method contains name, age, goals, and position
    self.name = name #set each values of the method
    self.age = age
    self.goals = goals
    self.position = position
  def checkplayer(self, filename):
    a = open(filename, "r")
    b = a.readline()
    while b != "":
      print("This is one player's data, it contains his/her name, age, goals, and positions :" + b + "\n")
      b = a.readline()
      a.close()
  def getstats(self): #create the method of getting the summary of the new teammate
    stats = ("This is one player's name, age, goals, and position:" + str(self.name) + " " + str(self.age) + " " + str(self.goals) + " " + str(self.position) + "\n")
    return stats
    
  def getstringout(self, filename):
    o = open("store.txt","w")
    x = open(filename, "r")
    r = x.read()
    o.write(r)
    o.write(str(self.name) + " " + str(self.age) + " " +str(self.goals) + " " + str(self.position) + " " +"\n") 
    o.close()
    f = open("store.txt","r")
    z = f.read()
    x.close()
    y = open(filename, "w")
    y.write(z)
    y.close()
loop = True #Create a loop
myplayers = [] #Create a list of myplayers
goalsamount = 0 #Calculate the amount of goals
goalsnumber = 0 #Calculate the amount of the number of goals 
agesamount = 0 #calculate the amount of goals
agesnumber = 0 #calculate the amount of the number of ages


print("Welcome to the teamManagerDeluxe! Which performance do you want to use?") #The new things of the Deluxe version. I added two more options.
print("(1)I want to start a new team.")
print("(2)I want to open a file with an existing team.")
choice = int(raw_input())
  
if choice == 1:
  while loop == True:
    print("What do you want to do to your new team? Please enter your choice and press enter.") #Starting asking user questions and do the next steps by their reactions.
    print("(1)I want to add a new player.")
    print("(2)I want to check the list of players.")
    print("(3)I want to calculate the average goals of members.")
    print("(4)I want to calculate the average age of members.")
    print("(5)I want to save my player list to a file.")
    print("(0)I want to exit.") #If you enter 0, you will exit from this program.
  
    answer = int(raw_input()) #The user's answer should be an integer.
    if answer == 0:
      print("Thanks for using this program.")
      loop = False #The explanation is as same as line 28's.
    if answer == 1:
      print("What's your new player's name?") #Asking step by step.
      answer1 = str(raw_input())
      print("So, what's your new player's age?")
      answer2 = int(raw_input())
      print("What's your player's goals?")
      answer3 = int(raw_input())
      print("What's your player's position?")
      answer4 = str(raw_input())
      newplayer = Player(answer1, answer2, answer3, answer4)
      print(newplayer.getstats()) #Starting getting the new player's imformation.
      myplayers.append(newplayer) #Add a new item to the list of "myplayers".
      goalsamount =  goalsamount + int(answer3) #Try to calculate the amount of goals.
      goalsnumber = goalsnumber + 1 #Try to calculate the people.
      agesamount = agesamount + int(answer2) #Try to calculate the amount of ages.
      agesnumber = agesnumber + 1 #As same as line 44's explanation.
    if answer == 2:
      for lists in myplayers:
        print(lists.getstats())
    if answer == 3:
      averagegoals = goalsamount / goalsnumber 
      print("The average of teammates' goals is " + str(averagegoals) + ".") #calculate the average number of goals and print it.
    if answer == 4:
      averageages = agesamount / agesnumber
      print("The average of teammates' ages is " + str(averageages) + ".") #calculate the average number of ages and print it. 
    if answer == 5:
      print("What's your file's name?")
      filename = raw_input()
      for myplayer in myplayers:
        myplayer.getstringout(filename)
if choice == 2:
  print("So, could you tell me the file you want to open?")
  file1 = raw_input()
  myfile1 = open(file1, "r")
  while loop == True:  
    print("What do you want to do to your new team? Please enter your choice and press enter.") #Starting asking user questions and do the next steps by their reactions.
    print("(1)I want to add a new player.")
    print("(2)I want to check the list of players.")
    print("(3)I want to calculate the average goals of members.")
    print("(4)I want to calculate the average age of members.")
    print("(5)I want to save my player list to a file.")
    print("(6)I want to save my player list to this file.")
    print("(0)I want to exit.")
    answer = int(raw_input()) #The user's answer should be an integer.
    if answer == 0:
      print("Thanks for using this program.")
      loop = False #The explanation is as same as line 28's.
    if answer == 1:
      print("What's your new player's name?") #Asking step by step.
      answer1 = str(raw_input())
      print("So, what's your new player's age?")
      answer2 = int(raw_input())
      print("What's your player's goals?")
      answer3 = int(raw_input())
      print("What's your player's position?")
      answer4 = str(raw_input())
      newplayer = Player(answer1, answer2, answer3, answer4)
      print(newplayer.getstats()) #Starting getting the new player's imformation.
      myplayers.append(newplayer) #Add a new item to the list of "myplayers".      
      goalsamount =  goalsamount + int(answer3) #Try to calculate the amount of goals.
      goalsnumber = goalsnumber + 1 #Try to calculate the people.
      agesamount = agesamount + int(answer2) #Try to calculate the amount of ages.
      agesnumber = agesnumber + 1 #As same as line 44's explanation.
    if answer == 2:
      for lists in myplayers:
        print(lists.getstats())
      checkplayer1 = myfile1.readline()
      while checkplayer1 != "":
        print("This is one player's name, age, goals, and position:" + checkplayer1)
        checkplayer1 = myfile1.readline()
    if answer == 3:
      averagegoals = goalsamount / goalsnumber 
      print("The average of teammates' goals is " + str(averagegoals) + ".") #calculate the average number of goals and print it.
    if answer == 4:
      averageages = agesamount / agesnumber
      print("The average of teammates' ages is " + str(averageages) + ".") #calculate  the average number of ages and print it. 
    if answer == 5:  
      print("What's your file's name?")
      filename = raw_input()
      for myplayer in myplayers: #Storing to the file you choose
        myplayer.getstringout(filename)
    if answer == 6:
      for myplayer in myplayers:
        myplayer.getstringout(file1)
            
