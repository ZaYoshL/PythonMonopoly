import random
import sys
import math
import os
#import randint

Player1Money = 2000 #Money to start with
Player2Money = 2000
Player3Money = 2000
Player4Money = 2000
Player1Location = 1 #Starts out on go
Player2Location = 1
Player3Location = 1
Player4Location = 1
Player1InJail = 0
Player2InJail = 0
Player3InJail = 0
Player4InJail = 0
from MonopolyMap import MonopolyMap

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
        s = DicePictures[rollOne-1] + " " + DicePictures[rollTwo-1] #12 left, 6 down 7 total
        #ss = ""
        #for i in range(0, 11):
        #        for ii in range(1, 6):
        #                ss += Substr(s, ii, i)
        #        ss += "\n"
                        
        print(s)
        return rollOne + rollTwo

def GameOver():
    if Player1Money < 0:
        print("Player 1 has no more money.")
        if Player2Money > Player3Money and Player2Money > Player4Money:
            print("Player 2 has the most money, Player 2 is the winner.")
            input()
        elif Player3Money > Player2Money and Player3Money > Player4Money:
            print("Player 3 has the most money, Player 3 is the winner.")
            input()
        else:
            print("Player 4 has the most money, Player 4 is the winner.")
            input()
        sys.exit(0)
    elif Player2Money < 0:
        print("Player 2 has no more money.")
        if Player1Money > Player3Money and Player1Money > Player4Money:
            print("Player 1 has the most money, Player 1 is the winner.")
            input()
        elif Player3Money > Player1Money and Player3Money > Player4Money:
            print("Player 3 has the most money, Player 3 is the winner.")
            input()
        else:
            print("Player 4 has the most money, Player 4 is the winner.")
            input()
        sys.exit(0)
    elif Player3Money < 0:
        print("Player 3 has no more money.")
        if Player1Money > Player2Money and Player1Money > Player4Money:
            print("Player 1 has the most money, Player 1 is the winner.")
            input()
        elif Player2Money > Player1Money and Player2Money > Player4Money:
            print("Player 2 has the most money, Player 2 is the winner.")
            input()
        else:
            print("Player 4 has the most money, Player 4 is the winner.")
            input()
        sys.exit(0)
    elif Player4Money < 0:
        print("Player 4 has no more money.")
        if Player1Money > Player2Money and Player1Money > Player3Money:
            print("Player 1 has the most money, Player 1 is the winner.")
            input()
        elif Player2Money > Player1Money and Player2Money > Player3Money:
            print("Player 2 has the most money, Player 2 is the winner.")
            input()
        else:
            print("Player 3 has the most money, Player 3 is the winner.")
            input()
        sys.exit(0)


MediterraneanAve = 0
BalticAve = 0
ReadingRailroad = 0
OrientalAve = 0
VermontAve = 0
ConnecticutAve = 0
StCharlesPlace = 0
ElectricCompany = 0
StatesAve = 0
VirginiaAve = 0
PennsylvaniaRailroad = 0
StJamesPlace = 0
TennesseeAve = 0
NewYorkAve = 0
FreeParkingMoney = 0
KentuckyAve = 0
IndianaAve = 0
IllinoisAve = 0
BORailroad = 0
AtlanticAve = 0
VentnorAve = 0
WaterWorks = 0
MarvinGardens = 0
PacificAve = 0
NorthCarolinaAve = 0
PennsylvaniaAve = 0
ShortLineRailroad = 0
ParkPlace = 0
Boardwalk = 0


MediterraneanAveRent = 2
BalticAveRent = 4
ReadingRailroadRent = 25
OrientalAveRent = 6
VermontAveRent = 6
ConnecticutAveRent = 8
StCharlesPlaceRent = 10
ElectricCompanyRent = 4
StatesAveRent = 10
VirginiaAveRent = 12
PennsylvaniaRailroadRent = 25
StJamesPlaceRent = 14
TennesseeAveRent = 14
NewYorkAveRent = 16
KentuckyAveRent = 18
IndianaAveRent = 18
IllinoisAveRent = 20
BORailroadRent = 25
AtlanticAveRent = 22
VentnorAveRent = 22
WaterWorksRent = 4
MarvinGardensRent = 24
PacificAveRent = 26
NorthCarolinaAveRent = 26
PennsylvaniaAveRent = 28
ShortLineRailroadRent = 25
ParkPlaceRent = 35
BoardwalkRent = 50

list1, list2, list3, list4, list5 = [[] for _ in range(5)]
#             1                   2                3                4                 5                   6                  7              8                   9               10                11                12              13          14              15              16              17                 18              19                        20                 21         22           23                   24                         25              26                
list1 = ["Mediterranean Ave.", "Baltic Ave.", "Oriental Ave.", "Vermont Ave.", "Connecticut Ave.", "St. Charles Place", "States Ave.", "Virginia Ave.","St. James Place", "Tennessee Ave.", "New York Ave.", "Kentucky Ave.","Indiana Ave.","Illinois Ave.","Atlantic Ave.","Ventnor Ave.", "Marvin Gardens", "Pacific Ave.", "North Carolina Ave.", "Pennsylvania Ave.","Park Place", "Boardwalk", "Reading Railroad", "Pennsylvania Railroad","B. & O. Railroad","Short Line Railroad","Electric Company","Water Works"]
#Cost of places
#         1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
list2 = [60,60,100,100,120,140,140,160,180,180,200,220,220,240,260,260,280,300,300,320,350,400,200,200,200,200,150,150]
#Owner of the place
#         1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
list3 = [0, 0, 0,  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , 0  ,0   ,0]
#Rent
#         1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26         
list4 = [2, 4, 6,  6  ,8  ,10 ,10 ,12 ,14 ,14 ,16 ,18 ,18 ,20 ,22 ,22 ,24 ,26 ,26 , 28,35 ,50 ,25 ,25 ,25 ,25 , 0   ,0]
#Extra
list5 = [0, 0, 0,  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,  0,0  ,0  ,0  ,0  ,0  ,0 ,  0   ,0]
#Most likely need a mortgage value.
#Need to add waterworks and electric company to for loops once finish.

