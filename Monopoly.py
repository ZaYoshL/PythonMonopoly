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

#Dicerolls. If there is 0 and 30 that appear in the game there must be an error.
rollOne = 0
rollTwo = 30

#All Imports go here
from MonopolyMap import MonopolyMap
from MonopolyGameOver import GameOver
from PlayersAndRolls import HowManyPlayers
from PlayersAndRolls import DiceRoll
from PlayersAndRolls import ReturnRollOne
from PlayersAndRolls import ReturnRollTwo
from Property import createPlayerList

FreeParkingMoney = 0

#Extra(use for trading)
list5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def UseTheList(LandedOn, WhosThis):
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        waterElectric = 0
        if propertyList[LandedOn].owner == 0 and WhosThis == 1:
            print("Player 1 has landed on "+str(propertyList[LandedOn].name)+"\nWould you like to buy it for $"+str(propertyList[LandedOn].cost)+" (Yes/No)(can also use y/n)(Rent - "+str(propertyList[LandedOn].rent)+").")
            while True:
                if Player1Money < propertyList[LandedOn].cost:
                    print("You don't have enough money to pay " + str(propertyList[LandedOn].name))
                    input()
                    GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    propertyList[LandedOn].owner = 1
                    Player1Money -= propertyList[LandedOn].cost
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif propertyList[LandedOn].owner == 1 and WhosThis == 1:
            print("Player 1 has landed on "+str(propertyList[LandedOn].name)+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif propertyList[LandedOn].owner != 1 and propertyList[LandedOn].owner != 0 and WhosThis == 1:
            print("Player 1 has landed on "+str(propertyList[LandedOn].name)+"\nPlayer " + str(propertyList[LandedOn].owner)+" owns this place and it cost $" + str(propertyList[LandedOn].rent)+"\nPress enter.")
            Player1Money -= propertyList[LandedOn].rent
            if propertyList[LandedOn].owner == 2:
                Player2Money += propertyList[LandedOn].rent
            elif propertyList[LandedOn].owner == 3:
                Player3Money += propertyList[LandedOn].rent
            else:
                Player4Money += propertyList[LandedOn].rent
            GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
            input()
        elif propertyList[LandedOn].owner == 0 and WhosThis == 2:
            print("Player 2 has landed on "+str(propertyList[LandedOn].name)+"\nWould you like to buy it for $"+str(propertyList[LandedOn].cost)+" (Yes/No)(can also use y/n)(Rent - "+str(propertyList[LandedOn].rent)+").")
            while True:
                if Player2Money < propertyList[LandedOn].cost:
                    print("You don't have enough money to pay " + str(propertyList[LandedOn].name))
                    input()
                    GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    propertyList[LandedOn].owner = 2
                    Player2Money -= propertyList[LandedOn].cost
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif propertyList[LandedOn].owner == 2 and WhosThis == 2:
            print("Player 2 has landed on "+str(propertyList[LandedOn].name)+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif propertyList[LandedOn].owner != 2 and propertyList[LandedOn].owner != 0 and WhosThis == 2:
            print("Player 2 has landed on "+str(propertyList[LandedOn].name)+"\nPlayer " + str(propertyList[LandedOn].owner)+" owns this place and it cost $" + str(propertyList[LandedOn].rent)  +"\nPress enter.")
            Player2Money -= propertyList[LandedOn].rent
            if propertyList[LandedOn].owner == 1:
                Player1Money += propertyList[LandedOn].rent
            elif propertyList[LandedOn].owner == 3:
                Player3Money += propertyList[LandedOn].rent
            else:
                Player4Money += propertyList[LandedOn].rent
            GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
            input()
        elif propertyList[LandedOn].owner == 0 and WhosThis == 3:
            print("Player 3 has landed on "+str(propertyList[LandedOn].name)+"\nWould you like to buy it for $"+str(propertyList[LandedOn].cost)+" (Yes/No)(can also use y/n)(Rent - "+str(propertyList[LandedOn].rent)+").")
            while True:
                if Player3Money < propertyList[LandedOn].cost:
                    print("You don't have enough money to pay "+str(propertyList[LandedOn].name))
                    input()
                    GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    propertyList[LandedOn].owner = 3
                    Player3Money -= propertyList[LandedOn].cost
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif propertyList[LandedOn].owner == 3 and WhosThis == 3:
            print("Player 3 has landed on "+str(propertyList[LandedOn].name)+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif propertyList[LandedOn].owner != 3 and propertyList[LandedOn].owner != 0 and WhosThis == 3:
            print("Player 3 has landed on "+str(propertyList[LandedOn].name)+"\nPlayer " + str(propertyList[LandedOn].owner)+" owns this place and it cost $" + str(propertyList[LandedOn].rent)+"\nPress enter.")
            Player3Money -= propertyList[LandedOn].rent
            if propertyList[LandedOn].owner == 1:
                Player1Money += propertyList[LandedOn].rent
            elif propertyList[LandedOn].owner == 2:
                Player2Money += propertyList[LandedOn].rent
            else:
                Player4Money += propertyList[LandedOn].rent
            GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
            input()
        elif propertyList[LandedOn].owner == 0 and WhosThis == 4:
            print("Player 4 has landed on "+str(propertyList[LandedOn].name)+"\nWould you like to buy it for $"+str(propertyList[LandedOn].cost)+" (Yes/No)(can also use y/n)(Rent - "+str(propertyList[LandedOn].rent)+").")
            while True:
                if Player4Money < propertyList[LandedOn].cost:
                    print("You don't have enough money to pay "+str(propertyList[LandedOn].name))
                    input()
                    GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
                    break
                Answer = input().lower()
                if Answer == 'yes' or Answer == 'ye' or Answer == 'y':
                    propertyList[LandedOn].owner = 4
                    Player4Money -= propertyList[LandedOn].cost
                    break
                elif Answer == 'no' or Answer == 'n':
                    #Add ability to Fighting for place here later
                    break
                else:
                    print("What is it? Yes or No?")
        elif propertyList[LandedOn].owner == 4 and WhosThis == 4:
            print("Player 4 has landed on "+str(propertyList[LandedOn].name)+"\nYou own this place, so it cost nothing to land on it.\nPress enter.")
            input()
        elif propertyList[LandedOn].owner != 4 and propertyList[LandedOn].owner != 0 and WhosThis == 4:
            print("Player 4 has landed on "+str(propertyList[LandedOn].name)+"\nPlayer " + str(propertyList[LandedOn].owner)+" owns this place and it cost $" + str(propertyList[LandedOn].rent)+"\nPress enter.")
            Player4Money -= propertyList[LandedOn].rent
            if propertyList[LandedOn].owner == 1:
                Player1Money += propertyList[LandedOn].rent
            elif propertyList[LandedOn].owner == 2:
                Player2Money += propertyList[LandedOn].rent
            else:
                Player3Money += propertyList[LandedOn].rent
            GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
            input()

def LandedPlaces(landedOn, WhosThis):
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
        elif WhosThis == 2:
            Player2Money += 50
        elif WhosThis == 3:
            Player3Money += 50
        else:
            Player4Money += 50
        print("Player " + str(WhosThis) + " landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
        input()
    elif landedOn == 4:#Baltic Ave.
           UseTheList(1, WhosThis)
    elif landedOn == 5:#Income Tax
        if WhosThis == 1:
            if (int)(Player1Money/10) < 200:
                print("Player 1 landed on the Income Tax\nPlayer 1 had to pay 10% of his value in tax which was " + str((int)(Player1Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player1Money/10)
                Player1Money -= (int)(Player1Money/10)
            else:
                FreeParkingMoney += 200
                Player1Money -= 200
                print("Player 1 landed on the Income Tax\nPlayer 1 had to pay $200 in tax. (Press Enter)")
        elif WhosThis == 2:
            if (int)(Player2Money/10) < 200:
                print("Player 2 landed on the Income Tax\nPlayer 2 had to pay 10% of his value in tax which was " + str((int)(Player2Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player2Money/10)
                Player2Money -= (int)(Player2Money/10)
            else:
                FreeParkingMoney += 200
                Player2Money -= 200
                print("Player 2 landed on the Income Tax\nPlayer 2 had to pay $200 in tax. (Press Enter)")
        elif WhosThis == 3:
            if (int)(Player3Money/10) < 200:
                print("Player 3 landed on the Income Tax\nPlayer 3 had to pay 10% of his value in tax which was " + str((int)(Player3Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player3Money/10)
                Player3Money -= (int)(Player3Money/10)
            else:
                FreeParkingMoney += 200
                Player3Money -= 200
                print("Player 3 landed on the Income Tax\nPlayer 3 had to pay $200 in tax. (Press Enter)")
        else:
            if (int)(Player4Money/10) < 200:
                print("Player 4 landed on the Income Tax\nPlayer 4 had to pay 10% of his value in tax which was " + str((int)(Player4Money/10)) + ". (Press Enter)")
                FreeParkingMoney += (int)(Player4Money/10)
                Player4Money -= (int)(Player4Money/10)
            else:
                FreeParkingMoney += 200
                Player4Money -= 200
                print("Player 4 landed on the Income Tax\nPlayer 4 had to pay $200 in tax. (Press Enter)")
        GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
        input()
    elif landedOn == 6:#Reading Railroad
            UseTheList(22, WhosThis)
    elif landedOn == 7:#Oriental Ave.
            UseTheList(2, WhosThis)
    elif landedOn == 8:
            if WhosThis == 1:
                    Player1Money += 50
            elif WhosThis == 2:
                    Player2Money += 50
            elif WhosThis == 3:
                    Player3Money += 50
            else:
                    Player4Money += 50
            print("Player " + str(WhosThis) + " landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
    elif landedOn == 9:
            UseTheList(3, WhosThis)
    elif landedOn == 10:
            UseTheList(4, WhosThis)
    elif landedOn == 11:
            if WhosThis == 1:
                    if Player1InJail == 0:
                            print("Player 1 is just visiting jail. (Press Enter)")
                    else:
                            print("Player 1 is currently in jail. (Press Enter)")
            elif WhosThis == 2:
                    if Player2InJail == 0:
                            print("Player 2 is just visiting jail. (Press Enter)")
                    else:
                            print("Player 2 is currently in jail. (Press Enter)")
            elif WhosThis == 3:
                    if Player3InJail == 0:
                            print("Player 3 is just visiting jail. (Press Enter)")
                    else:
                            print("Player 3 is currently in jail. (Press Enter)")
            else:
                    if Player4InJail == 0:
                            print("Player 4 is just visiting jail. (Press Enter)")
                    else:
                            print("Player 4 is currently in jail. (Press Enter)")
            input()
    elif landedOn == 12:
            UseTheList(5, WhosThis)
    elif landedOn == 13:#26
            if propertyList[26].owner != 0:
                    if propertyList[26].owner == propertyList[27].owner:
                            propertyList[26].rent = random.randint(2, 12) * 10
                    else:
                            propertyList[26].rent = random.randint(2, 12) * 4
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
            elif WhosThis == 2:
                    Player2Money += 50
            elif WhosThis == 3:
                    Player3Money += 50
            else:
                    Player4Money += 50
            print("Player "+ str(WhosThis) +" landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
    elif landedOn == 19:
            UseTheList(9, WhosThis)
    elif landedOn == 20:
            UseTheList(10, WhosThis)
    elif landedOn == 21:
            if WhosThis == 1:
                    Player1Money += FreeParkingMoney
            elif WhosThis == 2:
                    Player2Money += FreeParkingMoney
            elif WhosThis == 3:
                    Player3Money += FreeParkingMoney
            else:
                    Player4Money += FreeParkingMoney
            print("Player " + str(WhosThis) + " landed on Free Parking\nPlayer 4 has gained $" + str(FreeParkingMoney) + "!")
            FreeParkingMoney = 0
            input()            
    elif landedOn == 22:
            UseTheList(11, WhosThis) 
    elif landedOn == 23:
            if WhosThis == 1:
                    Player1Money += 50
            elif WhosThis == 2:
                    Player2Money += 50
            elif WhosThis == 3:
                    Player3Money += 50
            else:
                    Player4Money += 50
            print("Player " + str(WhosThis) + " landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
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
            if propertyList[27].owner != 0:
                    if propertyList[26].owner == propertyList[27].owner:
                            propertyList[27].rent = random.randint(2, 12) * 10
                    else:
                            propertyList[27].rent = random.randint(2, 12) * 4
            if WhosThis == 1:
                    UseTheList(27, WhosThis)
            elif WhosThis == 2:
                    UseTheList(27, WhosThis)
            elif WhosThis == 3:
                    UseTheList(27, WhosThis)
            else:
                    UseTheList(27, WhosThis)
    elif landedOn == 30:
            UseTheList(16, WhosThis)
    elif landedOn == 31:
            global Player1Location
            global Player2Location
            global Player3Location
            global Player4Location
            if WhosThis == 1:
                    Player1InJail = 1
                    Player1Location = 11
            elif WhosThis == 2:
                    Player2InJail = 1
                    Player2Location = 11
            elif WhosThis == 3:
                    Player3InJail = 1
                    Player3Location = 11
            else:
                    Player4InJail = 1
                    Player4Location = 11
            print("Player " + str(WhosThis) + " has to go to Jail. (Press Enter)")
            input()
    elif landedOn == 32:
            UseTheList(17, WhosThis)
    elif landedOn == 33:
            UseTheList(18, WhosThis)
    elif landedOn == 34:
            if WhosThis == 1:
                    Player1Money += 50
            elif WhosThis == 2:
                    Player2Money += 50
            elif WhosThis == 3:
                    Player3Money += 50
            else:
                    Player4Money += 50
            print("Player " + str(WhosThis) + " landed on the Community Chest\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
    elif landedOn == 35:
            UseTheList(19, WhosThis)
    elif landedOn == 36:
            UseTheList(25, WhosThis)            
    elif landedOn == 37:
            if WhosThis == 1:
                    Player1Money += 50
            elif WhosThis == 2:
                    Player2Money += 50
            elif WhosThis == 3:
                    Player3Money += 50
            else:
                    Player4Money += 50
            print("Player " + str(WhosThis) + " landed on Chance\nSince I haven't added the random chance, here's 50 dollars. (Press Enter)")
            input()
    elif landedOn == 38:
            UseTheList(20, WhosThis)    
    elif landedOn == 39:
            if WhosThis == 1:
                    Player1Money -= 75
            elif WhosThis == 2:
                    Player2Money -= 75
            elif WhosThis == 3:
                    Player3Money -= 75
            else:
                    Player4Money -= 75
            FreeParkingMoney += 75
            print("Player " + str(WhosThis) + " landed on Luxury Tax\nThey have to pay $75. (Press Enter)")
            input()
            GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
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
                                 if propertyList[x].owner == StarterOfTrade:
                                         print(propertyList[x].name)
                                         
                        print("And player " + str(WhoTheyWantToTrade) + " can trade...")
                        for x in range(0, 28):
                                 if propertyList[x].owner == WhoTheyWantToTrade:
                                         print(propertyList[x].name)
                        print("(Type finish when you're done. If you type the same place again, it will trade back the places to the original owner.)")                 
                        while True:
                                TradingABuilding = input().lower()
                                for x in range(0, 28):
                                        if TradingABuilding == propertyList[x].name.lower():
                                                if list5[x] == WhoTheyWantToTrade or list5[x] == StarterOfTrade:
                                                        list5[x] = 0
                                                        print("The trade was canceled.")
                                                elif propertyList[x].owner == WhoTheyWantToTrade:
                                                        list5[x] = StarterOfTrade
                                                        print("The trade was succesful.")
                                                elif propertyList[x].owner == StarterOfTrade:
                                                        list5[x] = WhoTheyWantToTrade
                                                        print("The trade was succesful.")
                                                else:
                                                        print("Neither players own " + propertyList[x].name)
                                if TradingABuilding == "finish" or TradingABuilding == "exit":
                                        break
                                print("Anything else? (Type finish or exit to stop trading building.)")
                        print("Now, will you like to trade money or finish?")
                                
                elif WhatTheyChoose.lower() == "finish" or WhatTheyChoose.lower() == "finis" or WhatTheyChoose.lower() == "fini" or WhatTheyChoose.lower() == "fin" or WhatTheyChoose.lower() == "fin" or WhatTheyChoose.lower() == "fi" or WhatTheyChoose.lower() == "f":
                        if playerOfTrade == 0:
                                print("Player " + str(StarterOfTrade) + " is willing to give player "+str(WhoTheyWantToTrade) +" $"+ str(GiveMoney1) + " and")
                                for x in range(0, 28):
                                        if list5[x] == WhoTheyWantToTrade:
                                                print(propertyList[x].name + ", ")   
                                print("for...")
                                print(str(GiveMoney2) + " of player " + str(WhoTheyWantToTrade)+"'s gold and ")
                                for x in range(0, 28):
                                        if list5[x] == StarterOfTrade:
                                                print(propertyList[x].name+", ")
                                                
                                print("Does player " + str(WhoTheyWantToTrade) + " agree to this? (yes or no)")
                        else:
                                print("Player " + str(WhoTheyWantToTrade) + " wants player "+str(StarterOfTrade) +" to instead give them $"+ str(GiveMoney1) + " and ")
                                for x in range(0, 28):
                                        if list5[x] == WhoTheyWantToTrade:
                                                print(propertyList[x].name+ ", ")
                                print("for...")
                                print("Player " + str(WhoTheyWantToTrade) +"'s $"+ str(GiveMoney2) + " and ")
                                for x in range(0, 28):
                                        if list5[x] == StarterOfTrade:
                                                print(propertyList[x].name+", ")
                                print("Does player " + str(StarterOfTrade) + " agree to this? (yes or no)")
                        exitTradeLoop = 0
                        while True:       
                                AnswerToTrade = input().lower()
                                if AnswerToTrade.lower() == "yes" or AnswerToTrade.lower() == "y" or AnswerToTrade.lower() == "ye":
                                        if StarterOfTrade == 1:
                                                GiveMoney1 = int(GiveMoney1)
                                                GiveMoney2 = int(GiveMoney2)
                                                if WhoTheyWantToTrade == 2:
                                                        GivingAway(1, 2, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                elif WhoTheyWantToTrade == 3:
                                                        GivingAway(1, 3, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                else:
                                                        GivingAway(1, 4, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                        elif StarterOfTrade == 2:
                                                if WhoTheyWantToTrade == 1:
                                                        GivingAway(2, 1, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                elif WhoTheyWantToTrade == 3:
                                                        GivingAway(2, 3, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                else:
                                                        GivingAway(2, 4, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                        elif StarterOfTrade == 3:
                                                if WhoTheyWantToTrade == 1:
                                                        GivingAway(3, 1, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                elif WhoTheyWantToTrade == 2:
                                                        GivingAway(3, 2, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                else:
                                                        GivingAway(3, 4, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                        else:
                                                if WhoTheyWantToTrade == 1:
                                                        GivingAway(4, 1, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                elif WhoTheyWantToTrade == 2:
                                                        GivingAway(4, 2, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                                else:
                                                        GivingAway(4, 3, GiveMoney1, GiveMoney2, StarterOfTrade, WhoTheyWantToTrade)
                                        exitTradeLoop = 1
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

def GivingAway(Player1, Player2, MoneyGiven1, MoneyGiven2, StarterOfTrade, WhoTheyWantToTrade):
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        if Player1 == 1:
                Player1Money -= ((int)(MoneyGiven1))
                Player1Money += ((int)(MoneyGiven2))
        elif Player1 == 2:
                Player2Money -= ((int)(MoneyGiven1))
                Player2Money += ((int)(MoneyGiven2))
        elif Player1 == 3:
                Player3Money -= ((int)(MoneyGiven1))
                Player3Money += ((int)(MoneyGiven2))
        else:
                Player4Money -= ((int)(MoneyGiven1))
                Player4Money += ((int)(MoneyGiven2))
        if Player2 == 1:
                Player1Money -= ((int)(MoneyGiven2))
                Player1Money += ((int)(MoneyGiven1))
        elif Player2 == 2:
                Player2Money -= ((int)(MoneyGiven2))
                Player2Money += ((int)(MoneyGiven1))
        elif Player2 == 3:
                Player3Money -= ((int)(MoneyGiven2))
                Player3Money += ((int)(MoneyGiven1))
        else:
                Player4Money -= ((int)(MoneyGiven2))
                Player4Money += ((int)(MoneyGiven1))
        for x in range(0, 28):
                if list5[x] == StarterOfTrade:
                        propertyList[x].name = StarterOfTrade
                if list5[x] == WhoTheyWantToTrade:
                        propertyList[x].name = WhoTheyWantToTrade
        print("The deal was succesful. (Please press enter to continue.)")
        input()

GreenHouses = 32
RedHotels = 12
#                          0  2  4  5  7  9  0  2  4  5  7  8  0  2  3  5  8  0
#              2  4  7  9  1  1  1  1  1  1  2  2  2  2  2  2  3  3  3  3  3  4
HousesArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def PromotingBuildings(PlayerWhosPromoting):
        global HousesArray
        global GreenHouses
        global RedHotels
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        print("You can currently put green and red houses on...")
        if propertyList[0].owner == propertyList[1].owner == PlayerWhosPromoting:
                print("Mediterranean Ave. and Baltic Ave.")
        if propertyList[2].owner == propertyList[3].owner == propertyList[4].owner == PlayerWhosPromoting:
                print("Oriental Ave., Vermont Ave., and Connecticut Ave.")
        if propertyList[5].owner == propertyList[6].owner == propertyList[7].owner == PlayerWhosPromoting:
                print("St. Charles Place, States Ave., and Virginia Ave.")
        if propertyList[8].owner == propertyList[9].owner == propertyList[10].owner == PlayerWhosPromoting:
                print("St. James Place, Tennessee Ave., and New York Ave.")
        if propertyList[11].owner == propertyList[12].owner == propertyList[13].owner == PlayerWhosPromoting:
                print("Kentucky Ave., Indiana Ave., and Illinois Ave.")
        if propertyList[14].owner == propertyList[15].owner == propertyList[16].owner == PlayerWhosPromoting:
                print("Atlantic Ave., Ventnor Ave., and Marvin Gardens.")
        if propertyList[17].owner == propertyList[18].owner == propertyList[19].owner == PlayerWhosPromoting:
                print("Pacific Ave., North Carolina Ave., and Pennsylvania Ave.")
        if propertyList[20].owner == propertyList[21].owner == PlayerWhosPromoting:
                print("Park Place and Boardwalk.")
        print("Exit.")
        while True:
                WhatTheyWantToPromote = input()
                Cost = [50, 100, 150, 200]
                if propertyList[0].owner == propertyList[1].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[0].name or propertyList[0].owner == propertyList[1].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[1].name :
                        if WhatTheyWantToPromote == propertyList[0].name:
                                print("Do you really want to put a house on " + propertyList[0].name+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 0)
                        if WhatTheyWantToPromote == propertyList[1].name:
                                print("Do you really want to put a house on " + propertyList[1].name+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 1)
                elif propertyList[2].owner == propertyList[3].owner == propertyList[4].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[2].name or propertyList[2].owner == propertyList[3].owner == propertyList[4].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[3].name or propertyList[2].owner == propertyList[3].owner == propertyList[4].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[4].name:
                        if WhatTheyWantToPromote == propertyList[2].name:
                                print("Do you really want to put a house on " + propertyList[2].name+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 2)
                        if WhatTheyWantToPromote == propertyList[3].name:
                                print("Do you really want to put a house on " + propertyList[3].name+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 3)
                        if WhatTheyWantToPromote == propertyList[4].name:
                                print("Do you really want to put a house on " + propertyList[4].name+ " for $"+ str(Cost[0]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[0], 4)
                elif propertyList[5].owner == propertyList[6].owner == propertyList[7].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[5].name or propertyList[5].owner == propertyList[6].owner == propertyList[7].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[6].name or propertyList[5].owner == propertyList[6].owner == propertyList[7].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[7].name:
                        if WhatTheyWantToPromote == propertyList[5].name:
                                print("Do you really want to put a house on " + propertyList[5].name+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 5)
                        if WhatTheyWantToPromote == propertyList[6].name:
                                print("Do you really want to put a house on " + propertyList[6].name+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 6)
                        if WhatTheyWantToPromote == propertyList[7].name:
                                print("Do you really want to put a house on " + propertyList[7].name+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 7)
                elif propertyList[8].owner == propertyList[9].owner == propertyList[10].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[8].name or propertyList[8].owner == propertyList[9].owner == propertyList[10].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[9].name or propertyList[8].owner == propertyList[9].owner == propertyList[10].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[10].name:
                        if WhatTheyWantToPromote == propertyList[8].name:
                                print("Do you really want to put a house on " + propertyList[8].name+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 8)
                        if WhatTheyWantToPromote == propertyList[9].name:
                                print("Do you really want to put a house on " + propertyList[9].name+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 9)
                        if WhatTheyWantToPromote == propertyList[10].name:
                                print("Do you really want to put a house on " + propertyList[10].name+ " for $"+ str(Cost[1]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[1], 10)
                elif propertyList[11].owner == propertyList[12].owner == propertyList[13].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[11].name or propertyList[11].owner == propertyList[12].owner == propertyList[13].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[12].name or propertyList[11].owner == propertyList[12].owner == propertyList[13].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[13].name:
                        if WhatTheyWantToPromote == propertyList[11].name:
                                print("Do you really want to put a house on " + propertyList[11].name+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 11)
                        if WhatTheyWantToPromote == propertyList[12].name:
                                print("Do you really want to put a house on " + propertyList[12].name+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 12)
                        if WhatTheyWantToPromote == propertyList[13].name:
                                print("Do you really want to put a house on " + propertyList[13].name+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 13)
                elif propertyList[14].owner == propertyList[15].owner == propertyList[16].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[14].name or propertyList[14].owner == propertyList[15].owner == propertyList[16].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[15].name or propertyList[14].owner == propertyList[15].owner == propertyList[16].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[16].name:
                        if WhatTheyWantToPromote == propertyList[14].name:
                                print("Do you really want to put a house on " + propertyList[14].name+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 14)
                        if WhatTheyWantToPromote == propertyList[15].name:
                                print("Do you really want to put a house on " + propertyList[15].name+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 15)
                        if WhatTheyWantToPromote == propertyList[16].name:
                                print("Do you really want to put a house on " + propertyList[16].name+ " for $"+ str(Cost[2]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[2], 16)
                elif propertyList[17].owner == propertyList[18].owner == propertyList[19].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[17].name or propertyList[17].owner == propertyList[18].owner == propertyList[19].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[18].name or propertyList[17].owner == propertyList[18].owner == propertyList[19].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[19].name:
                        if WhatTheyWantToPromote == propertyList[17].name:
                                print("Do you really want to put a house on " + propertyList[17].name+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 17)
                        if WhatTheyWantToPromote == propertyList[18].name:
                                print("Do you really want to put a house on " + propertyList[18].name+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 18)
                        if WhatTheyWantToPromote == propertyList[19].name:
                                print("Do you really want to put a house on " + propertyList[19].name+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 19)
                elif propertyList[20].owner == propertyList[21].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[20].name or propertyList[20].owner == propertyList[21].owner == PlayerWhosPromoting and WhatTheyWantToPromote == propertyList[21].name:
                        if WhatTheyWantToPromote == propertyList[20].name:
                                print("Do you really want to put a house on " + propertyList[20].name+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 20)
                        if WhatTheyWantToPromote == propertyList[21].name:
                                print("Do you really want to put a house on " + propertyList[21].name+ " for $"+ str(Cost[3]) +"?(Yes/No)")
                                HouseUpgrading(PlayerWhosPromoting, Cost[3], 21)
                elif WhatTheyWantToPromote.lower() == "exit" or WhatTheyWantToPromote.lower() == "exi" or WhatTheyWantToPromote.lower() == "ex" or WhatTheyWantToPromote.lower() == "e":
                        break
                else:
                        print("You either don't own that place, have a monopoly in that area, or you spelled it wrong.")
        print()



def HouseUpgrading(Player, CostOfHouse, Place):
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
        global AlreadyWasAMonopoly
        if AlreadyWasAMonopoly[0] == 0 and propertyList[0].owner == propertyList[1].owner != 0:
                ChangingList4Mult(0, 1, 99, 0)
        if AlreadyWasAMonopoly[0] == 1 and propertyList[0].owner != propertyList[1].owner != 0:
                ChangingList4Divi(0, 1, 99, 0)
        if AlreadyWasAMonopoly[1] == 0 and propertyList[2].owner == propertyList[3].owner == propertyList[4].owner != 0:
                ChangingList4Mult(2, 3, 4, 1)
        if AlreadyWasAMonopoly[1] == 1 and propertyList[2].owner != propertyList[3].owner != propertyList[4].owner != 0:
                ChangingList4Divi(2, 3, 4, 1)
        if AlreadyWasAMonopoly[2] == 0 and propertyList[5].owner == propertyList[6].owner == propertyList[7].owner != 0:
                ChangingList4Mult(5, 6, 7, 2)
        if AlreadyWasAMonopoly[2] == 1 and propertyList[5].owner != propertyList[6].owner != propertyList[7].owner != 0:
                ChangingList4Divi(5, 6, 7, 2)
        if AlreadyWasAMonopoly[3] == 0 and propertyList[8].owner == propertyList[9].owner == propertyList[10].owner != 0:
                ChangingList4Mult(8, 9, 10, 3)
        if AlreadyWasAMonopoly[3] == 1 and propertyList[8].owner != propertyList[9].owner != propertyList[10].owner != 0:
                ChangingList4Divi(8, 9, 10, 3)
        if AlreadyWasAMonopoly[4] == 0 and propertyList[11].owner == propertyList[12].owner == propertyList[13].owner != 0:
                ChangingList4Mult(11, 12, 13, 4)
        if AlreadyWasAMonopoly[4] == 1 and propertyList[11].owner != propertyList[12].owner != propertyList[13].owner != 0:
                ChangingList4Divi(11, 12, 13, 4)
        if AlreadyWasAMonopoly[5] == 0 and propertyList[14].owner == propertyList[15].owner == propertyList[16].owner != 0:
                ChangingList4Mult(14, 15, 16, 5)
        if AlreadyWasAMonopoly[5] == 1 and propertyList[14].owner != propertyList[15].owner != propertyList[16].owner != 0:
                ChangingList4Divi(14, 15, 16, 5)
        if AlreadyWasAMonopoly[6] == 0 and propertyList[17].owner == propertyList[18].owner == propertyList[19].owner != 0:
                ChangingList4Mult(17, 18, 19, 6)
        if AlreadyWasAMonopoly[6] == 1 and propertyList[17].owner != propertyList[18].owner != propertyList[19].owner != 0:
                ChangingList4Divi(17, 18, 19, 6)
        if AlreadyWasAMonopoly[7] == 0 and propertyList[20].owner == propertyList[21].owner != 0:
                ChangingList4Mult(20, 21, 99, 7)
        if AlreadyWasAMonopoly[7] == 1 and propertyList[20].owner != propertyList[21].owner != 0:
                ChangingList4Divi(20, 21, 99, 7)
        print()

def ChangingList4Mult(FirstPlace, SecondPlace, ThirdPlace, MonopolyLocation):
        propertyList[FirstPlace].rent *= 2
        propertyList[FirstPlace].rent = (int)(propertyList[FirstPlace].rent)
        propertyList[SecondPlace].rent *= 2
        propertyList[SecondPlace].rent = (int)(propertyList[SecondPlace].rent)
        if ThirdPlace != 99:
                propertyList[ThirdPlace].rent *= 2
                propertyList[ThirdPlace].rent = (int)(propertyList[ThirdPlace].rent)
        AlreadyWasAMonopoly[MonopolyLocation] = 1
        
def ChangingList4Divi(FirstPlace, SecondPlace, ThirdPlace, MonopolyLocation):
        propertyList[FirstPlace].rent /= 2
        propertyList[FirstPlace].rent = (int)(propertyList[FirstPlace].rent)
        propertyList[SecondPlace].rent /= 2
        propertyList[SecondPlace].rent = (int)(propertyList[SecondPlace].rent)
        if ThirdPlace != 99:
                propertyList[ThirdPlace].rent /= 2
                propertyList[ThirdPlace].rent = (int)(propertyList[ThirdPlace].rent)
        AlreadyWasAMonopoly[MonopolyLocation] = 0
        

def ChanceTime(PlayerEffected):
        DaNumberYouGot = random.randint(1, 1)
        print()

def CommunityChest(PlayerEffected):
        DaNumberYouGot = random.randint(1, 1)
        print()
      
def debugMode(PlayerDebug):
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
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
        print("13 - Choice who is in jail\n14 - Move somewhere and activate its effect\n15 - Just move everyone somewhere\n16 - Test GameOver()\n17 - Test MONOPOLY()\n18 - Test DiceRoll()\n19 - Retest HowManyPlayers()\n20 - Test UseTheList()\n21 - Test dice picture(Currently broken)\n22 - Change free parking amount")
        print("23 - Change all useless rent ints\n24 - Change all useless house own int\n25 - Give everyone random buildings")
        s = "" + input()
        if s == "1":
                for x in range(0, 28):
                        propertyList[x].owner = PlayerDebug
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
                        propertyList[x].cost = 0
        elif s == "6":
                GreenHouses = input()
                RedHotels = input()
        elif s == "7":
                for x in range(0, 28):
                        propertyList[x].name = ""+input()
        elif s == "8":
                for x in range(0, 28):
                        propertyList[x].cost = ""+input()
        elif s == "9":
                for x in range(0, 28):
                        propertyList[x].owner = ""+input()
        elif s == "10":
                for x in range(0, 28):
                        propertyList[x].rent = ""+input()
        elif s == "11":
                for x in range(0, 28):
                        list5[x] = ""+input()
        elif s == "12":
                Player1Money = ((int)(input()))
                Player2Money = ((int)(input()))
                Player3Money = ((int)(input()))
                Player4Money = ((int)(input()))
        elif s == "13":
                Player1InJail = ((int)(input()))
                Player1InJail = ((int)(input()))
                Player1InJail = ((int)(input()))
                Player1InJail = ((int)(input()))
        elif s == "14":
                PlayToGo = ((int)(input()))
                LandedPlaces(PlayToGo, PlayerDebug)
        elif s == "15":
                Player1Location = ((int)(input()))
                Player2Location = ((int)(input()))
                if Player3Location != 99999:
                        Player3Location = ((int)(input()))
                if Player4Location != 99999:
                        Player4Location = ((int)(input()))
        elif s == "16":
                GameOver(Player1Money, Player2Money, Player3Money, Player4Money)
        elif s == "17":
                MONOPOLY()
        elif s == "18":
                DiceRoll(PlayerDebug)
                rollOne = ReturnRollOne()
                rollTwo = ReturnRollTwo()
        elif s == "19":
                HowManyPlayers()
        elif s == "20":
                PlayToGo = ((int)(input()))
                UseTheList(PlayToGo, PlayerDebug)
        #elif s == "21":
        #        Picture = input()
        #        print(DicePictures[Picture])
        elif s == "22":
                global FreeParkingMoney
                FreeParkingMoney = ((int)(input()))
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
                
                MediterraneanAveRent = ((int)(input()))
                BalticAveRent = ((int)(input()))
                ReadingRailroadRent = ((int)(input()))
                OrientalAveRent = ((int)(input()))
                VermontAveRent = ((int)(input()))
                ConnecticutAveRent = ((int)(input()))
                StCharlesPlaceRent = ((int)(input()))
                ElectricCompanyRent = ((int)(input()))
                StatesAveRent = ((int)(input()))
                VirginiaAveRent = ((int)(input()))
                PennsylvaniaRailroadRent = ((int)(input()))
                StJamesPlaceRent = ((int)(input()))
                TennesseeAveRent = ((int)(input()))
                NewYorkAveRent = ((int)(input()))
                KentuckyAveRent = ((int)(input()))
                IndianaAveRent = ((int)(input()))
                IllinoisAveRent = ((int)(input()))
                BORailroadRent = ((int)(input()))
                AtlanticAveRent = ((int)(input()))
                VentnorAveRent = ((int)(input()))
                WaterWorksRent = ((int)(input()))
                MarvinGardensRent = ((int)(input()))
                PacificAveRent = ((int)(input()))
                NorthCarolinaAveRent = ((int)(input()))
                PennsylvaniaAveRent = ((int)(input()))
                ShortLineRailroadRent = ((int)(input()))
                ParkPlaceRent = ((int)(input()))
                BoardwalkRent = ((int)(input()))
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
                
                MediterraneanAve = ((int)(input()))
                BalticAve = ((int)(input()))
                ReadingRailroad = ((int)(input()))
                OrientalAve = ((int)(input()))
                VermontAve = ((int)(input()))
                ConnecticutAve = ((int)(input()))
                StCharlesPlace = ((int)(input()))
                ElectricCompany = ((int)(input()))
                StatesAve = ((int)(input()))
                VirginiaAve = ((int)(input()))
                PennsylvaniaRailroad = ((int)(input()))
                StJamesPlace = ((int)(input()))
                TennesseeAve = ((int)(input()))
                NewYorkAve = ((int)(input()))
                FreeParkingMoney = ((int)(input()))
                KentuckyAve = ((int)(input()))
                IndianaAve = ((int)(input()))
                IllinoisAve = ((int)(input()))
                BORailroad = ((int)(input()))
                AtlanticAve = ((int)(input()))
                VentnorAve = ((int)(input()))
                WaterWorks = ((int)(input()))
                MarvinGardens = ((int)(input()))
                PacificAve = ((int)(input()))
                NorthCarolinaAve = ((int)(input()))
                PennsylvaniaAve = ((int)(input()))
                ShortLineRailroad = ((int)(input()))
                ParkPlace = ((int)(input()))
                Boardwalk = ((int)(input()))
        elif s == "25":
                if Player3Location == 99999:
                        for x in range(0, 28):
                                propertyList[x].owner = random.randint(1, 2)
                elif Player4Location == 99999:
                        for x in range(0, 28):
                                propertyList[x].owner = random.randint(1, 3)
                else:
                        for x in range(0, 28):
                                propertyList[x].owner = random.randint(1, 4)
        input()

SellingValue = [30, 30, 50, 50, 60, 70, 70, 80, 90, 90, 100, 110, 110, 120, 130, 130, 140, 150, 150, 160, 175, 200, 100, 100, 100, 100, 75, 75]
WhatYouThinkingOfSelling = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
WhatHousesAreCurrentlyBeenSell = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def HouseForSells(PlayerWhosSelling):
        print("You own...")
        global Player1Money
        global Player2Money
        global Player3Money
        global Player4Money
        YESNO = ""
        for x in range(0, 28):
                WhatYouThinkingOfSelling[x] = 0
                if propertyList[x].owner == PlayerWhosSelling:
                        print(str(x) +" - "+propertyList[x].name)
        print("What place do you want to sell?\n(Type all buildings. Type f to finish)\n(Type the same number/name again to no longer mortgage the place)")
        while True:
                s = "" + input()
                for x in range(0, 28):
                        if WhatYouThinkingOfSelling[x] == 1:
                                print("Player " + str(PlayerWhosSelling) + " decided to no longer mortgage " + propertyList[x].name)
                                WhatYouThinkingOfSelling[x] = 0
                        elif propertyList[x].name == s and PlayerWhosSelling == propertyList[x].owner or s == ("" + str(x)) and PlayerWhosSelling == propertyList[x].owner:
                                print("player " + str(PlayerWhosSelling) + " decided to mortgage " +propertyList[x].name)
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
                

DoublesForJail = 0
        
propertyList = createPlayerList()
#print(len(propertyList))
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
    print()
    print()
    os.system('cls')
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
                    rollOne = ReturnRollOne()
                    rollTwo = ReturnRollTwo()
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
                    rollOne = ReturnRollOne()
                    rollTwo = ReturnRollTwo()
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
                    rollOne = ReturnRollOne()
                    rollTwo = ReturnRollTwo()
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
                    rollOne = ReturnRollOne()
                    rollTwo = ReturnRollTwo()
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
                for x in range(0, 60):
                        print("")
                os.system('cls')
                for x in range(0, 28):
                        if x < 22:
                                print(propertyList[x].name + ", cost - " + str(propertyList[x].cost)+ ", the owner is player - " + str(propertyList[x].owner) + " and the rent is currently " + str(propertyList[x].rent)+" Houses on this place "+ str(HousesArray[x]) +".")
                        else:
                                print(propertyList[x].name + ", cost - " + str(propertyList[x].cost)+ ", the owner is player - " + str(propertyList[x].owner) + " and the rent is currently " + str(propertyList[x].rent)+".")
                                
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
