import math
import random
import time
import matplotlib.pyplot as plt 

from os import system, name
def screenclear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')
#import matplotlib.pyplot as plt
#import numpy as np

#Variable Defining (REMEMBER TO global IN FUNCTIONS)
money = 5000000
displaymoney = str(money/1000) + "k"
day = 0
issuesamount = 0
leaderName = ""
nationName = ""

civilrights=50
freedom=5
economy=50
satisfaction = 50
war=False

tokens = 50

c=0

names = ["Ralph","Joshua", "Adhit", "Ethan", "Jayden", "Henry", "John", "Harry", "Bob", "Rob", "Tommy", "Wilbur", "Ash", "George","Ethan", "James","Oskar","Meky"]
nations = ["L'Manberg","3mber","D-City","S-Union","Austrialia","Danaca","Antarctica"]

alphabet = ["A", "B", "C", "D"]

enemy = [["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "]]

record = [["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "]]

ships = [["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "],["■ ","■ ","■ ","■ "]]

b = ""


def printRecord():
  print("Enemy Ships:")
  for y in range(4):
    print(alphabet[y],end=" ")
    for x in range(4):
      print(record[y][x],end="")
    print("")

  print("  1 2 3 4")

def printShips():
  print("Your Ships:")
  for y in range(4):
    print(alphabet[y],end=" ")
    for x in range(4):
      print(ships[y][x],end="")
    print("")

  print("  1 2 3 4")

def coord():
  global b
  b = ""
  b = input()
  while True:
    if len(b) == 2:
      if b[0] in alphabet:
        try:
          if int(b[1]) >= 1 and int(b[1]) <= 4:
            return
          else:
            print("Please enter a valid coordinate, for example 'A2'!")
            b = input()
        except:
          print("Please enter a valid coordinate, for example 'B3'!")
          b = input()
      else:
        print("Please enter a valid coordinate, for example 'D1'!")
        b = input()
    else:
      print("Please enter a valid coordinate, for example 'C4'!")
      b = input()

def placeShip():
  while True:
    y = alphabet.index(b[0])
    x = int(b[1])-1
    if ships[y][x] == "■ ":
      ships[y][x] = "O "
      break
    else:
      print("Please place your ship on an empty square!")
      coord()






def battleship():

  screenclear()
  print("Battleship\n")
  printShips()

  print("Input a coordinate to place your first ship!")
  coord()
  placeShip()
  screenclear()
  print("Battleship\n")
  printShips()

  print("Input a coordinate to place your second ship!")
  coord()
  placeShip()
  screenclear()
  print("Battleship\n")
  printShips()

  print("Input a coordinate to place your third ship!")
  coord()
  placeShip()

  for i in range(3):
    while True:
        y = random.randint(0,3)
        x = random.randint(0,3)
        if enemy[y][x] == "■ ":
          enemy[y][x] = "O "
          break

  win = False

  while True:

    screenclear()
    print("Battleship\n")
    print("Your move")

    printRecord()
    print("")

    print("Input a coordinate to launch a missile to")
    coord()

    

    

    while True:
      y = alphabet.index(b[0])
      x = int(b[1])-1

      if enemy[y][x] == "O ":
        print("You sank a ship!\n")
        record[y][x] = "\033[0;91;48mX \033[0;30;39m"
        enemy[y][x] = "X "
        break
      elif enemy[y][x] == "■ ":
        print("You missed!\n")
        record[y][x] = "x "
        enemy[y][x] = "x "
        break
      else:
        print("Please enter a valid square!")
        coord()

    screenclear()

    print("Battleship")


    if ("O " not in enemy[0]) and ("O " not in enemy[1]) and ("O " not in enemy[2]) and ("O " not in enemy[3]):
      win = True
      break

    print("Enemy's move\n")

    while True:
      y = random.randint(0,3)
      x = random.randint(0,3)
      if ships[y][x] == "■ ":
        ships[y][x] = "x "
        print("The enemy missed!")
        break

      elif ships[y][x] == "O ":
        ships[y][x] = "\033[0;91;48mX \033[0;30;39m"
        print("The enemy hit a ship!")
        break

    printShips()

    input("Press any key to continue")

    if ("O " not in ships[0]) and ("O " not in ships[1]) and ("O " not in ships[2]) and ("O " not in ships[3]):
      win = False
      break

  screenclear()
  if win:
    print("YOU WON!")
    return
  else:
    print("YOU LOST!")
    return




def choice(question):
  global c
  try:
    c = int(input(question))
  except:
    print("That is not a valid input!")
    choice(question)