def UseTheList(LandedOn, WhosThis):
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        waterElectric = 0
        if list3[LandedOn] == 0 and WhosThis == 1:
            print("Player 1 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(can also use y/n)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player1Money < list2[LandedOn]:
                    print("You don't have enouge money to pay " + str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    list3[LandedOn] = 1
                    Player1Money -= list2[LandedOn]
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif list3[LandedOn] == 1 and WhosThis == 1:
            print("Player 1 has landed on "+str(list1[LandedOn])+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif list3[LandedOn] != 1 and list3[LandedOn] != 0 and WhosThis == 1:
            print("Player 1 has landed on "+str(list1[LandedOn])+"\nPlayer " + str(list3[LandedOn])+" owns this place and it cost $" + str(list4[LandedOn])+"\nPress enter.")
            Player1Money -= list4[LandedOn]
            if list3[LandedOn] == 2:
                Player2Money += list4[LandedOn]
            elif list3[LandedOn] == 3:
                Player3Money += list4[LandedOn]
            else:
                Player4Money += list4[LandedOn]
            GameOver()
            input()
        elif list3[LandedOn] == 0 and WhosThis == 2:
            print("Player 2 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(can also use y/n)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player2Money < list2[LandedOn]:
                    print("You don't have enouge money to pay " + str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    list3[LandedOn] = 2
                    Player2Money -= list2[LandedOn]
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif list3[LandedOn] == 2 and WhosThis == 2:
            print("Player 2 has landed on "+str(list1[LandedOn])+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif list3[LandedOn] != 2 and list3[LandedOn] != 0 and WhosThis == 2:
            print("Player 2 has landed on "+str(list1[LandedOn])+"\nPlayer " + str(list3[LandedOn])+" owns this place and it cost $" + str(list4[LandedOn])  +"\nPress enter.")
            #if LandedOn == 26 or LandedOn == 27:###################################################################################################################################################################################################################################
            #        waterElectric
            #else:
            Player2Money -= list4[LandedOn]
            if list3[LandedOn] == 1:
                Player1Money += list4[LandedOn]
            elif list3[LandedOn] == 3:
                Player3Money += list4[LandedOn]
            else:
                Player4Money += list4[LandedOn]
            GameOver()
            input()
        elif list3[LandedOn] == 0 and WhosThis == 3:
            print("Player 3 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(can also use y/n)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player3Money < list2[LandedOn]:
                    print("You don't have enouge money to pay "+str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    list3[LandedOn] = 3
                    Player3Money -= list2[LandedOn]
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif list3[LandedOn] == 3 and WhosThis == 3:
            print("Player 3 has landed on "+str(list1[LandedOn])+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif list3[LandedOn] != 3 and list3[LandedOn] != 0 and WhosThis == 3:
            print("Player 3 has landed on "+str(list1[LandedOn])+"\nPlayer " + str(list3[LandedOn])+" owns this place and it cost $" + str(list4[LandedOn])+"\nPress enter.")
            Player3Money -= list4[LandedOn]
            if list3[LandedOn] == 1:
                Player1Money += list4[LandedOn]
            elif list3[LandedOn] == 2:
                Player2Money += list4[LandedOn]
            else:
                Player4Money += list4[LandedOn]
            GameOver()
            input()
        elif list3[LandedOn] == 0 and WhosThis == 4:
            print("Player 4 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(can also use y/n)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player4Money < list2[LandedOn]:
                    print("You don't have enouge money to pay "+str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    list3[LandedOn] = 4
                    Player4Money -= list2[LandedOn]
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif list3[LandedOn] == 4 and WhosThis == 4:
            print("Player 4 has landed on "+str(list1[LandedOn])+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif list3[LandedOn] != 4 and list3[LandedOn] != 0 and WhosThis == 4:
            print("Player 4 has landed on "+str(list1[LandedOn])+"\nPlayer " + str(list3[LandedOn])+" owns this place and it cost $" + str(list4[LandedOn])+"\nPress enter.")
            Player4Money -= list4[LandedOn]
            if list3[LandedOn] == 1:
                Player1Money += list4[LandedOn]
            elif list3[LandedOn] == 2:
                Player2Money += list4[LandedOn]
            else:
                Player3Money += list4[LandedOn]
            GameOver()
            input()

def LandedPlaces(landedOn, WhosThis):
    global list4
    global FreeParkingMoney
    global Player1Money 
    global Player2Money
    global Player3Money
    global Player4Money
    global Player1InJail
    global Player2InJail
    global Player3InJail
    global Player4InJail
    if landedOn == 1:
        print("Player " + str(WhosThis) + " landed on Go! (Press Enter)")#Landed on go
        input()
    elif landedOn == 2:#Landed on Mediterranean Ave.
            UseTheList(0, WhosThis)
    elif landedOn == 3: #Need to change later to add random chance in community chest
        if WhosThis == 1:
            Player1Money += 50
            print("Player 1 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
        elif WhosThis == 2:
            Player2Money += 50
            print("Player 2 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
        elif WhosThis == 3:
            Player3Money += 50
            print("Player 3 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
        else:
            Player4Money += 50
            print("Player 4 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
    elif landedOn == 4:#Baltic Ave.
           UseTheList(1, WhosThis)
    elif landedOn == 5:#Income Tax
        if WhosThis == 1:
            if (int)(Player1Money/10) < 200:
                print("Player 1 landed on the Income Tax\nPlayer 1 had to pay 10% of his value in tax which was " + str((int)(Player1Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player1Money/10)
                Player1Money -= (int)(Player1Money/10)
                GameOver()
                input()
            else:
                FreeParkingMoney += 200
                Player1Money -= 200
                print("Player 1 landed on the Income Tax\nPlayer 1 had to pay $200 in tax. (Press Enter)")
                GameOver()
                input()
        elif WhosThis == 2:
            if (int)(Player2Money/10) < 200:
                print("Player 2 landed on the Income Tax\nPlayer 2 had to pay 10% of his value in tax which was " + str((int)(Player2Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player2Money/10)
                Player2Money -= (int)(Player2Money/10)
                GameOver()
                input()
            else:
                FreeParkingMoney += 200
                Player2Money -= 200
                print("Player 2 landed on the Income Tax\nPlayer 2 had to pay $200 in tax. (Press Enter)")
                GameOver()
                input()
        elif WhosThis == 3:
            if (int)(Player3Money/10) < 200:
                print("Player 3 landed on the Income Tax\nPlayer 3 had to pay 10% of his value in tax which was " + str((int)(Player3Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player3Money/10)
                Player3Money -= (int)(Player3Money/10)
                GameOver()
                input()
            else:
                FreeParkingMoney += 200
                Player3Money -= 200
                print("Player 3 landed on the Income Tax\nPlayer 3 had to pay $200 in tax. (Press Enter)")
                GameOver()
                input()
        else:
            if (int)(Player4Money/10) < 200:
                print("Player 4 landed on the Income Tax\nPlayer 4 had to pay 10% of his value in tax which was " + str((int)(Player4Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player4Money/10)
                Player4Money -= (int)(Player4Money/10)
                GameOver()
                input()
            else:
                FreeParkingMoney += 200
                Player4Money -= 200
                print("Player 4 landed on the Income Tax\nPlayer 4 had to pay $200 in tax. (Press Enter)")
                GameOver()
                input()
    elif landedOn == 6:#Reading Railroad
            UseTheList(22, WhosThis)
    elif landedOn == 7:#Oriental Ave.
            UseTheList(2, WhosThis)
    elif landedOn == 8:
            if WhosThis == 1:
                    Player1Money += 50
                    print("Player 1 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 2:
                    Player2Money += 50
                    print("Player 2 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 3:
                    Player3Money += 50
                    print("Player 3 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            else:
                    Player4Money += 50
                    print("Player 4 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
    elif landedOn == 9:
            UseTheList(3, WhosThis)
    elif landedOn == 10:
            UseTheList(4, WhosThis)
    elif landedOn == 11:
            if WhosThis == 1:
                    if Player1InJail == 0:
                            print("Player 1 is just visiting jail. (Press Enter)")
                            input()
                    else:
                            print("Player 1 is currently in jail. (Press Enter)")
                            input()
            elif WhosThis == 2:
                    if Player2InJail == 0:
                            print("Player 2 is just visiting jail. (Press Enter)")
                            input()
                    else:
                            print("Player 2 is currently in jail. (Press Enter)")
                            input()
            elif WhosThis == 3:
                    if Player3InJail == 0:
                            print("Player 3 is just visiting jail. (Press Enter)")
                            input()
                    else:
                            print("Player 3 is currently in jail. (Press Enter)")
                            input()
            else:
                    if Player4InJail == 0:
                            print("Player 4 is just visiting jail. (Press Enter)")
                            input()
                    else:
                            print("Player 4 is currently in jail. (Press Enter)")
                            input()
    elif landedOn == 12:
            UseTheList(5, WhosThis)
    elif landedOn == 13:#26
            if list3[26] != 0:
                    if list3[26] == list3[27]:
                            list4[26] = random.randint(2, 12) * 10
                    else:
                            list4[26] = random.randint(2, 12) * 4
            if WhosThis == 1:
                    UseTheList(26, WhosThis)
            elif WhosThis == 2:
                    UseTheList(26, WhosThis)
            elif WhosThis == 3:
                    UseTheList(26, WhosThis)
            else:
                    UseTheList(26, WhosThis)
    elif landedOn == 14:
            UseTheList(6, WhosThis)
    elif landedOn == 15:
            UseTheList(7, WhosThis)
    elif landedOn == 16:
            UseTheList(23, WhosThis)
    elif landedOn == 17:
            UseTheList(8, WhosThis)            
    elif landedOn == 18:
            if WhosThis == 1:
                    Player1Money += 50
                    print("Player 1 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 2:
                    Player2Money += 50
                    print("Player 2 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 3:
                    Player3Money += 50
                    print("Player 3 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            else:
                    Player4Money += 50
                    print("Player 4 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
    elif landedOn == 19:
            UseTheList(9, WhosThis)
    elif landedOn == 20:
            UseTheList(10, WhosThis)
    elif landedOn == 21:
            if WhosThis == 1:
                    Player1Money += FreeParkingMoney
                    print("Player 1 landed on Free Parking\nPlayer 1 has gained $" + str(FreeParkingMoney) + "!")
                    FreeParkingMoney = 0
                    input()
            elif WhosThis == 2:
                    Player2Money += FreeParkingMoney
                    print("Player 2 landed on Free Parking\nPlayer 2 has gained $" + str(FreeParkingMoney) + "!")
                    FreeParkingMoney = 0
                    input()
            elif WhosThis == 3:
                    Player3Money += FreeParkingMoney
                    print("Player 3 landed on Free Parking\nPlayer 3 has gained $" + str(FreeParkingMoney) + "!")
                    FreeParkingMoney = 0
                    input()
            else:
                    Player4Money += FreeParkingMoney
                    print("Player 4 landed on Free Parking\nPlayer 4 has gained $" + str(FreeParkingMoney) + "!")
                    FreeParkingMoney = 0
                    input()            
    elif landedOn == 22:
            UseTheList(11, WhosThis) 
    elif landedOn == 23:
            if WhosThis == 1:
                    Player1Money += 50
                    print("Player 1 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 2:
                    Player2Money += 50
                    print("Player 2 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 3:
                    Player3Money += 50
                    print("Player 3 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            else:
                    Player4Money += 50
                    print("Player 4 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
    elif landedOn == 24:
            UseTheList(12, WhosThis)
    elif landedOn == 25:
            UseTheList(13, WhosThis)
    elif landedOn == 26:
            UseTheList(24, WhosThis)
    elif landedOn == 27:
            UseTheList(14, WhosThis)
    elif landedOn == 28:
            UseTheList(15, WhosThis)
    elif landedOn == 29:#27
            if list3[27] != 0:
                    if list3[26] == list3[27]:
                            list4[27] = random.randint(2, 12) * 10
                    else:
                            list4[27] = random.randint(2, 12) * 4
            if WhosThis == 1:
                    #print("Player 1 has landed on the Water Works. (Press Enter)")
                    UseTheList(27, WhosThis)
                    #input()
            elif WhosThis == 2:
                    #print("Player 2 has landed on the Water Works. (Press Enter)")
                    UseTheList(27, WhosThis)
                    #input()
            elif WhosThis == 3:
                    #print("Player 3 has landed on the Water Works. (Press Enter)")
                    UseTheList(27, WhosThis)
                    #input()
            else:
                    #print("Player 4 has landed on the Water Works. (Press Enter)")
                    UseTheList(27, WhosThis)
                    #input()
    elif landedOn == 30:
            UseTheList(16, WhosThis)
    elif landedOn == 31:
            global Player1Location
            global Player2Location
            global Player3Location
            global Player4Location
            if WhosThis == 1:
                    print("Player 1 has to go to Jail. (Press Enter)")
                    input()
                    #global Player1InJail
                    Player1InJail = 1
                    Player1Location = 11
            elif WhosThis == 2:
                    print("Player 2 has to go to Jail. (Press Enter)")
                    input()
                    #global Player2InJail
                    Player2InJail = 1
                    Player2Location = 11
            elif WhosThis == 3:
                    print("Player 3 has to go to Jail. (Press Enter)")
                    input()
                    #global Player3InJail
                    Player3InJail = 1
                    Player3Location = 11
            else:
                    print("Player 4 has to go to Jail. (Press Enter)")
                    input()
                    #global Player4InJail
                    Player4InJail = 1
                    Player4Location = 11
    elif landedOn == 32:
            UseTheList(17, WhosThis)
    elif landedOn == 33:
            UseTheList(18, WhosThis)
    elif landedOn == 34:
            if WhosThis == 1:
                    Player1Money += 50
                    print("Player 1 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 2:
                    Player2Money += 50
                    print("Player 2 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 3:
                    Player3Money += 50
                    print("Player 3 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            else:
                    Player4Money += 50
                    print("Player 4 landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
    elif landedOn == 35:
            UseTheList(19, WhosThis)
    elif landedOn == 36:
            UseTheList(25, WhosThis)            
    elif landedOn == 37:
            if WhosThis == 1:
                    Player1Money += 50
                    print("Player 1 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 2:
                    Player2Money += 50
                    print("Player 2 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            elif WhosThis == 3:
                    Player3Money += 50
                    print("Player 3 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
            else:
                    Player4Money += 50
                    print("Player 4 landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
                    input()
    elif landedOn == 38:
            UseTheList(20, WhosThis)    
    elif landedOn == 39:
            if WhosThis == 1:
                    Player1Money -= 75
                    FreeParkingMoney += 75
                    print("Player 1 landed on Luxury Tax\nThey have to pay $75. (Press Enter)")
                    input()
                    GameOver()
            elif WhosThis == 2:
                    Player2Money -= 75
                    FreeParkingMoney += 75
                    print("Player 1 landed on Luxury Tax\nThey have to pay $75. (Press Enter)")
                    input()
                    GameOver()
            elif WhosThis == 3:
                    Player3Money -= 75
                    FreeParkingMoney += 75
                    print("Player 1 landed on Luxury Tax\nThey have to pay $75. (Press Enter)")
                    input()
                    GameOver()
            else:
                    Player4Money -= 75
                    FreeParkingMoney += 75
                    print("Player 1 landed on Luxury Tax\nThey have to pay $75. (Press Enter)")
                    input()
                    GameOver()            
    else:#40 / Boardwalk
            UseTheList(21, WhosThis)
    MONOPOLY()

def TradingWithPeople(StarterOfTrade, WhoTheyWantToTrade):
        print("What do you want to trade?\nMoney?\nBuildings\nFinish\nExit?")
        GiveMoney1 = 0
        GiveMoney2 = 0
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        for x in range(0, 28):
                list5[x] = 0
        playerOfTrade = 0
        while True:
                WhatTheyChoose = input().lower()
                if WhatTheyChoose.lower() == "money" or WhatTheyChoose.lower() == "mone" or WhatTheyChoose.lower() == "mon" or WhatTheyChoose.lower() == "mo" or WhatTheyChoose.lower() == "m":
                        if playerOfTrade == 0:
                                print("How much do you want to give? (It will ask how much you want the other player to give next)")
                        else:
                                print("How much do you want the other player to give you?")
                        while True:
                                GiveMoney1 = input()
                                try:
                                        int(GiveMoney1)
                                        if int(GiveMoney1) >= 0:
                                                break
                                        else:
                                                print("You can't do negitives. Type 0 if you don't want to give any money.")
                                except Exception:
                                        print("That isn't a int.")
                        if playerOfTrade == 0:                                              
                                print("How much do you want the other player to give?")
                        else:
                                print("How much are you willing to give?")
                        while True:
                                GiveMoney2 = input()
                                try:
                                        int(GiveMoney2)
                                        if int(GiveMoney2) >= 0:
                                                break
                                        else:
                                                print("You can't do negitives. Type 0 if you don't want to give any money.")
                                except Exception:
                                        print("That isn't a int.")
                        print("Now, do you want to trade buildings or finish the deal?")

                                        
                elif WhatTheyChoose.lower() == "buildings" or WhatTheyChoose.lower() == "building" or WhatTheyChoose.lower() == "buildin" or WhatTheyChoose.lower() == "buildi" or WhatTheyChoose.lower() == "build" or WhatTheyChoose.lower() == "buil" or WhatTheyChoose.lower() == "bui" or WhatTheyChoose.lower() == "bu" or WhatTheyChoose.lower() == "b":
                        print("")
                        #list5[0] = 0
                        print("Player " + str(StarterOfTrade) +" can trade...")
                        for x in range(0, 28):
                                 if list3[x] == StarterOfTrade:
                                         print(list1[x])
                                         
                        print("And player " + str(WhoTheyWantToTrade) + " can trade...")
                        for x in range(0, 28):
                                 if list3[x] == WhoTheyWantToTrade:
                                         print(list1[x])
                        print("(Type finish when you're done. If you type the same place again, it will trade back the places to the original owner.)")                 
                        while True:
                                #list1 = ["Mediterranean Ave.", "Baltic Ave.", "Oriental Ave.", "Vermont Ave.", "Connecticut Ave.", "St. Charles Place", "States Ave.", "Virginia Ave.","St. James Place", "Tennessee Ave.", "New York Ave.", "Kentucky Ave.","Indiana Ave.","Illinois Ave.","Atlantic Ave.","Ventnor Ave.", "Marvin Gardens", "Pacific Ave.", "North Carolina Ave.", "Pennsylvania Ave.","Park Place", "Boardwalk", "Reading Railroad", "Pennsylvania Railroad","B. & O. Railroad","Short Line Railroad"]
                                TradingABuilding = input().lower()
                                for x in range(0, 28):
                                        if TradingABuilding == list1[x].lower():
                                                if list5[x] == WhoTheyWantToTrade or list5[x] == StarterOfTrade:
                                                        list5[x] = 0
                                                        print("The trade was canceled.")
                                                elif list3[x] == WhoTheyWantToTrade:
                                                        list5[x] = StarterOfTrade
                                                        print("The trade was succesful.")
                                                elif list3[x] == StarterOfTrade:
                                                        list5[x] = WhoTheyWantToTrade
                                                        print("The trade was succesful.")
                                                else:
                                                        print("Neither players own " + list1[x])
                                if TradingABuilding == "finish" or TradingABuilding == "exit":
                                        break
                                print("Anything else? (Type finish or exit to stop trading building.)")
                        print("Now, will you like to trade money or finish?")
                                
                elif WhatTheyChoose.lower() == "finish" or WhatTheyChoose.lower() == "finis" or WhatTheyChoose.lower() == "fini" or WhatTheyChoose.lower() == "fin" or WhatTheyChoose.lower() == "fin" or WhatTheyChoose.lower() == "fi" or WhatTheyChoose.lower() == "f":
                        if playerOfTrade == 0:
                                print("Player " + str(StarterOfTrade) + " is willing to give player "+str(WhoTheyWantToTrade) +" $"+ str(GiveMoney1) + " and")
                                for x in range(0, 28):
                                        if list5[x] == WhoTheyWantToTrade:
                                                print(list1[x] + ", ")   
                                print("for...")
                                print(str(GiveMoney2) + " of player " + str(WhoTheyWantToTrade)+"'s gold and ")
                                for x in range(0, 28):
                                        if list5[x] == StarterOfTrade:
                                                print(list1[x]+", ")
                                                
                                print("Does player " + str(WhoTheyWantToTrade) + " agree to this? (yes or no)")
                        else:
                                print("Player " + str(WhoTheyWantToTrade) + " wants player "+str(StarterOfTrade) +" to instead give them $"+ str(GiveMoney1) + " and ")
                                for x in range(0, 28):
                                        if list5[x] == WhoTheyWantToTrade:
                                                print(list1[x] + ", ")
                                print("for...")
                                print("Player " + str(WhoTheyWantToTrade) +"'s $"+ str(GiveMoney2) + " and ")
                                for x in range(0, 28):
                                        if list5[x] == StarterOfTrade:
                                                print(list1[x]+", ")
                                print("Does player " + str(StarterOfTrade) + " agree to this? (yes or no)")
                        exitTradeLoop = 0
                        while True:       
                                AnswerToTrade = input().lower()
                                if AnswerToTrade.lower() == "yes" or AnswerToTrade.lower() == "y" or AnswerToTrade.lower() == "ye":
                                        if StarterOfTrade == 1:
                                                GiveMoney1 = int(GiveMoney1)
                                                GiveMoney2 = int(GiveMoney2)
                                                if WhoTheyWantToTrade == 2:
                                                        Player1Money -= GiveMoney1
                                                        Player1Money += GiveMoney2
                                                        Player2Money -= GiveMoney2
                                                        Player2Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                elif WhoTheyWantToTrade == 3:
                                                        Player1Money -= GiveMoney1
                                                        Player1Money += GiveMoney2
                                                        Player3Money -= GiveMoney2
                                                        Player3Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                else:
                                                        Player1Money -= GiveMoney1
                                                        Player1Money += GiveMoney2
                                                        Player4Money -= GiveMoney2
                                                        Player4Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                        elif StarterOfTrade == 2:
                                                if WhoTheyWantToTrade == 1:
                                                        Player2Money -= GiveMoney1
                                                        Player2Money += GiveMoney2
                                                        Player1Money -= GiveMoney2
                                                        Player1Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                elif WhoTheyWantToTrade == 3:
                                                        Player2Money -= GiveMoney1
                                                        Player2Money += GiveMoney2
                                                        Player3Money -= GiveMoney2
                                                        Player3Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                else:
                                                        Player2Money -= GiveMoney1
                                                        Player2Money += GiveMoney2
                                                        Player4Money -= GiveMoney2
                                                        Player4Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                        elif StarterOfTrade == 3:
                                                if WhoTheyWantToTrade == 1:
                                                        Player3Money -= GiveMoney1
                                                        Player3Money += GiveMoney2
                                                        Player1Money -= GiveMoney2
                                                        Player1Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                elif WhoTheyWantToTrade == 2:
                                                        Player3Money -= GiveMoney1
                                                        Player3Money += GiveMoney2
                                                        Player2Money -= GiveMoney2
                                                        Player2Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                else:
                                                        Player3Money -= GiveMoney1
                                                        Player3Money += GiveMoney2
                                                        Player4Money -= GiveMoney2
                                                        Player4Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                        else:
                                                if WhoTheyWantToTrade == 1:
                                                        Player4Money -= GiveMoney1
                                                        Player4Money += GiveMoney2
                                                        Player1Money -= GiveMoney2
                                                        Player1Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                elif WhoTheyWantToTrade == 2:
                                                        Player4Money -= GiveMoney1
                                                        Player4Money += GiveMoney2
                                                        Player2Money -= GiveMoney2
                                                        Player2Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                                else:
                                                        Player4Money -= GiveMoney1
                                                        Player4Money += GiveMoney2
                                                        Player3Money -= GiveMoney2
                                                        Player3Money += GiveMoney1
                                                        for x in range(0, 28):
                                                                if list5[x] == StarterOfTrade:
                                                                        list3[x] = StarterOfTrade
                                                                if list5[x] == WhoTheyWantToTrade:
                                                                        list3[x] = WhoTheyWantToTrade
                                                        print("The deal was succesful. (Please press enter to continue.)")
                                                        exitTradeLoop = 1
                                                        input()
                                        MONOPOLY()
                                        break
                                elif AnswerToTrade.lower() == "no" or AnswerToTrade.lower() == "n":
                                        print("Would you like to make 'changes' to the trade or just flat out 'cancel' the trade?")
                                        while True:
                                                AnswerToChange = input().lower()
                                                if AnswerToChange.lower() == "changes" or AnswerToChange.lower() == "change":
                                                        if playerOfTrade == 0:
                                                                playerOfTrade = 1
                                                        else:
                                                                playerOfTrade = 0
                                                        print("What would you like to change?\nMoney?\nBuildings?\nFinish?\nExit?")
                                                                
                                                        break
                                                elif AnswerToChange.lower() == "cancel":
                                                        exitTradeLoop = 1
                                                        break
                                                else:
                                                        print("I'm sorry, please type in change or cancel to move on.")
                                        break
                                else:
                                        print("I don't understand what you mean. Do you or do you not want to make the trade? (Yes/No).")
                        if exitTradeLoop == 1:
                                break
                elif WhatTheyChoose.lower() == "exit" or WhatTheyChoose.lower() == "exi" or WhatTheyChoose.lower() == "ex" or WhatTheyChoose.lower() == "e":
                        break
                else:
                        print("I don't understand? Do you want to trade money, buildings, finish the trade, or exit?")

GreenHouses = 32
RedHotels = 12
#                          0  2  4  5  7  9  0  2  4  5  7  8  0  2  3  5  8  0
#              2  4  7  9  1  1  1  1  1  1  2  2  2  2  2  2  3  3  3  3  3  4
HousesArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def PromotingBuildings(PlayerWhosPromoting):
        global list3
        global list4
        global HousesArray
        global GreenHouses
        global RedHotels
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        print("You can currently put green and red houses on...")
        if list3[0] == list3[1] == PlayerWhosPromoting:
                print("Mediterranean Ave. and Baltic Ave.")
        if list3[2] == list3[3] == list3[4] == PlayerWhosPromoting:
                print("Oriental Ave., Vermont Ave., and Connecticut Ave.")
        if list3[5] == list3[6] == list3[7] == PlayerWhosPromoting:
                print("St. Charles Place, States Ave., and Virginia Ave.")
        if list3[8] == list3[9] == list3[10] == PlayerWhosPromoting:
                print("St. James Place, Tennessee Ave., and New York Ave.")
        if list3[11] == list3[12] == list3[13] == PlayerWhosPromoting:
                print("Kentucky Ave., Indiana Ave., and Illinois Ave.")
        if list3[14] == list3[15] == list3[16] == PlayerWhosPromoting:
                print("Atlantic Ave., Ventnor Ave., and Marvin Gardens.")
        if list3[17] == list3[18] == list3[19] == PlayerWhosPromoting:
                print("Pacific Ave., North Carolina Ave., and Pennsylvania Ave.")
        if list3[20] == list3[21] == PlayerWhosPromoting:
                print("Park Place and Boardwalk.")
        print("Exit.")
        while True:
                WhatTheyWantToPromote = input()
                Cost = [50, 100, 150, 200]
                if list3[0] == list3[1] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[0] or list3[0] == list3[1] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[1] :
                        if WhatTheyWantToPromote == list1[0]:
                                print("Do you really want to put a house on " + list1[0]+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 0)
                        if WhatTheyWantToPromote == list1[1]:
                                print("Do you really want to put a house on " + list1[1]+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 1)
                        #print("Mediterranean Ave. and Baltic Ave.")
                elif list3[2] == list3[3] == list3[4] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[2] or list3[2] == list3[3] == list3[4] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[3] or list3[2] == list3[3] == list3[4] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[4]:
                        if WhatTheyWantToPromote == list1[2]:
                                print("Do you really want to put a house on " + list1[2]+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 2)
                        if WhatTheyWantToPromote == list1[3]:
                                print("Do you really want to put a house on " + list1[3]+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 3)
                        if WhatTheyWantToPromote == list1[4]:
                                print("Do you really want to put a house on " + list1[4]+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 4)
                        #print("Oriental Ave., Vermont Ave., and Connecticut Ave.")
                elif list3[5] == list3[6] == list3[7] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[5] or list3[5] == list3[6] == list3[7] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[6] or list3[5] == list3[6] == list3[7] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[7]:
                        if WhatTheyWantToPromote == list1[5]:
                                print("Do you really want to put a house on " + list1[5]+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 5)
                        if WhatTheyWantToPromote == list1[6]:
                                print("Do you really want to put a house on " + list1[6]+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 6)
                        if WhatTheyWantToPromote == list1[7]:
                                print("Do you really want to put a house on " + list1[7]+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 7)
                        #print("St. Charles Place, States Ave., and Virginia Ave.")
                elif list3[8] == list3[9] == list3[10] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[8] or list3[8] == list3[9] == list3[10] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[9] or list3[8] == list3[9] == list3[10] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[10]:
                        if WhatTheyWantToPromote == list1[8]:
                                print("Do you really want to put a house on " + list1[8]+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 8)
                        if WhatTheyWantToPromote == list1[9]:
                                print("Do you really want to put a house on " + list1[9]+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 9)
                        if WhatTheyWantToPromote == list1[10]:
                                print("Do you really want to put a house on " + list1[10]+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 10)
                        #print("St. James Place, Tennessee Ave., and New York Ave.")
                elif list3[11] == list3[12] == list3[13] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[11] or list3[11] == list3[12] == list3[13] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[12] or list3[11] == list3[12] == list3[13] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[13]:
                        if WhatTheyWantToPromote == list1[11]:
                                print("Do you really want to put a house on " + list1[11]+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 11)
                        if WhatTheyWantToPromote == list1[12]:
                                print("Do you really want to put a house on " + list1[12]+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 12)
                        if WhatTheyWantToPromote == list1[13]:
                                print("Do you really want to put a house on " + list1[13]+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 13)
                        #print("Kentucky Ave., Indiana Ave., and Illinois Ave.")
                elif list3[14] == list3[15] == list3[16] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[14] or list3[14] == list3[15] == list3[16] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[15] or list3[14] == list3[15] == list3[16] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[16]:
                        if WhatTheyWantToPromote == list1[14]:
                                print("Do you really want to put a house on " + list1[14]+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 14)
                        if WhatTheyWantToPromote == list1[15]:
                                print("Do you really want to put a house on " + list1[15]+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 15)
                        if WhatTheyWantToPromote == list1[16]:
                                print("Do you really want to put a house on " + list1[16]+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 16)
                        #print("Atlantic Ave., Ventnor Ave., and Marvin Gardens.")
                elif list3[17] == list3[18] == list3[19] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[17] or list3[17] == list3[18] == list3[19] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[18] or list3[17] == list3[18] == list3[19] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[19]:
                        if WhatTheyWantToPromote == list1[17]:
                                print("Do you really want to put a house on " + list1[17]+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 17)
                        if WhatTheyWantToPromote == list1[18]:
                                print("Do you really want to put a house on " + list1[18]+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 18)
                        if WhatTheyWantToPromote == list1[19]:
                                print("Do you really want to put a house on " + list1[19]+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 19)
                        #print("Pacific Ave., North Carolina Ave., and Pennsylvania Ave.")
                elif list3[20] == list3[21] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[20] or list3[20] == list3[21] == PlayerWhosPromoting and WhatTheyWantToPromote == list1[21]:
                        if WhatTheyWantToPromote == list1[20]:
                                print("Do you really want to put a house on " + list1[20]+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 20)
                        if WhatTheyWantToPromote == list1[21]:
                                print("Do you really want to put a house on " + list1[21]+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 21)
                        #print("Park Place and Boardwalk.")
                elif WhatTheyWantToPromote.lower() == "exit" or WhatTheyWantToPromote.lower() == "exi" or WhatTheyWantToPromote.lower() == "ex" or WhatTheyWantToPromote.lower() == "e":
                        break
                else:
                        print("You either don't own that place, have a monopoly in that area, or you spelled it wrong.")
        print()



def HouseUpgrading(Player, CostOfHouse, Place):
        global list3
        global list4
        global HousesArray
        global GreenHouses
        global RedHotels
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        #print(".")
        YesNo = ""
        while True:
                YesNo = input()
                if YesNo.lower() == "yes" or YesNo.lower() == "no":
                        break
        if YesNo.lower() == "yes":
                if Player == 1:
                        if Player1Money >= CostOfHouse:
                                if GreenHouses > 0 and HousesArray[Place] < 4 or RedHotels > 0 and HousesArray[Place] == 4:
                                        Player1Money -= CostOfHouse
                                        HousesArray[Place] += 1
                                        print("It was succesful.")
                                else:
                                        print("There isn't enough houses left for that.")
                        else:
                                print("Player one doesn't have enough money to put a house on his place")
                elif Player == 2:
                        if Player2Money >= CostOfHouse:
                                if GreenHouses > 0 and HousesArray[Place] < 4 or RedHotels > 0 and HousesArray[Place] == 4:
                                        Player2Money -= CostOfHouse
                                        HousesArray[Place] += 1
                                        print("It was succesful.")
                                else:
                                        print("There isn't enough houses left for that.")
                        else:
                                print("Player two doesn't have enough money to put a house on his place")
                elif Player == 3:
                        if Player3Money >= CostOfHouse:
                                if GreenHouses > 0 and HousesArray[Place] < 4 or RedHotels > 0 and HousesArray[Place] == 4:
                                        Player3Money -= CostOfHouse
                                        HousesArray[Place] += 1
                                        print("It was succesful.")
                                else:
                                        print("There isn't enough houses left for that.")
                        else:
                                print("Player three doesn't have enough money to put a house on his place")
                else:
                        if Player4Money >= CostOfHouse:
                                if GreenHouses > 0 and HousesArray[Place] < 4 or RedHotels > 0 and HousesArray[Place] == 4:
                                        Player4Money -= CostOfHouse
                                        HousesArray[Place] += 1
                                        print("It was succesful.")
                                else:
                                        print("There isn't enough houses left for that.")
                        else:
                                print("Player four doesn't have enough money to put a house on his place")

        print("So, do you want to put houses on anything else? If not, you can just type exit to leave.")
                
#                      0  1  2  3  4  5  6  7
#                      D  L     O     Y
#                               r     e  G
#                      B  B  P  a     l  r  B
#                      l  l  i  n  R  l  e  l
#                      u  u  n  g  e  o  e  u
#                      e  e  k  e  d  w  n  e
AlreadyWasAMonopoly = [0, 0, 0, 0, 0, 0, 0, 0]
def MONOPOLY():
        global list3
        global list4
        if AlreadyWasAMonopoly[0] == 0 and list3[0] == list3[1] != 0:
                list4[0] *= 2
                list4[0] = (int)(list4[0])
                list4[1] *= 2
                list4[1] = (int)(list4[1])
                AlreadyWasAMonopoly[0] = 1
        if AlreadyWasAMonopoly[0] == 1 and list3[0] != list3[1] != 0:
                list4[0] /= 2
                list4[0] = (int)(list4[0])
                list4[1] /= 2
                list4[1] = (int)(list4[1])
                AlreadyWasAMonopoly[0] = 0
        if AlreadyWasAMonopoly[1] == 0 and list3[2] == list3[3] == list3[4] != 0:
                list4[2] *= 2
                list4[2] = (int)(list4[2])
                list4[3] *= 2
                list4[3] = (int)(list4[3])
                list4[4] *= 2
                list4[4] = (int)(list4[4])
                AlreadyWasAMonopoly[1] = 1
        if AlreadyWasAMonopoly[1] == 1 and list3[2] != list3[3] != list3[4] != 0:
                list4[2] /= 2
                list4[2] = (int)(list4[2])
                list4[3] /= 2
                list4[3] = (int)(list4[3])
                list4[4] /= 2
                list4[4] = (int)(list4[4])
                AlreadyWasAMonopoly[1] = 0
        if AlreadyWasAMonopoly[2] == 0 and list3[5] == list3[6] == list3[7] != 0:
                list4[5] *= 2
                list4[5] = (int)(list4[5])
                list4[6] *= 2
                list4[6] = (int)(list4[6])
                list4[7] *= 2
                list4[7] = (int)(list4[7])
                AlreadyWasAMonopoly[2] = 1
        if AlreadyWasAMonopoly[2] == 1 and list3[5] != list3[6] != list3[7] != 0:
                list4[5] /= 2
                list4[5] = (int)(list4[5])
                list4[6] /= 2
                list4[6] = (int)(list4[6])
                list4[7] /= 2
                list4[7] = (int)(list4[7])
                AlreadyWasAMonopoly[2] = 0
        if AlreadyWasAMonopoly[3] == 0 and list3[8] == list3[9] == list3[10] != 0:
                list4[8] *= 2
                list4[8] = (int)(list4[8])
                list4[9] *= 2
                list4[9] = (int)(list4[9])
                list4[10] *= 2
                list4[10] = (int)(list4[10])
                AlreadyWasAMonopoly[3] = 1
        if AlreadyWasAMonopoly[3] == 1 and list3[8] != list3[9] != list3[10] != 0:
                list4[8] /= 2
                list4[8] = (int)(list4[8])
                list4[9] /= 2
                list4[9] = (int)(list4[9])
                list4[10] /= 2
                list4[10] = (int)(list4[10])
                AlreadyWasAMonopoly[3] = 0
        if AlreadyWasAMonopoly[4] == 0 and list3[11] == list3[12] == list3[13] != 0:
                list4[11] *= 2
                list4[11] = (int)(list4[11])
                list4[12] *= 2
                list4[12] = (int)(list4[12])
                list4[13] *= 2
                list4[13] = (int)(list4[13])
                AlreadyWasAMonopoly[4] = 1
        if AlreadyWasAMonopoly[4] == 1 and list3[11] != list3[12] != list3[13] != 0:
                list4[11] /= 2
                list4[11] = (int)(list4[11])
                list4[12] /= 2
                list4[12] = (int)(list4[12])
                list4[13] /= 2
                list4[13] = (int)(list4[13])
                AlreadyWasAMonopoly[4] = 0
        if AlreadyWasAMonopoly[5] == 0 and list3[14] == list3[15] == list3[16] != 0:
                list4[14] *= 2
                list4[14] = (int)(list4[14])
                list4[15] *= 2
                list4[15] = (int)(list4[15])
                list4[16] *= 2
                list4[16] = (int)(list4[16])
                AlreadyWasAMonopoly[5] = 1
        if AlreadyWasAMonopoly[5] == 1 and list3[14] != list3[15] != list3[16] != 0:
                list4[14] /= 2
                list4[14] = (int)(list4[14])
                list4[15] /= 2
                list4[15] = (int)(list4[15])
                list4[16] /= 2
                list4[16] = (int)(list4[16])
                AlreadyWasAMonopoly[5] = 0
        if AlreadyWasAMonopoly[6] == 0 and list3[17] == list3[18] == list3[19] != 0:
                list4[17] *= 2
                list4[17] = (int)(list4[17])
                list4[18] *= 2
                list4[18] = (int)(list4[18])
                list4[19] *= 2
                list4[19] = (int)(list4[19])
                AlreadyWasAMonopoly[6] = 1
        if AlreadyWasAMonopoly[6] == 1 and list3[17] != list3[18] != list3[19] != 0:
                list4[17] /= 2
                list4[17] = (int)(list4[17])
                list4[18] /= 2
                list4[18] = (int)(list4[18])
                list4[19] /= 2
                list4[19] = (int)(list4[19])
                AlreadyWasAMonopoly[6] = 0
        if AlreadyWasAMonopoly[7] == 0 and list3[20] == list3[21] != 0:
                list4[20] *= 2
                list4[20] = (int)(list4[20])
                list4[21] *= 2
                list4[21] = (int)(list4[21])
                AlreadyWasAMonopoly[7] = 1
        if AlreadyWasAMonopoly[7] == 1 and list3[20] != list3[21] != 0:
                list4[20] /= 2
                list4[20] = (int)(list4[20])
                list4[21] /= 2
                list4[21] = (int)(list4[21])
                AlreadyWasAMonopoly[7] = 0
        print()

def ChanceTime(PlayerEffected):
        DaNumberYouGot = random.randint(1, 1)
        print()

def CommunityChest(PlayerEffected):
        DaNumberYouGot = random.randint(1, 1)
        print()
      
def debugMode(PlayerDebug): #heyguysimdefinitelynotcheatingandijustlikelytypingveryuselesslongwordsallwithoutausinganyspaces
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        global list1
        global list2
        global list3
        global list4
        global list5
        global GreenHouses
        global RedHotels
        global Player1InJail
        global Player2InJail
        global Player3InJail
        global Player4InJail
        global Player1Location
        global Player2Location
        global Player3Location
        global Player4Location
        print("Welcome to the place to change Ints/Strings, test different defs, and random funny things. (In no predictular order)\n(Also with no fail safes, so if you puta String for an int... You can get an error if the int isn't change before it is called to be use)")
        print("1 - Player in debug mode gets all buildings\n2 - Player in debug money == -69\n3 - Community Chest\n4 - Chance Time\n5 - Everything is free!!!\n6 - Make houses amount the same amount\n7 - Change list 1\n8 - Change list 2\n9 - Change list 3\n10 - Change list 4\n11 - Change list 5\n12 - Change Everyone Money Amount")
        print("13 - Choice who is in jail\n14 - Move somewhere and activate its effect\n15 - Just move everyone somewhere\n16 - Test GameOver()\n17 - Test MONOPOLY()\n18 - Test DiceRoll()\n19 - Retest HowManyPlayers()\n20 - Test UseTheList()\n21 - Test dice picture\n22 - Change free parking amount")
        print("23 - Change all useless rent ints\n24 - Change all useless house own int\n25 - Give everyone random buildings")
        s = "" + input()
        if s == "1":
                for x in range(0, 28):
                        list3[x] = PlayerDebug
        elif s == "2":
                if PlayerDebug == 1:
                        Player1Money = -69
                if PlayerDebug == 2:
                        Player2Money = -69
                if PlayerDebug == 3:
                        Player3Money = -69
                if PlayerDebug == 4:
                        Player4Money = -69
        elif s == "3":
                CommunityChest(PlayerDebug)
        elif s == "4":
                ChanceTime(PlayerDebug)
        elif s == "5":
                for x in range(0, 28):
                        list2[x] = 0
        elif s == "6":
                GreenHouses = input()
                RedHotels = input()
        elif s == "7":
                for x in range(0, 28):
                        list1[x] = ""+input()
        elif s == "8":
                for x in range(0, 28):
                        list2[x] = ""+input()
        elif s == "9":
                for x in range(0, 28):
                        list3[x] = ""+input()
        elif s == "10":
                for x in range(0, 28):
                        list4[x] = ""+input()
        elif s == "11":
                for x in range(0, 28):
                        list5[x] = ""+input()
        elif s == "12":
                Player1Money = input()
                Player2Money = input()
                Player3Money = input()
                Player4Money = input()
        elif s == "13":
                Player1InJail = input()
                Player1InJail = input()
                Player1InJail = input()
                Player1InJail = input()
        elif s == "14":
                PlayToGo = input()
                LandedPlaces(PlayToGo, PlayerDebug)
        elif s == "15":
                Player1Location = input()
                Player2Location = input()
                if Player3Location != 99999:
                        Player3Location = input()
                if Player4Location != 99999:
                        Player4Location = input()
        elif s == "16":
                GameOver()
        elif s == "17":
                MONOPOLY()
        elif s == "18":
                DiceRoll(PlayerDebug)
        elif s == "19":
                HowManyPlayers()
        elif s == "20":
                PlayToGo = input()
                UseTheList(PlayToGo, PlayerDebug)
        elif s == "21":
                Picture = input()
                print(DicePictures[Picture])
        elif s == "22":
                global FreeParkingMoney
                FreeParkingMoney = input()
        elif s == "23":
                global MediterraneanAveRent
                global BalticAveRent
                global ReadingRailroadRent
                global OrientalAveRent
                global VermontAveRent
                global ConnecticutAveRent
                global StCharlesPlaceRent
                global ElectricCompanyRent
                global StatesAveRent
                global VirginiaAveRent
                global PennsylvaniaRailroadRent
                global StJamesPlaceRent
                global TennesseeAveRent
                global NewYorkAveRent
                global KentuckyAveRent
                global IndianaAveRent
                global IllinoisAveRent
                global BORailroadRent
                global AtlanticAveRent
                global VentnorAveRent
                global WaterWorksRent
                global MarvinGardensRent
                global PacificAveRent
                global NorthCarolinaAveRent
                global PennsylvaniaAveRent
                global ShortLineRailroadRent
                global ParkPlaceRent
                global BoardwalkRent
                
                MediterraneanAveRent = input()
                BalticAveRent = input()
                ReadingRailroadRent = input()
                OrientalAveRent = input()
                VermontAveRent = input()
                ConnecticutAveRent = input()
                StCharlesPlaceRent = input()
                ElectricCompanyRent = input()
                StatesAveRent = input()
                VirginiaAveRent = input()
                PennsylvaniaRailroadRent = input()
                StJamesPlaceRent = input()
                TennesseeAveRent = input()
                NewYorkAveRent = input()
                KentuckyAveRent = input()
                IndianaAveRent = input()
                IllinoisAveRent = input()
                BORailroadRent = input()
                AtlanticAveRent = input()
                VentnorAveRent = input()
                WaterWorksRent = input()
                MarvinGardensRent = input()
                PacificAveRent = input()
                NorthCarolinaAveRent = input()
                PennsylvaniaAveRent = input()
                ShortLineRailroadRent = input()
                ParkPlaceRent = input()
                BoardwalkRent = input()
        elif s == "24":
                global MediterraneanAve
                global BalticAve
                global ReadingRailroad
                global OrientalAve
                global VermontAve
                global ConnecticutAve
                global StCharlesPlace
                global ElectricCompany
                global StatesAve
                global VirginiaAve
                global PennsylvaniaRailroad
                global StJamesPlace
                global TennesseeAve
                global NewYorkAve
                global KentuckyAve
                global IndianaAve
                global IllinoisAve
                global BORailroad
                global AtlanticAve
                global VentnorAve
                global WaterWorks
                global MarvinGardens
                global PacificAve
                global NorthCarolinaAve
                global PennsylvaniaAve
                global ShortLineRailroad
                global ParkPlace
                global Boardwalk
                
                MediterraneanAve = input()
                BalticAve = input()
                ReadingRailroad = input()
                OrientalAve = input()
                VermontAve = input()
                ConnecticutAve = input()
                StCharlesPlace = input()
                ElectricCompany = input()
                StatesAve = input()
                VirginiaAve = input()
                PennsylvaniaRailroad = input()
                StJamesPlace = input()
                TennesseeAve = input()
                NewYorkAve = input()
                FreeParkingMoney = input()
                KentuckyAve = input()
                IndianaAve = input()
                IllinoisAve = input()
                BORailroad = input()
                AtlanticAve = input()
                VentnorAve = input()
                WaterWorks = input()
                MarvinGardens = input()
                PacificAve = input()
                NorthCarolinaAve = input()
                PennsylvaniaAve = input()
                ShortLineRailroad = input()
                ParkPlace = input()
                Boardwalk = input()
        elif s == "25":
                if Player3Location == 99999:
                        for x in range(0, 28):
                                list3[x] = random.randint(1, 2)
                elif Player4Location == 99999:
                        for x in range(0, 28):
                                list3[x] = random.randint(1, 3)
                else:
                        for x in range(0, 28):
                                list3[x] = random.randint(1, 4)

SellingValue = [30, 30, 50, 50, 60, 70, 70, 80, 90, 90, 100, 110, 110, 120, 130, 130, 140, 150, 150, 160, 175, 200, 100, 100, 100, 100, 75, 75]
WhatYouThinkingOfSelling = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
WhatHousesAreCurrentlyBeenSell = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def HouseForSells(PlayerWhosSelling):
        print("You own...")
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        global list3
        global list1
        YESNO = ""
        for x in range(0, 28):
                WhatYouThinkingOfSelling[x] = 0
                if list3[x] == PlayerWhosSelling:
                        print(str(x) +" - "+list1[x])
        print("What place do you want to sell?\n(Type all buildings. Type f to finish)\n(Type the same number/name again to no longer mortgage the place)")
        while True:
                s = "" + input()
                for x in range(0, 28):
                        if WhatYouThinkingOfSelling[x] == 1:
                                print("Player " + str(PlayerWhosSelling) + " decided to no longer mortgage " + list1[x])
                                WhatYouThinkingOfSelling[x] = 0
                        elif list1[x] == s and PlayerWhosSelling == list3[x] or s == ("" + str(x)) and PlayerWhosSelling == list3[x]:
                                print("player " + str(PlayerWhosSelling) + " decided to mortgage " +list1[x])
                                WhatYouThinkingOfSelling[x] = 1
                if s == 'f' or s == 'fi' or s == 'fin' or s == 'fini' or s == 'finis' or s == 'finish':
                        if PlayerWhosSelling == 1 and Player1Money > 0 or PlayerWhosSelling == 2 and Player2Money > 0 or PlayerWhosSelling == 3 and Player3Money > 0 or PlayerWhosSelling == 4 and Player4Money > 0:
                                break
                        else:
                                print("Are you sure? You're going to become bankrupt, ending the game.")
                                while True:
                                        YESNO = "" + input()
                                        try:
                                                s.lower()
                                        except:
                                                print("Error, whatever you put is not a letter.")
                                        if YESNO == "yes" or YESNO == "ye" or YESNO == "y":
                                                break
                                        elif YESNO == "no" or YESNO == "n":
                                                break
                                        else:
                                                print("That is not yes/ye/y or no/n. Please only use one of those few words words.")
                                if YESNO == "yes" or YESNO == "ye" or YESNO == "y":
                                        break
                

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

DoublesForJail = 0
        
x = HowManyPlayers()
Player1LenghtInJail = 0
Player2LenghtInJail = 0
Player3LenghtInJail = 0
Player4LenghtInJail = 0
#global HousesArray
if x == 3:
    Player4Location = 99999
    Player4Money = 1
elif x == 2:
    Player4Location = 99999
    Player3Location = 99999
    Player4Money = 1
    Player3Money = 1
playerTurn = 1
while True:
    if playerTurn == 5:
        playerTurn = 1
    elif playerTurn == 4 and Player4Location == 99999:
        playerTurn = 1
    elif playerTurn == 3 and Player3Location == 99999:
        playerTurn = 1
    else:
        MonopolyMap(Player1Location, Player2Location, Player3Location, Player4Location, Player1InJail, Player2InJail, Player3InJail, Player4InJail, Player1Money, Player2Money, Player3Money, Player4Money, FreeParkingMoney)
        print("It is currently Player " + str(playerTurn) + " Turn.\nType 'Roll' or 'r' to Roll.\nType 'Trade' or 't' to switch money/buildings with other players.\nType 'Add' or 'a' to house to one of your monopolies.\nType 'Stats' or 's' to learn about what people currently have and have not.")
        WhatTheyWantToDo = input().lower()
        if WhatTheyWantToDo.lower() == "roll" or WhatTheyWantToDo.lower() == "r" or WhatTheyWantToDo.lower() == "ro" or WhatTheyWantToDo.lower() == "rol":
                if playerTurn == 1:
                    Roll = 0
                    Roll = DiceRoll(1)
                    print("Player 1 has rolled a " + str(rollOne) +" and a "+ str(rollTwo) +" Which equals "+ str(Roll) + "!\nPress Enter to Move.")
                    input()
                    if Player1InJail == 1 and rollOne != rollTwo and Player1LenghtInJail == 3:
                            print("Player 1 has rolled 3 non-doubles while in jail, they will get out of jail, but at the cost of 50 dollars.")
                            Player1Money -= 50
                            Player1InJail = 0
                            input()
                    if DoublesForJail == 2 and rollOne == rollTwo:
                            print("Player 1 has rolled 3 doubles in a roll, automatically making them go to jail.")
                            Player1InJail = 1
                            Player1Location = 11
                            input()
                    elif Player1InJail == 1 and rollOne != rollTwo:
                            print("Player 1 has rolled a " + rollOne + " and a " + rollTwo + "which is not a double, so you stay in jail.")
                            Player1LenghtInJail += 1
                            input()
                    else:
                            if Player1InJail == 1:
                                    print("Player 1 has rolled a double, so they escape from jail.")
                                    input()
                            Player1InJail = 0
                            if int(Player1Location + Roll) > 40:
                                Player1Money += 200
                                Player1Location = int(Player1Location + Roll) - 40
                                LandedPlaces(Player1Location, 1)
                            else:
                                Player1Location += Roll
                                LandedPlaces(Player1Location, 1)
                    #print("Ok.")
                    #input()
                elif playerTurn == 2:
                    Roll = 0
                    Roll = DiceRoll(2)
                    print("player 2 has rolled a " + str(rollOne) +" and a "+ str(rollTwo) +" Which equals "+ str(Roll) + "!\nPress Enter to Move.")
                    input()
                    if Player2InJail == 1 and rollOne != rollTwo and Player2LenghtInJail == 3:
                            print("Player 2 has rolled 3 non-doubles while in jail, they will get out of jail, but at the cost of 50 dollars.")
                            Player2Money -= 50
                            Player2InJail = 0
                            input()
                    if DoublesForJail == 2 and rollOne == rollTwo:
                            print("Player 2 has rolled 3 doubles in a roll, automatically making them go to jail.")
                            Player2InJail = 1
                            Player2Location = 11
                            input()
                    elif Player2InJail == 1 and rollOne != rollTwo:
                            print("Player 2 has rolled a " + rollOne + " and a " + rollTwo + "which is not a double, so you stay in jail.")
                            Player2LenghtInJail += 1
                            input()
                    else:
                            if Player2InJail == 1:
                                    print("Player 2 has rolled a double, so they escape from jail.")
                                    input()
                            Player2InJail = 0
                            if int(Player2Location + Roll) > 40:
                                Player2Money += 200
                                Player2Location = int(Player2Location + Roll) - 40
                                LandedPlaces(Player2Location, 2)
                            else:
                                Player2Location += Roll
                                LandedPlaces(Player2Location, 2)
                    #print("Ok.")
                    #input()
                elif playerTurn == 3:
                    Roll = 0
                    Roll = DiceRoll(3)
                    print("Player 3 has rolled a " + str(rollOne) +" and a "+ str(rollTwo) +" Which equals "+ str(Roll) + "!\nPress Enter to Move.")
                    input()
                    if Player3InJail == 1 and rollOne != rollTwo and Player3LenghtInJail == 3:
                            print("Player 3 has rolled 3 non-doubles while in jail, they will get out of jail, but at the cost of 50 dollars.")
                            Player3Money -= 50
                            Player3InJail = 0
                            input()
                    if DoublesForJail == 2 and rollOne == rollTwo:
                            print("Player 3 has rolled 3 doubles in a roll, automatically making them go to jail.")
                            Player3InJail = 1
                            Player3Location = 11
                            input()
                    elif Player3InJail == 1 and rollOne != rollTwo:
                            print("Player 3 has rolled a " + rollOne + " and a " + rollTwo + "which is not a double, so you stay in jail.")
                            Player3LenghtInJail += 1
                            input()
                    else:
                            if Player3InJail == 1:
                                    print("Player 3 has rolled a double, so they escape from jail.")
                                    input()
                            Player3InJail = 0
                            if int(Player3Location + Roll) > 40:
                                Player3Money += 200
                                Player3Location = int(Player3Location + Roll) - 40
                                LandedPlaces(Player3Location, 3)
                            else:
                                Player3Location += Roll
                                LandedPlaces(Player3Location, 3)
                else:
                    Roll = 0
                    Roll = DiceRoll(4)
                    print("Player 4 has rolled a " + str(rollOne) +" and a "+ str(rollTwo) +" Which equals "+ str(Roll) + "!\nPress Enter to Move.")
                    input()
                    if Player4InJail == 1 and rollOne != rollTwo and Player3LenghtInJail == 3:
                            print("Player 4 has rolled 3 non-doubles while in jail, they will get out of jail, but at the cost of 50 dollars.")
                            Player4Money -= 50
                            Player4InJail = 0
                            input()
                    if DoublesForJail == 2 and rollOne == rollTwo:
                            print("Player 4 has rolled 3 doubles in a roll, automatically making them go to jail.")
                            Player4InJail = 1
                            Player4Location = 11
                            input()
                    elif Player4InJail == 1 and rollOne != rollTwo:
                            print("Player 4 has rolled a " + rollOne + " and a " + rollTwo + "which is not a double, so you stay in jail.")
                            Player4LenghtInJail += 1
                            input()
                    else:
                            if Player4InJail == 1:
                                    print("Player 4 has rolled a double, so they escape from jail.")
                                    input()
                            Player4InJail = 0
                            if int(Player4Location + Roll) > 40:
                                Player4Money += 200
                                Player4Location = int(Player4Location + Roll) - 40
                                LandedPlaces(Player4Location, 4)
                            else:
                                Player4Location += Roll
                                LandedPlaces(Player4Location, 4)
                if rollOne != rollTwo or DoublesForJail == 2 and rollOne == rollTwo:
                        playerTurn += 1
                        DoublesForJail = 0
                else:
                        print("Since Player " + str(playerTurn) +" rolled doubles, Player " + str(playerTurn) + " gets to go again.")
                        input()
                        DoublesForJail += 1
        elif WhatTheyWantToDo.lower() == "stats" or WhatTheyWantToDo.lower() == "stat" or WhatTheyWantToDo.lower() == "sta" or WhatTheyWantToDo.lower() == "st" or WhatTheyWantToDo.lower() == "s":
                #list1 is names
                #list2 is cost of places
                #list3 is the owner
                #list4 is the rent
                for x in range(0, 60):
                        print("")
                os.system('cls')
                os.system('clear')
                for x in range(0, 28):
                        if x < 22:
                                print(list1[x] + ", cost - " + str(list2[x])+ ", the owner is player - " + str(list3[x]) + " and the rent is currently " + str(list4[x])+" Houses on this place "+ str(HousesArray[x]) +".")
                        else:
                                print(list1[x] + ", cost - " + str(list2[x])+ ", the owner is player - " + str(list3[x]) + " and the rent is currently " + str(list4[x])+".")
                                
                print("Press enter to continue.")
                input()
        elif WhatTheyWantToDo.lower() == "trade" or WhatTheyWantToDo.lower() == "t" or WhatTheyWantToDo.lower() == "tr" or WhatTheyWantToDo.lower() == "tra" or WhatTheyWantToDo.lower() == "trad":
                print("Who do you want to trade with? (You can just type in the number).")
                if(playerTurn != 1):
                        print("Player 1.")
                if(playerTurn != 2):
                        print("Player 2.")
                if(playerTurn != 3 and Player3Location != 99999):
                        print("Player 3.")
                if(playerTurn != 4 and Player4Location != 99999):
                        print("Player 4.")
                print("Exit.")
                while True:
                        PlayerToTradeWith = "" + input().lower()
                        if playerTurn != 1 and PlayerToTradeWith == "Player 1" or playerTurn != 1 and PlayerToTradeWith == "1":
                                TradingWithPeople(playerTurn ,1)
                                break
                        elif playerTurn != 2 and PlayerToTradeWith == "Player 2" or playerTurn != 2 and PlayerToTradeWith == "2":
                                TradingWithPeople(playerTurn ,2)
                                break
                        elif playerTurn != 3 and PlayerToTradeWith == "Player 3" and Player3Location != 99999 or playerTurn != 3 and PlayerToTradeWith == "3" and Player3Location != 99999:
                                TradingWithPeople(playerTurn ,3)
                                break
                        elif playerTurn != 4 and PlayerToTradeWith == "Player 4" and Player4Location != 99999 or playerTurn != 4 and PlayerToTradeWith == "4" and Player4Location != 99999:
                                TradingWithPeople(playerTurn ,4)
                                break
                        elif PlayerToTradeWith == "exit" or PlayerToTradeWith == "exi" or PlayerToTradeWith == "ex" or PlayerToTradeWith == "e":
                                break
                        else:
                                print("Who do you want to trade with again?")
                
        elif WhatTheyWantToDo.lower() == "add" or WhatTheyWantToDo.lower() == "ad" or WhatTheyWantToDo.lower() == "a":
                PromotingBuildings(playerTurn)
        elif WhatTheyWantToDo.lower() == "mortgage" or WhatTheyWantToDo.lower() == "mortgag" or WhatTheyWantToDo.lower() == "mortga" or WhatTheyWantToDo.lower() == "mortg" or WhatTheyWantToDo.lower() == "mort" or WhatTheyWantToDo.lower() == "mor" or WhatTheyWantToDo.lower() == "mo" or WhatTheyWantToDo.lower() == "m":
                HouseForSells(playerTurn)
        elif WhatTheyWantToDo.lower() == "debug":
                print("Debug mode.")
                debugMode(playerTurn)
        else:
                print("What do you want to do? Roll or Look at stats?")
                input()
