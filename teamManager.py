class Player(object):

  def __init__(self, name, age, goals):
    self.name = name
    self.age = age
    self.goals = goals
    
  def getstats(self):
    stats = "This player's name is " + str(self.name) + ", and his/her age is " + str(self.age) + ", his/her goal is " + str(self.goals) 
    
loop = True
myplayers = []
while loop == True:
  
  print("What do you want to do to your new team? Please enter your choice and press enter.")
  print("(1)I want to add a new player.")
  print("(2)I want to check the list of players.")
  print("(0)I want to exit.")
  
  answer = int(input())
  if answer == 0:
    loop = False
  if answer == 1:
    print("What's your new player's name?")
    answer1 = input()
    print("So, what's your new player's age?")
    answer2 = input()
    print("Now is the last question. What's your player's goals?")
    answer3 = input()
    newplayer = Player(answer1, answer2, answer3)
    print(newplayer.getstats())
    myplayers.append(newplayer)
  if answer == 2:
    for lists in myplayers:
      print(lists.getstats())
    