def foreignpolicy():
  
  print(" \033[0;94;48mFOREIGN POLICY MENU\033[0;30;39m")
  
  print("1: Declare war")
  print("2: Form alliance")
  print("3: Sign trade agreement")
  print("4: Improve relationships")
  print("5: Exit menu")

  choice("Your selection")

  if c == 1:
    screenclear()
    battleship()
    
  elif c == 2:
    print("FORM ALLIANCE")
  elif c == 3:
    print("SIGNING TRADE AGREEMENT")
  elif c == 4:
    print("IMPROVING RELATIONSHIPS")
  
  elif c == 5:
    print("Exiting menu...")

def civilian():
  global tokens
  print(" \033[0;94;48mMINIGAME MENU\033[0;30;39m")
  print("You currently have",tokens,"tokens.")
  print("1: Play Guess the Number")
  print("2: Play Slots (10 - 50 Tokens)")
  print("3: Play Spin the Wheel (10 Tokens)")
  print("4: Play Horse Betting")
  print("5: Return to main menu")
  choice("Your selection:")
  print("")
  screenclear()
  if c == 1:
    print("Welcome to Guess the Number!")
    print("This game, you guess a number between 1 and 10, and we will tell you whether the number is higher or lower")
    print("If you get it right first try, we give you 3x your bet")
    print("If you get it right after 1 wrong try, we give you 2x your bet")
    print("If you get it right after 2 wrong tries, we give you 1x your bet")
    print("If you get it right after 3  wrong tries, we give you 0.5x your bet")
    print("3+ wrong tries and you lose all your tokens")
    print("Enter 0 in the 'How much would you like to bet?' to return to main menu")
    bet = int(input("How much would you like to bet? "))
    if bet > tokens:
      print("You do not have enough money! Returning to main menu...")
    elif bet == 0:
      print("Returning to main menu...")
    elif bet > 0:
      win = False
      highlownum = random.randint(1, 10)
      wrongtries = 0
      while win == False:
          guess = int(input("Guess any number"))
          if guess == highlownum:
              print("Correct number!")
              win = True
          elif guess > highlownum:
              print("Lower!")
              wrongtries = wrongtries + 1
          elif guess < highlownum:
              print("Higher!")
              wrongtries = wrongtries + 1
      if wrongtries == 0:
          tokens = tokens + (bet*3)
          print("You won 3x Your bet!")
          print("New Balance: ",tokens)
      elif wrongtries == 1:
          tokens = tokens + (bet * 2)
          print("You won 2x Your bet!")
          print("New Balance: ", tokens)
      elif wrongtries == 2:
          print("You regained your original bet")
          print("New Balance: ", tokens)
      elif wrongtries == 3:
          tokens = tokens - (bet/2)
          print("You lost 0.5x Your bet!")
          print("New Balance: ", tokens)
      elif wrongtries > 3:
          tokens = tokens - bet
          print("You lost all your tokens. Maybe more luck next time!")
          print("New Balance: ", tokens)
      time.sleep(3)
      screenclear()
    elif bet <= 0:
      print("Invalid number, returning to main menu...")
  elif c == 2:
    end = False
    while end == False:
      print("Slots Menu")
      print("1: Check winning combinations")
      print("2: 777 Machine (10 Tokens)")
      print("3: Ross and Beth (20 Tokens)")
      print("4: Risk it to win it (50 Tokens)")
      print("5: Return to main menu")
      choice("Your selection:")
      if c == 1:
        screenclear()
        print("777 Machine combinations")
        print("7 7 7 = 1000 Tokens")
        print("1 2 3 = 500 Tokens")
        print("7 8 9 = 500 Tokens")
        print("Any 3 Pairs = 250 Tokens")
        print("")
        print("Ross and Beth Machine combinations")
        print("7 7 7 = 2000 Tokens")
        print("1 2 3 = 1000 Tokens")
        print("7 8 9 = 1000 Tokens")
        print("Any 3 Pairs = 500 Tokens")
        print("")
        print("Risk it to win it Machine combinations")
        print("7 7 7 = 5000 Tokens")
        print("1 2 3 = 2500 Tokens")
        print("7 8 9 = 2500 Tokens")
        print("Any 3 Pairs = 1250 Tokens")
        waiting = input("Press enter to continue")
        screenclear()
      elif c == 2 or c == 3 or c == 4:
        screenclear()
        if c == 2 and tokens > 10:
          bet = 10
          tokens = tokens - 10
          print("New Token Balance:", tokens)
        elif c == 3 and tokens > 20:
          bet = 20
          tokens = tokens - 20
          print("New Token Balance:", tokens)
        elif c == 4 and tokens > 50:
          bet = 50
          tokens = tokens - 50
          print("New Token Balance:", tokens)
        waiting = input("Press enter to spin the machine!")
        screenclear()
        for i in range(10):
          num1 = random.randint(1,9)
          decimaltime = random.randint(3,7)
          decimaltime = decimaltime/10
          print(num1)
          time.sleep(decimaltime)
          screenclear()
        for i in range(10):
          num2 = random.randint(1,9)
          decimaltime = random.randint(3,7)
          decimaltime = decimaltime/10
          print(num1,num2)
          time.sleep(decimaltime)
          screenclear()
        for i in range(10):
          num3 = random.randint(1,9)
          decimaltime = random.randint(3,7)
          decimaltime = decimaltime/10
          print(num1,num2,num3)
          time.sleep(decimaltime)
          screenclear()
        if num1 == 7 and num2 == 7 and num3 == 7:
          print("YOU WON THE JACKPOT")
          print("You earned",bet*100)
          tokens = tokens + (bet*100)
          print("New Balance:",tokens)
        if num1 == 1 and num2 == 2 and num3 == 3:
          print("You won the 123 Combination!")
          print("You earned",bet*50)
          tokens = tokens + (bet*50)
          print("New Balance:",tokens)
        if num1 == 7 and num2 == 8 and num3 == 9:
          print("You won the 789 Combination!")
          print("You earned",bet*50)
          tokens = tokens + (bet*50)
          print("New Balance:",tokens)
        if num1 == num2 and num2 == num3:
          print("You won the 3 Pairs Combination!")
          print("You earned",bet*25)
          tokens = tokens + (bet*25)
          print("New Balance:",tokens)
        else:
          print("You did not win anything. Better luck next time.")
        waiting = input("Press enter to continue")
        screenclear()
      if c == 5:
        print("Returning to Main Menu...")
        end = True
        time.sleep(1)
        screenclear()
  elif c == 3:
    print("\033[0;31;48mSPIN THE WHEEL\033[0;31;39m")
    print("Loading game...")
    outtaloup = False
    if tokens < 10:
      print("You do not have enough money!")
      print("Returning to main menu...")
      outtaloup = True
    if outtaloup == False:
      allnums = [1,1,1,2,2,2,3,3,3,5,5,10,20,50,100]
      wheelnums = []
      for i in range(20):
        wheelnum = random.randint(0,14)
        wheelnums.append(allnums[wheelnum])
      time.sleep(1)
      screenclear()
      tokens = tokens - 10
      print("New token balance:",tokens)
      waiting = input("Press enter to Spin the wheel!")
      screenclear()
      winningnum = 5
      p1 = 3
      p2 = 5
      f1 = 10
      f2 = 2
      f3 = 6
      l = 0
      for i in range(35):
        p3 = p2
        p2 = p1
        p1 = winningnum
        winningnum = f1
        f1 = f2
        f2 = f3
        newnum =  random.randint(0,19)
        newnumber = wheelnums[newnum]
        f3 = newnumber
        print(p3)
        print(p2)
        print(p1)
        print("\033[32m" + str(winningnum) + "\033[0m")
        print(f1)
        print(f2)
        print(f3)
        l = l + 0.01
        time.sleep(l)
        screenclear()
      print(p3)
      print(p2)
      print(p1)
      print("\033[32m" + str(winningnum) + "\033[0m")
      print(f1)
      print(f2)
      print(f3)
      print("You won",winningnum,"token(s)!")
      winningtokens = int(winningnum)
      tokens = tokens + winningtokens
      print("New Token Balance:",tokens)
      waiting = input("Press enter to return to the main menu")
    screenclear()
  elif c == 4:
    print("\033[0;34;48mHorse Betting\033[0;30;39m")
    print("Loading game...")
    time.sleep(1)
    screenclear()
    print("Welcome to Horse Betting")
    print("Here you can bet on a horse, and win or lose depending on the race.")
    print("There are 5 horses each race, each with different win and lose statistics")
    print("The higher win change a horse has, the less win amount you will get by betting on them")
    print("")
    print("Today's horses:")
    horsechange = random.randint(1,5)
    horsechange2 = random.randint(1,5)
    horse1 = 20 + horsechange
    horse2 = 8 + horsechange2
    horse3 = 23 - horsechange
    horse4 = 15
    horse5 = 34 - horsechange2

    print("Horse 1 win chance:",horse1,"%", "Win multiplier of 2x")
    print("Horse 2 win chance:", horse2, "%", "Win multiplier of 2.5x")
    print("Horse 3 win chance:", horse3, "%", "Win multiplier of 1.8x")
    print("Horse 4 win chance:", horse4, "%", "Win multiplier of 2x")
    print("Horse 5 win chance:", horse5, "%", "Win multiplier of 1.2x")
    print("Enter 0 to return to main menu")
    bet = int(input("How much would you like to bet today?"))
    if bet == 0:
      print("Returning to main menu...")
    elif bet > 0 and tokens > bet:
      tokens = tokens - bet
      horse = int(input("Which horse will you bet on? (Enter their number)"))
      print("Racing...")
      time.sleep(3)
      horsewin = random.randint(1,100)
      if horsewin >= 0 and horsewin < horse1:
          print("Horse 1 wins the race!")
          winnerhorse = 1
      elif horsewin >= horse1 and horsewin < horse2 + horse1:
          print("Horse 2 wins the race!")
          winnerhorse = 2
      elif horsewin >= horse2 + horse1 and horsewin < horse3 + horse2 + horse1:
          print("Horse 3 wins the race!")
          winnerhorse = 3
      elif horsewin >= horse3 + horse2 + horse1 and horsewin < horse4 + horse3 + horse2 + horse1:
          print("Horse 4 wins the race!")
          winnerhorse = 4
      elif horsewin >= horse4 + horse3 + horse2 + horse1 and horsewin <= 100:
          print("Horse 5 wins the race!")
          winnerhorse = 5
      if horse == winnerhorse:
          print("You won!")
          if winnerhorse == 1:
              tokens = tokens + (bet*2)
              print("You won ",bet*2)
          if winnerhorse == 2:
              tokens = tokens + (bet*2.5)
              print("You won ", bet * 2.5)
          if winnerhorse == 3:
              tokens = tokens + (bet*1.8)
              print("You won ", bet * 1.8)
          if winnerhorse == 4:
              tokens = tokens + (bet*2)
              print("You won ", bet * 2)
          if winnerhorse == 5:
              tokens = tokens + (bet*1.2)
              print("You won ", bet * 1.2)
      else:
        print("You lost",bet,"tokens")
      time.sleep(2)
      print("New balance: ",tokens)
      time.sleep(2)
    else:
      print("Invalid Input. Returning to Main menu")
    screenclear()


  elif c == 5:
    print("Returning to main menu...")
    time.sleep(1)
    screenclear()
      




