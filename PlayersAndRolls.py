import random
def HowManyPlayers():
    print("It is recommended to put this game into fullscreen.")
    print("How many players? (2-4)")
    while True:
            try:
                    x = int(input())
                    if x == 4:
                            return 4
                    elif x == 3:
                            return 3
                    elif x == 2:
                            return 2
                    else:
                            print("That is not 2, 3, or 4")
            except Exception:
                    print("That isn't a int.")

rollOne = 0
rollTwo = 30

def DiceRoll(y):
        global rollOne
        global rollTwo
        rollOne = 1
        rollTwo = 1
        rollOne = random.randint(1, 6)
        rollTwo = random.randint(1, 6)
        s = DicePictures[rollOne-1] + " " + DicePictures[rollTwo-1] #12 left, 6 down 7 tota           
        print(s)
        return rollOne + rollTwo

def ReturnRollOne():
    return rollOne

def ReturnRollTwo():
    return rollTwo

DicePictures = ['''
  _________ 
 |         |
 |         |
 |    0    |
 |         |
 |_________|''','''
  _________ 
 |         |
 |  0      |
 |         |
 |      0  |
 |_________|''','''
  _________ 
 |         |
 |  0      |
 |    0    |
 |      0  |
 |_________|''','''
  _________ 
 |         |
 |  0   0  |
 |         |
 |  0   0  |
 |_________|''','''
  _________ 
 |         |
 |  0   0  |
 |    0    |
 |  0   0  |
 |_________|''','''
  _________ 
 |         |
 |  0   0  |
 |  0   0  |
 |  0   0  |
 |_________|''']