# print("1: View stock market")
# print("2: View nation fianances (bugdet)")
# print("3: View industrial production")
# print("4: ")

#Introduction function
def startup():
  global leaderName, nationName
  print("")
  leaderName=str(input("What would your leader like to be named?"))
  nationName=str(input("What would country be called"))
  screenclear()
  
def daily():
  global money, day, civilrights, freedom, economy, war, issuesamount, c, satisfaction, tokens
  tokens = tokens + 20
  day = day + 1
  issuesamount =+ 1
  dayover = False
  print("\n\nDay",day,"\n")
  print("Daily Report:")
  print("Civil Rights:",civilrights)
  print("Government Satisfaction:",satisfaction)
  while dayover == False:
  
    print("\n \033[0;92;48mMAIN MENU\033[0;30;39m")
    print("1: Go to foreign policy menu")
    print("2: Go to economy menu")
    print("3: Go to minigame menu")
    print("4: Skip day (sleep in)")
    #print("5: Gp to military menu")
    choice("Your Selection")
    screenclear()
    if c == 1:
      foreignpolicy()
    elif  c == 2:
      economy()
    elif c == 3:
      civilian()
    elif c == 4:
      dayover = True
      print("")
    else:
      print("Invalid Imput, please enter again.")

stockmarket=random.randint(200, 1000)
stockaos=random.randint(100000, 100000000000)
days=[]
stockpricehistory=[]
taxrate=20
admin=10
defense=10
education=random.randint(10,26)
environment=random.randint(1,19)
industry=random.randint(10,30)
foraid=random.randint(1,10)
laworder=random.randint(10,30)
transport=random.randint(1,19)
welfare=random.randint(10,40)
religion=random.randint(1,7)
#Book Publishing","Information Technology","Cheese Exports","Furniture Restoration","Pizza Delivery","Retail","Arms Manufacturing","Basket Weaving","Insurance","Car Production","Trout Fishing","Beverage Sales","Timber Woodchiping","Gambling","Mining"]
def economy():
    global day,stockmarket,stockaos,days,stockpricehistory,taxrate,admin,defense,education,environment,industry,foraid,laworder,transport,welfare,religion
    day=day+1
    #screenclear()
    days.append(day)
    admin=random.randint(int(admin*0.9),int(admin*1.1))
    defense=random.randint(int(defense*0.9),int(defense*1.1))
    education=random.randint(int(education*0.9),int(education*1.1))
    environment=random.randint(int(environment*0.9),int(environment*1.1))
    industry=random.randint(int(industry*0.9),int(industry*1.1))
    foraid=random.randint(int(foraid*0.9),int(foraid*1.1))
    laworder=random.randint(int(laworder*0.9),int(laworder*1.1))
    transport=random.randint(int(transport*0.9),int(transport*1.1))
    welfare=random.randint(int(welfare*0.9),int(welfare*1.1))
    religion=random.randint(int(religion*0.9),int(religion*1.1))
    stockmarket = stockmarket + random.randint(-7, 10)
    newvar=stockmarket*stockaos
    stockpricehistory.append(newvar)
    industrialproduction=(100/industry)*newvar
    govspending=newvar*(100-taxrate)/100
    goodevents = ["Companies reported strong, above forecast quarterly results today ",
                      "Many companies merged together, giving shareholders more power",
                      "After sanctions against Guomeristania, a large nation, were lifed, companies can do business there again",
                      "The federal reserve decide to cut corporate tax"]
    badevents = ["After the government reported a recession, companies had to lay off employeess.",
                     "A new law passed by parliament forces companies to comply with stringent regulations.",
                     "A hostile but large foreign country closed its markets, cutting companies profits",
                     "A global war has been declared, and stocks are sinking"]
    industries=["Book Publishing","Information Technology","Cheese Exports","Furniture Restoration","Pizza Delivery","Retail","Arms Manufacturing","Basket Weaving","Insurance","Car Production","Trout Fishing","Beverage Sales","Timber Woodchiping","Gambling","Mining"]
    goodevent = 0
    goodeventnumber = 0
    goodeventhappening = False
    badevent = 0
    badeventnumber = 0
    badeventhappening = False
    if day > 2:
        goodevent = random.randint(10, 50)
        badevent = random.randint(10, 40)
        if day == 11:
            goodevent = 30
        elif day == 12:
            badevent = 30
        if goodevent == 30:
            goodeventhappening = True
            stockmarket = stockmarket + (stockmarket * 0.1)
        elif badevent == 30:
             badeventhappening = True
             stockmarket = stockmarket - (stockmarket * 0.1)   
    print(" \033[0;94;48mECONOMY MENU\033[0;30;39m")
    print("1: View stock market")
    print("2: View nation fianances (bugdet)")
    print("3: View industrial production")
    print("4: Issue a bond")
    print("5: Exit back to main menu")
    choice("Your selection")
    if c == 1:
        print("STOCK MARKET")
        plt.xlabel("Date")
        plt.ylabel("Stock Market Market Capitalization/ Trillion Dollars")
        plt.title("Stock Market")
        plt.plot(days,stockpricehistory)
        plt.show()
        if goodeventhappening == True:
                print("A good event happened! All stock prices increased by 10%")
                goodeventnumber = random.randint(0, 3)
                print(goodevents[goodeventnumber])
                print("")
        if badeventhappening == True:
                print("A bad event happened! All stock prices decreased by 10%")
                badeventnumber = random.randint(0, 3)
                print(badevents[badeventnumber])
                print("")
    elif c == 2:
        print("NATION FIANANCES (BUDGET)")
        print("Your tax rate is ",taxrate," at the moment")
        taxrate=int(input("What will your new tax rate be?"))
        while taxrate>100 or taxrate<0:
            taxrate=int(input("What will your new tax rate be?"))
        print("Government spending is", govspending,"dollars")
        my_data = [admin,defense,education,environment,industry,foraid,laworder,transport,welfare,religion]
        my_labels = 'Administration','Defense','Education','Environment','Industry','Foreign Aid','Law and Order','Transport','Welfare','Spirituality'
        plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
        plt.title('Government Expenditures')
        plt.axis('equal')
        plt.show()
    elif c == 3:
        print("INDUSTRIAL PRODUCTION")
        print("Your industrial production is valued at", industrialproduction)
        my_data = [newvar-govspending,govspending,1000000000]
        my_labels = 'Government','Private','Black Market'
        plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
        plt.title('Economy Composition')
        plt.axis('equal')
        plt.show()
    elif c == 4:
        print("ISSUE A BOND")
    elif c == 5:
        print("Exiting menu...")



startup()
while True:
  daily()
  print("Ending day...")
  time.sleep(1)
  screenclear()


def choice(question):
  global c
  try:
    c = int(input(question))
  except:
    print("That is not a valid input!")
    choice(question)
