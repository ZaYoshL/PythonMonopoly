import random
import sys
import math
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

def MonopolyMap():
        print('''
                 _________________________________________________________________________________________________________________________________________________________
                |Just visiting|St. Charles  |Electric     |States Ave.  |Virginia Ave.|Pennsylvania |St. James    |Community    |Tennessee    |New York Ave.|Free Parking |
                |             |Place        |Company      |             |             |Railroad     |Place        |Chest        |Ave.         |             |             |''')
        OnJustVisiting = "                |"#If Players are visiting jail
        if Player1Location == 11 and Player1InJail == 0:#If Player 1 Is visiting jail
            OnJustVisiting += "1 "#If Player 1 Is visiting jail
        else:#If Player 1 Is visiting jail
            OnJustVisiting += "  "#If Player 1 Is visiting jail
        if Player2Location == 11 and Player2InJail == 0:#If Player 2 Is visiting jail
            OnJustVisiting += "2 "#If Player 2 Is visiting jail
        else:#If Player 2 Is visiting jail
            OnJustVisiting += "  "#If Player 2 Is visiting jail
        if Player3Location == 11 and Player3InJail == 0:#If Player 3 Is visiting jail
            OnJustVisiting += "3 "#If Player 3 Is visiting jail
        else:#If Player 3 Is visiting jail
            OnJustVisiting += "  "#If Player 3 Is visiting jail
        if Player4Location == 11 and Player4InJail == 0:#If Player 4 Is visiting jail
            OnJustVisiting += "4 "#If Player 4 Is visiting jail
        else:#If Player 4 Is visiting jail
            OnJustVisiting += "  "#If Player 4 Is visiting jail

            
        OnJustVisiting += "     |             |             |             |             |             |             |             |             |             |             |"             
        print(OnJustVisiting)
        print('''                |In Jail      |Price - 140  |Price - 150  |Price - 140  |Price - 160  |Price - 200  |Price - 180  |             |Price - 180  |Price - 200  |             |''')


        PlayersOnTopRow = "                |"#If Players are in the top row
        if Player1Location == 11 and Player1InJail == 1:#If player 1 is in jail
            PlayersOnTopRow += "1 "#If player 1 is in jail
        else:#If player 1 is in jail
            PlayersOnTopRow += "  "#If player 1 is in jail
        if Player1Location == 11 and Player2InJail == 1:#If player 2 is in jail
            PlayersOnTopRow += "2 "#If player 2 is in jail
        else:#If player 2 is in jail
            PlayersOnTopRow += "  "#If player 2 is in jail
        if Player1Location == 11 and Player3InJail == 1:#If player 3 is in jail
            PlayersOnTopRow += "3 "#If player 3 is in jail
        else:#If player 3 is in jail
            PlayersOnTopRow += "  "#If player 3 is in jail
        if Player1Location == 11 and Player4InJail == 1:#If player 4 is in jail
            PlayersOnTopRow += "4 "#If player 4 is in jail
        else:#If player 4 is in jail
            PlayersOnTopRow += "  "#If player 4 is in jail

            
        PlayersOnTopRow += "     |"
        if Player1Location == 12:#If player 1 is on St. Charles Place
            PlayersOnTopRow += "1 "#If player 1 is on St. Charles Place
        else:#If player 1 is on St. Charles Place
            PlayersOnTopRow += "  "#If player 1 is on St. Charles Place
        if Player2Location == 12:#If player 2 is on St. Charles Place
            PlayersOnTopRow += "2 "#If player 2 is on St. Charles Place
        else:##If player 2 is on St. Charles Place
            PlayersOnTopRow += "  "#If player 2 is on St. Charles Place
        if Player3Location == 12:#If player 3 is on St. Charles Place
            PlayersOnTopRow += "3 "#If player 3 is on St. Charles Place
        else:#If player 3 is on St. Charles Place
            PlayersOnTopRow += "  "#If player 3 is on St. Charles Place
        if Player4Location == 12:#If player 4 is on St. Charles Place
            PlayersOnTopRow += "4 "#If player 4 is on St. Charles Place
        else:#If player 4 is on St. Charles Place
            PlayersOnTopRow += "  "#If player 4 is on St. Charles Place

            
        PlayersOnTopRow += "     |"
        if Player1Location == 13:#If player 1 is on Electric Company
            PlayersOnTopRow += "1 "#If player 1 is on Electric Company
        else:#If player 1 is on Electric Company
            PlayersOnTopRow += "  "#If player 1 is on Electric Company
        if Player2Location == 13:#If player 2 is on Electric Company
            PlayersOnTopRow += "2 "#If player 2 is on Electric Company
        else:##If player 2 is on Electric Company
            PlayersOnTopRow += "  "#If player 2 is on Electric Company
        if Player3Location == 13:#If player 3 is on Electric Company
            PlayersOnTopRow += "3 "#If player 3 is on Electric Company
        else:#If player 3 is on Electric Company
            PlayersOnTopRow += "  "#If player 3 is on Electric Company
        if Player4Location == 13:#If player 4 is on Electric Company
            PlayersOnTopRow += "4 "#If player 4 is on Electric Company
        else:#If player 4 is on Electric Company
            PlayersOnTopRow += "  "#If player 4 is on Electric Company

            
        PlayersOnTopRow += "     |"
        if Player1Location == 14:#If player 1 is on States Ave.
            PlayersOnTopRow += "1 "#If player 1 is on States Ave.
        else:#If player 1 is on States Ave.
            PlayersOnTopRow += "  "#If player 1 is on States Ave.
        if Player2Location == 14:#If player 2 is on States Ave.
            PlayersOnTopRow += "2 "#If player 2 is on States Ave.
        else:##If player 2 is on States Ave.
            PlayersOnTopRow += "  "#If player 2 is on States Ave.
        if Player3Location == 14:#If player 3 is on States Ave.
            PlayersOnTopRow += "3 "#If player 3 is on States Ave.
        else:#If player 3 is on States Ave.
            PlayersOnTopRow += "  "#If player 3 is on States Ave.
        if Player4Location == 14:#If player 4 is on States Ave.
            PlayersOnTopRow += "4 "#If player 4 is on States Ave.
        else:#If player 4 is on States Ave.
            PlayersOnTopRow += "  "#If player 4 is on States Ave.
            
            
        PlayersOnTopRow += "     |"
        if Player1Location == 15:#If player 1 is on Virginia Ave.
            PlayersOnTopRow += "1 "#If player 1 is on Virginia Ave.
        else:#If player 1 is on Virginia Ave.
            PlayersOnTopRow += "  "#If player 1 is on Virginia Ave.
        if Player2Location == 15:#If player 2 is on Virginia Ave.
            PlayersOnTopRow += "2 "#If player 2 is on Virginia Ave.
        else:##If player 2 is on Virginia Ave.
            PlayersOnTopRow += "  "#If player 2 is on Virginia Ave.
        if Player3Location == 15:#If player 3 is on Virginia Ave.
            PlayersOnTopRow += "3 "#If player 3 is on Virginia Ave.
        else:#If player 3 is on Virginia Ave.
            PlayersOnTopRow += "  "#If player 3 is on Virginia Ave.
        if Player4Location == 15:#If player 4 is on Virginia Ave.
            PlayersOnTopRow += "4 "#If player 4 is on Virginia Ave.
        else:#If player 4 is on Virginia Ave.
            PlayersOnTopRow += "  "#If player 4 is on Virginia Ave.
                 
            
        PlayersOnTopRow += "     |"
        if Player1Location == 16:#If player 1 is on Pennsylvania Railroad
            PlayersOnTopRow += "1 "#If player 1 is on Pennsylvania Railroad
        else:#If player 1 is on Pennsylvania Railroad
            PlayersOnTopRow += "  "#If player 1 is on Pennsylvania Railroad
        if Player2Location == 16:#If player 2 is on Pennsylvania Railroad
            PlayersOnTopRow += "2 "#If player 2 is on Pennsylvania Railroad
        else:##If player 2 is on Pennsylvania Railroad
            PlayersOnTopRow += "  "#If player 2 is on Pennsylvania Railroad
        if Player3Location == 16:#If player 3 is on Pennsylvania Railroad
            PlayersOnTopRow += "3 "#If player 3 is on Pennsylvania Railroad
        else:#If player 3 is on Pennsylvania Railroad
            PlayersOnTopRow += "  "#If player 3 is on Pennsylvania Railroad
        if Player4Location == 16:#If player 4 is on Pennsylvania Railroad
            PlayersOnTopRow += "4 "#If player 4 is on Pennsylvania Railroad
        else:#If player 4 is on Pennsylvania Railroad
            PlayersOnTopRow += "  "#If player 4 is on Pennsylvania Railroad
           
            
        PlayersOnTopRow += "     |"
        if Player1Location == 17:#If player 1 is on St. James Place
            PlayersOnTopRow += "1 "#If player 1 is on St. James Place
        else:#If player 1 is on St. James Place
            PlayersOnTopRow += "  "#If player 1 is on St. James Place
        if Player2Location == 17:#If player 2 is on St. James Place
            PlayersOnTopRow += "2 "#If player 2 is on St. James Place
        else:##If player 2 is on St. James Place
            PlayersOnTopRow += "  "#If player 2 is on St. James Place
        if Player3Location == 17:#If player 3 is on St. James Place
            PlayersOnTopRow += "3 "#If player 3 is on St. James Place
        else:#If player 3 is on St. James Place
            PlayersOnTopRow += "  "#If player 3 is on St. James Place
        if Player4Location == 17:#If player 4 is on St. James Place
            PlayersOnTopRow += "4 "#If player 4 is on St. James Place
        else:#If player 4 is on St. James Place
            PlayersOnTopRow += "  "#If player 4 is on St. James Place
                 
            
        PlayersOnTopRow += "     |"
        if Player1Location == 18:#If player 1 is on Community Chest
            PlayersOnTopRow += "1 "#If player 1 is on Community Chest
        else:#If player 1 is on Community Chest
            PlayersOnTopRow += "  "#If player 1 is on Community Chest
        if Player2Location == 18:#If player 2 is on Community Chest
            PlayersOnTopRow += "2 "#If player 2 is on Community Chest
        else:##If player 2 is on Community Chest
            PlayersOnTopRow += "  "#If player 2 is on Community Chest
        if Player3Location == 18:#If player 3 is on Community Chest
            PlayersOnTopRow += "3 "#If player 3 is on Community Chest
        else:#If player 3 is on Community Chest
            PlayersOnTopRow += "  "#If player 3 is on Community Chest
        if Player4Location == 18:#If player 4 is on Community Chest
            PlayersOnTopRow += "4 "#If player 4 is on Community Chest
        else:#If player 4 is on Community Chest
            PlayersOnTopRow += "  "#If player 4 is on Community Chest
                      
            
        PlayersOnTopRow += "     |"
        if Player1Location == 19:#If player 1 is on Tennessee Ave.
            PlayersOnTopRow += "1 "#If player 1 is on Tennessee Ave.
        else:#If player 1 is on Tennessee Ave.
            PlayersOnTopRow += "  "#If player 1 is on Tennessee Ave.
        if Player2Location == 19:#If player 2 is on Tennessee Ave.
            PlayersOnTopRow += "2 "#If player 2 is on Tennessee Ave.
        else:##If player 2 is on Tennessee Ave.
            PlayersOnTopRow += "  "#If player 2 is on Tennessee Ave.
        if Player3Location == 19:#If player 3 is on Tennessee Ave.
            PlayersOnTopRow += "3 "#If player 3 is on Tennessee Ave.
        else:#If player 3 is on Tennessee Ave.
            PlayersOnTopRow += "  "#If player 3 is on Tennessee Ave.
        if Player4Location == 19:#If player 4 is on Tennessee Ave.
            PlayersOnTopRow += "4 "#If player 4 is on Tennessee Ave.
        else:#If player 4 is on Tennessee Ave.
            PlayersOnTopRow += "  "#If player 4 is on Tennessee Ave.
                          
            
        PlayersOnTopRow += "     |"
        if Player1Location == 20:#If player 1 is on New York Ave.
            PlayersOnTopRow += "1 "#If player 1 is on New York Ave.
        else:#If player 1 is on New York Ave.
            PlayersOnTopRow += "  "#If player 1 is on New York Ave.
        if Player2Location == 20:#If player 2 is on New York Ave.
            PlayersOnTopRow += "2 "#If player 2 is on New York Ave.
        else:##If player 2 is on New York Ave.
            PlayersOnTopRow += "  "#If player 2 is on New York Ave.
        if Player3Location == 20:#If player 3 is on New York Ave.
            PlayersOnTopRow += "3 "#If player 3 is on New York Ave.
        else:#If player 3 is on New York Ave.
            PlayersOnTopRow += "  "#If player 3 is on New York Ave.
        if Player4Location == 20:#If player 4 is on New York Ave.
            PlayersOnTopRow += "4 "#If player 4 is on New York Ave.
        else:#If player 4 is on New York Ave.
            PlayersOnTopRow += "  "#If player 4 is on New York Ave.
                                      
            
        PlayersOnTopRow += "     |"
        if Player1Location == 21:#If player 1 is on Free Parking
            PlayersOnTopRow += "1 "#If player 1 is on Free Parking
        else:#If player 1 is on Free Parking
            PlayersOnTopRow += "  "#If player 1 is on Free Parking
        if Player2Location == 21:#If player 2 is on Free Parking
            PlayersOnTopRow += "2 "#If player 2 is on Free Parking
        else:##If player 2 is on Free Parking
            PlayersOnTopRow += "  "#If player 2 is on Free Parking
        if Player3Location == 21:#If player 3 is on Free Parking
            PlayersOnTopRow += "3 "#If player 3 is on Free Parking
        else:#If player 3 is on Free Parking
            PlayersOnTopRow += "  "#If player 3 is on Free Parking
        if Player4Location == 21:#If player 4 is on Free Parking
            PlayersOnTopRow += "4 "#If player 4 is on Free Parking
        else:#If player 4 is on Free Parking
            PlayersOnTopRow += "  "#If player 4 is on Free Parking
        PlayersOnTopRow += "     |"
        print(PlayersOnTopRow)        
        print('''                |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|
                |Connecticut  |                                                                                                                             |Kentucky Ave.|
                |Ave.         |                                                                                                                             |             |
                |Price - 120  |                                                                                                                             |Price - 220  |''')


        ConnecticutKentucky = "                |"
        if Player1Location == 10:#If player 1 is on Connecticut Ave.
            ConnecticutKentucky += "1 "#If player 1 is on Connecticut Ave.
        else:#If player 1 is on Connecticut Ave.
            ConnecticutKentucky += "  "#If player 1 is on Connecticut Ave.
        if Player2Location == 10:#If player 2 is on Connecticut Ave.
            ConnecticutKentucky += "2 "#If player 2 is on Connecticut Ave.
        else:##If player 2 is on Connecticut Ave.
            ConnecticutKentucky += "  "#If player 2 is on Connecticut Ave.
        if Player3Location == 10:#If player 3 is on Connecticut Ave.
            ConnecticutKentucky += "3 "#If player 3 is on Connecticut Ave.
        else:#If player 3 is on Connecticut Ave.
            ConnecticutKentucky += "  "#If player 3 is on Connecticut Ave.
        if Player4Location == 10:#If player 4 is on Connecticut Ave.
            ConnecticutKentucky += "4 "#If player 4 is on Connecticut Ave.
        else:#If player 4 is on Connecticut Ave.
            ConnecticutKentucky += "  "#If player 4 is on Connecticut Ave.

            
        ConnecticutKentucky += "     |                                                                                                                             |"
        if Player1Location == 22:#If player 1 is on Kentucky Ave.
            ConnecticutKentucky += "1 "#If player 1 is on Kentucky Ave.
        else:#If player 1 is on Kentucky Ave.
            ConnecticutKentucky += "  "#If player 1 is on Kentucky Ave.
        if Player2Location == 22:#If player 2 is on Kentucky Ave.
            ConnecticutKentucky += "2 "#If player 2 is on Kentucky Ave.
        else:##If player 2 is on Kentucky Ave.
            ConnecticutKentucky += "  "#If player 2 is on Kentucky Ave.
        if Player3Location == 22:#If player 3 is on Kentucky Ave.
            ConnecticutKentucky += "3 "#If player 3 is on Kentucky Ave.
        else:#If player 3 is on Kentucky Ave.
            ConnecticutKentucky += "  "#If player 3 is on Kentucky Ave.
        if Player4Location == 22:#If player 4 is on Kentucky Ave.
            ConnecticutKentucky += "4 "#If player 4 is on Kentucky Ave.
        else:#If player 4 is on Kentucky Ave.
            ConnecticutKentucky += "  "#If player 4 is on Kentucky Ave.
        ConnecticutKentucky += "     |"
        print(ConnecticutKentucky)
        print('''                |_____________|                                                                                                                             |_____________|
                |Vermon Ave.  |                                                                                                                             |Chance       |
                |             |                                                                                                                             |             |
                |Price - 100  |                                                                                                                             |             |''')


        VermontChance = "                |"
        if Player1Location == 9:#If player 1 is on Vermont Ave.
            VermontChance += "1 "#If player 1 is on Vermont Ave.
        else:#If player 1 is on Vermont Ave.
            VermontChance += "  "#If player 1 is on Vermont Ave.
        if Player2Location == 9:#If player 2 is on Vermont Ave.
            VermontChance += "2 "#If player 2 is on Vermont Ave.
        else:##If player 2 is on Vermont Ave.
            VermontChance += "  "#If player 2 is on Vermont Ave.
        if Player3Location == 9:#If player 3 is on Vermont Ave.
            VermontChance += "3 "#If player 3 is on Vermont Ave.
        else:#If player 3 is on Vermont Ave.
            VermontChance += "  "#If player 3 is on Vermont Ave.
        if Player4Location == 9:#If player 4 is on Vermont Ave.
            VermontChance += "4 "#If player 4 is on Vermont Ave.
        else:#If player 4 is on Vermont Ave.
            VermontChance += "  "#If player 4 is on Vermont Ave.

            
        VermontChance += "     |                                                                                                                             |"
        if Player1Location == 23:#If player 1 is on Chance
            VermontChance += "1 "#If player 1 is on Chance
        else:#If player 1 is on Chance
            VermontChance += "  "#If player 1 is on Chance
        if Player2Location == 23:#If player 2 is on Chance
            VermontChance += "2 "#If player 2 is on Chance
        else:##If player 2 is on Chance
            VermontChance += "  "#If player 2 is on Chance
        if Player3Location == 23:#If player 3 is on Chance
            VermontChance += "3 "#If player 3 is on Chance
        else:#If player 3 is on Chance
            VermontChance += "  "#If player 3 is on Chance
        if Player4Location == 23:#If player 4 is on Chance
            VermontChance += "4 "#If player 4 is on Chance
        else:#If player 4 is on Chance
            VermontChance += "  "#If player 4 is on Chance
        VermontChance += "     |"
        print(VermontChance)
        print('''                |_____________|                                                                                                                             |_____________|
                |Chance       |                                                                                                                             |Indiana Ave. |
                |             |                                                                                                                             |             |
                |             |                                                                                                                             |Price - 220  |''')


        ChanceIndiana = "                |"
        if Player1Location == 8:#If player 1 is on Chance
            ChanceIndiana += "1 "#If player 1 is on Chance
        else:#If player 1 is on Chance
            ChanceIndiana += "  "#If player 1 is on Chance
        if Player2Location == 8:#If player 2 is on Chance
            ChanceIndiana += "2 "#If player 2 is on Chance
        else:##If player 2 is on Chance
            ChanceIndiana += "  "#If player 2 is on Chance
        if Player3Location == 8:#If player 3 is on Chance
            ChanceIndiana += "3 "#If player 3 is on Chance
        else:#If player 3 is on Chance
            ChanceIndiana += "  "#If player 3 is on Chance
        if Player4Location == 8:#If player 4 is on Chance
            ChanceIndiana += "4 "#If player 4 is on Chance
        else:#If player 4 is on Chance
            ChanceIndiana += "  "#If player 4 is on Chance

            
        ChanceIndiana += "     |                                                                                                                             |"
        if Player1Location == 24:#If player 1 is on Indiana Ave.
            ChanceIndiana += "1 "#If player 1 is on Indiana Ave.
        else:#If player 1 is on Indiana Ave.
            ChanceIndiana += "  "#If player 1 is on Indiana Ave.
        if Player2Location == 24:#If player 2 is on Indiana Ave.
            ChanceIndiana += "2 "#If player 2 is on Indiana Ave.
        else:##If player 2 is on Indiana Ave.
            ChanceIndiana += "  "#If player 2 is on Indiana Ave.
        if Player3Location == 24:#If player 3 is on Indiana Ave.
            ChanceIndiana += "3 "#If player 3 is on Indiana Ave.
        else:#If player 3 is on Indiana Ave.
            ChanceIndiana += "  "#If player 3 is on Indiana Ave.
        if Player4Location == 24:#If player 4 is on Indiana Ave.
            ChanceIndiana += "4 "#If player 4 is on Indiana Ave.
        else:#If player 4 is on Indiana Ave.
            ChanceIndiana += "  "#If player 4 is on Indiana Ave.
        ChanceIndiana += "     |"
        print(ChanceIndiana)
        print('''                |_____________|                                                                                                                             |_____________|
                |Oriental Ave.|                                                                                                                             |Illinois Ave.|
                |             |                                                                                                                             |             |
                |Price - 100  |                                                                                                                             |Price - 240  |''')


        OrientalIllinois  = "                |"
        if Player1Location == 7:#If player 1 is on Oriental Ave.
            OrientalIllinois += "1 "#If player 1 is on Oriental Ave.
        else:#If player 1 is on Oriental Ave.
            OrientalIllinois += "  "#If player 1 is on Oriental Ave.
        if Player2Location == 7:#If player 2 is on Oriental Ave.
            OrientalIllinois += "2 "#If player 2 is on Oriental Ave.
        else:##If player 2 is on Oriental Ave.
            OrientalIllinois += "  "#If player 2 is on Oriental Ave.
        if Player3Location == 7:#If player 3 is on Oriental Ave.
            OrientalIllinois += "3 "#If player 3 is on Oriental Ave.
        else:#If player 3 is on Oriental Ave.
            OrientalIllinois += "  "#If player 3 is on Oriental Ave.
        if Player4Location == 7:#If player 4 is on Oriental Ave.
            OrientalIllinois += "4 "#If player 4 is on Oriental Ave.
        else:#If player 4 is on Oriental Ave.
            OrientalIllinois += "  "#If player 4 is on Oriental Ave.

            
        OrientalIllinois += "     |                                                                                                                             |"
        if Player1Location == 25:#If player 1 is on Illinois  Ave.
            OrientalIllinois += "1 "#If player 1 is on Illinois  Ave.
        else:#If player 1 is on Illinois  Ave.
            OrientalIllinois += "  "#If player 1 is on Illinois  Ave.
        if Player2Location == 25:#If player 2 is on Illinois  Ave.
            OrientalIllinois += "2 "#If player 2 is on Illinois  Ave.
        else:##If player 2 is on Illinois  Ave.
            OrientalIllinois += "  "#If player 2 is on Illinois  Ave.
        if Player3Location == 25:#If player 3 is on Illinois  Ave.
            OrientalIllinois += "3 "#If player 3 is on Illinois  Ave.
        else:#If player 3 is on Illinois  Ave.
            OrientalIllinois += "  "#If player 3 is on Illinois  Ave.
        if Player4Location == 25:#If player 4 is on Illinois  Ave.
            OrientalIllinois += "4 "#If player 4 is on Illinois  Ave.
        else:#If player 4 is on Illinois  Ave.
            OrientalIllinois += "  "#If player 4 is on Illinois  Ave.
        OrientalIllinois += "     |"
        print(OrientalIllinois)
        print('''                |_____________|                                                                                                                             |_____________|
                |Reading      |                                                                                                                             |B. & O.      |
                |Railroad     |                                                                                                                             |Railroad     |
                |Price - 200  |                                                                                                                             |Price - 200  |''')


        ReadingBO  = "                |"
        if Player1Location == 6:#If player 1 is on Reading Railroad
            ReadingBO += "1 "#If player 1 is on Reading Railroad
        else:#If player 1 is on Reading Railroad
            ReadingBO += "  "#If player 1 is on Reading Railroad
        if Player2Location == 6:#If player 2 is on Reading Railroad
            ReadingBO += "2 "#If player 2 is on Reading Railroad
        else:##If player 2 is on Reading Railroad
            ReadingBO += "  "#If player 2 is on Reading Railroad
        if Player3Location == 6:#If player 3 is on Reading Railroad
            ReadingBO += "3 "#If player 3 is on Reading Railroad
        else:#If player 3 is on Reading Railroad
            ReadingBO += "  "#If player 3 is on Reading Railroad
        if Player4Location == 6:#If player 4 is on Reading Railroad
            ReadingBO += "4 "#If player 4 is on Reading Railroad
        else:#If player 4 is on Reading Railroad
            ReadingBO += "  "#If player 4 is on Reading Railroad

            
        ReadingBO += "     |                                                                                                                             |"
        if Player1Location == 26:#If player 1 is on B. & O. Railroad
            ReadingBO += "1 "#If player 1 is on B. & O. Railroad
        else:#If player 1 is on B. & O. Railroad
            ReadingBO += "  "#If player 1 is on B. & O. Railroad
        if Player2Location == 26:#If player 2 is on B. & O. Railroad
            ReadingBO += "2 "#If player 2 is on B. & O. Railroad
        else:##If player 2 is on B. & O. Railroad
            ReadingBO += "  "#If player 2 is on B. & O. Railroad
        if Player3Location == 26:#If player 3 is on B. & O. Railroad
            ReadingBO += "3 "#If player 3 is on B. & O. Railroad
        else:#If player 3 is on B. & O. Railroad
            ReadingBO += "  "#If player 3 is on B. & O. Railroad
        if Player4Location == 26:#If player 4 is on B. & O. Railroad
            ReadingBO += "4 "#If player 4 is on B. & O. Railroad
        else:#If player 4 is on B. & O. Railroad
            ReadingBO += "  "#If player 4 is on B. & O. Railroad
        ReadingBO += "     |"
        print(ReadingBO)
        print('''                |_____________|                                                                                                                             |_____________|
                |Income Tax   |                                                                                                                             |Atlantic Ave.|
                |             |                                                                                                                             |             |
                |             |                                                                                                                             |Price - 260  |''')


        IncomeAtlantic = "                |"
        if Player1Location == 5:#If player 1 is on Income Tax
            IncomeAtlantic += "1 "#If player 1 is on Income Tax
        else:#If player 1 is on Income Tax
            IncomeAtlantic += "  "#If player 1 is on Income Tax
        if Player2Location == 5:#If player 2 is on Income Tax
            IncomeAtlantic += "2 "#If player 2 is on Income Tax
        else:##If player 2 is on Income Tax
            IncomeAtlantic += "  "#If player 2 is on Income Tax
        if Player3Location == 5:#If player 3 is on Income Tax
            IncomeAtlantic += "3 "#If player 3 is on Income Tax
        else:#If player 3 is on Income Tax
            IncomeAtlantic += "  "#If player 3 is on Income Tax
        if Player4Location == 5:#If player 4 is on Income Tax
            IncomeAtlantic += "4 "#If player 4 is on Income Tax
        else:#If player 4 is on Income Tax
            IncomeAtlantic += "  "#If player 4 is on Income Tax

            
        IncomeAtlantic += "     |                                                                                                                             |"
        if Player1Location == 27:#If player 1 is on Atlantic Ave.
            IncomeAtlantic += "1 "#If player 1 is on Atlantic Ave.
        else:#If player 1 is on Atlantic Ave.
            IncomeAtlantic += "  "#If player 1 is on Atlantic Ave.
        if Player2Location == 27:#If player 2 is on Atlantic Ave.
            IncomeAtlantic += "2 "#If player 2 is on Atlantic Ave.
        else:##If player 2 is on Atlantic Ave.
            IncomeAtlantic += "  "#If player 2 is on Atlantic Ave.
        if Player3Location == 27:#If player 3 is on Atlantic Ave.
            IncomeAtlantic += "3 "#If player 3 is on Atlantic Ave.
        else:#If player 3 is on Atlantic Ave.
            IncomeAtlantic += "  "#If player 3 is on Atlantic Ave.
        if Player4Location == 27:#If player 4 is on Atlantic Ave.
            IncomeAtlantic += "4 "#If player 4 is on Atlantic Ave.
        else:#If player 4 is on Atlantic Ave.
            IncomeAtlantic += "  "#If player 4 is on Atlantic Ave.
        IncomeAtlantic += "     |"
        print(IncomeAtlantic)
        print('''                |_____________|                                                                                                                             |_____________|
                |Baltic Ave.  |                                                                                                                             |Ventnor      |
                |             |                                                                                                                             |Ave.         |
                |Price - 60   |                                                                                                                             |Price - 260  |''')
        

        BalticVentnor = "                |"
        if Player1Location == 4:#If player 1 is on Baltic Ave.
            BalticVentnor += "1 "#If player 1 is on Baltic Ave.
        else:#If player 1 is on Baltic Ave.
            BalticVentnor += "  "#If player 1 is on Baltic Ave.
        if Player2Location == 4:#If player 2 is on Baltic Ave.
            BalticVentnor += "2 "#If player 2 is on Baltic Ave.
        else:##If player 2 is on Baltic Ave.
            BalticVentnor += "  "#If player 2 is on Baltic Ave.
        if Player3Location == 4:#If player 3 is on Baltic Ave.
            BalticVentnor += "3 "#If player 3 is on Baltic Ave.
        else:#If player 3 is on Baltic Ave.
            BalticVentnor += "  "#If player 3 is on Baltic Ave.
        if Player4Location == 4:#If player 4 is on Baltic Ave.
            BalticVentnor += "4 "#If player 4 is on Baltic Ave.
        else:#If player 4 is on Baltic Ave.
            BalticVentnor += "  "#If player 4 is on Baltic Ave.

            
        BalticVentnor += "     |                                                                                                                             |"
        if Player1Location == 28:#If player 1 is on Ventnor  Ave.
            BalticVentnor += "1 "#If player 1 is on Ventnor  Ave.
        else:#If player 1 is on Ventnor  Ave.
            BalticVentnor += "  "#If player 1 is on Ventnor  Ave.
        if Player2Location == 28:#If player 2 is on Ventnor  Ave.
            BalticVentnor += "2 "#If player 2 is on Ventnor  Ave.
        else:##If player 2 is on Ventnor  Ave.
            BalticVentnor += "  "#If player 2 is on Ventnor  Ave.
        if Player3Location == 28:#If player 3 is on Ventnor  Ave.
            BalticVentnor += "3 "#If player 3 is on Ventnor  Ave.
        else:#If player 3 is on Ventnor  Ave.
            BalticVentnor += "  "#If player 3 is on Ventnor  Ave.
        if Player4Location == 28:#If player 4 is on Ventnor  Ave.
            BalticVentnor += "4 "#If player 4 is on Ventnor  Ave.
        else:#If player 4 is on Ventnor  Ave.
            BalticVentnor += "  "#If player 4 is on Ventnor  Ave.
        BalticVentnor += "     |"
        print(BalticVentnor)
        print('''                |_____________|                                                                                                                             |_____________|
                |Community    |                                                                                                                             |Water Works  |
                |Chest        |                                                                                                                             |             |
                |             |                                                                                                                             |Price - 150  |''')


        CommunityWater = "                |"
        if Player1Location == 3:#If player 1 is on Community Chest
            CommunityWater += "1 "#If player 1 is on Community Chest
        else:#If player 1 is on Community Chest
            CommunityWater += "  "#If player 1 is on Community Chest
        if Player2Location == 3:#If player 2 is on Community Chest
            CommunityWater += "2 "#If player 2 is on Community Chest
        else:##If player 2 is on Community Chest
            CommunityWater += "  "#If player 2 is on Community Chest
        if Player3Location == 3:#If player 3 is on Community Chest
            CommunityWater += "3 "#If player 3 is on Community Chest
        else:#If player 3 is on Community Chest
            CommunityWater += "  "#If player 3 is on Community Chest
        if Player4Location == 3:#If player 4 is on Community Chest
            CommunityWater += "4 "#If player 4 is on Community Chest
        else:#If player 4 is on Community Chest
            CommunityWater += "  "#If player 4 is on Community Chest

            
        CommunityWater += "     |                                                                                                                             |"
        if Player1Location == 29:#If player 1 is on Water Works
            CommunityWater += "1 "#If player 1 is on Water Works
        else:#If player 1 is on Water Works
            CommunityWater += "  "#If player 1 is on Water Works
        if Player2Location == 29:#If player 2 is on Water Works
            CommunityWater += "2 "#If player 2 is on Water Works
        else:##If player 2 is on Water Works
            CommunityWater += "  "#If player 2 is on Water Works
        if Player3Location == 29:#If player 3 is on Water Works
            CommunityWater += "3 "#If player 3 is on Water Works
        else:#If player 3 is on Water Works
            CommunityWater += "  "#If player 3 is on Water Works
        if Player4Location == 29:#If player 4 is on Water Works
            CommunityWater += "4 "#If player 4 is on Water Works
        else:#If player 4 is on Water Works
            CommunityWater += "  "#If player 4 is on Water Works
        CommunityWater += "     |"
        print(CommunityWater)
        print('''                |_____________|                                                                                                                             |_____________|
                |Mediterranean|                                                                                                                             |Marvin       |
                |Ave.         |                                                                                                                             |Gardens      |
                |Price - 60   |                                                                                                                             |Price - 280  |''')
        

        MediterraneanMarvin  = "                |"
        if Player1Location == 2:#If player 1 is on Mediterranean Ave.
            MediterraneanMarvin += "1 "#If player 1 is on Mediterranean Ave.
        else:#If player 1 is on Mediterranean Ave.
            MediterraneanMarvin += "  "#If player 1 is on Mediterranean Ave.
        if Player2Location == 2:#If player 2 is on Mediterranean Ave.
            MediterraneanMarvin += "2 "#If player 2 is on Mediterranean Ave.
        else:##If player 2 is on Mediterranean Ave.
            MediterraneanMarvin += "  "#If player 2 is on Mediterranean Ave.
        if Player3Location == 2:#If player 3 is on Mediterranean Ave.
            MediterraneanMarvin += "3 "#If player 3 is on Mediterranean Ave.
        else:#If player 3 is on Mediterranean Ave.
            MediterraneanMarvin += "  "#If player 3 is on Mediterranean Ave.
        if Player4Location == 2:#If player 4 is on Mediterranean Ave.
            MediterraneanMarvin += "4 "#If player 4 is on Mediterranean Ave.
        else:#If player 4 is on Mediterranean Ave.
            MediterraneanMarvin += "  "#If player 4 is on Mediterranean Ave.

            
        MediterraneanMarvin += "     |                                                                                                                             |"
        if Player1Location == 30:#If player 1 is on Marvin Gardens
            MediterraneanMarvin += "1 "#If player 1 is on Marvin Gardens
        else:#If player 1 is on Marvin Gardens
            MediterraneanMarvin += "  "#If player 1 is on Marvin Gardens
        if Player2Location == 30:#If player 2 is on Marvin Gardens
            MediterraneanMarvin += "2 "#If player 2 is on Marvin Gardens
        else:##If player 2 is on Marvin Gardens
            MediterraneanMarvin += "  "#If player 2 is on Marvin Gardens
        if Player3Location == 30:#If player 3 is on Marvin Gardens
            MediterraneanMarvin += "3 "#If player 3 is on Marvin Gardens
        else:#If player 3 is on Marvin Gardens
            MediterraneanMarvin += "  "#If player 3 is on Marvin Gardens
        if Player4Location == 30:#If player 4 is on Marvin Gardens
            MediterraneanMarvin += "4 "#If player 4 is on Marvin Gardens
        else:#If player 4 is on Marvin Gardens
            MediterraneanMarvin += "  "#If player 4 is on Marvin Gardens
        MediterraneanMarvin += "     |"
        print(MediterraneanMarvin)
        print('''                |_____________|_____________________________________________________________________________________________________________________________|_____________|
                |Go           |Boardwalk    |Luxury Tax   |Park place   |Chance       |Short Line   |Pennsylvania |Community    |North        |Pacific Ave. |Go To Jail   |
                |             |             |             |             |             |Railroad     |Ave.         |Chest        |Carolina Ave.|             |             |
                |             |Price - 400  |             |Price - 350  |             |Price - 200  |Price - 320  |             |Price - 300  |Price - 300  |             |''')
        PlayersOnBottomRow = "                |"#If Players are in the top row
        if Player1Location == 1:#If player 1 is in jail
            PlayersOnBottomRow += "1 "#If player 1 is in jail
        else:#If player 1 is in jail
            PlayersOnBottomRow += "  "#If player 1 is in jail
        if Player2Location == 1:#If player 2 is in jail
            PlayersOnBottomRow += "2 "#If player 2 is in jail
        else:#If player 2 is in jail
            PlayersOnBottomRow += "  "#If player 2 is in jail
        if Player3Location == 1:#If player 3 is in jail
            PlayersOnBottomRow += "3 "#If player 3 is in jail
        else:#If player 3 is in jail
            PlayersOnBottomRow += "  "#If player 3 is in jail
        if Player4Location == 1:#If player 4 is in jail
            PlayersOnBottomRow += "4 "#If player 4 is in jail
        else:#If player 4 is in jail
            PlayersOnBottomRow += "  "#If player 4 is in jail

            
        PlayersOnBottomRow += "     |"
        if Player1Location == 40:#If player 1 is on St. Charles Place
            PlayersOnBottomRow += "1 "#If player 1 is on St. Charles Place
        else:#If player 1 is on St. Charles Place
            PlayersOnBottomRow += "  "#If player 1 is on St. Charles Place
        if Player2Location == 40:#If player 2 is on St. Charles Place
            PlayersOnBottomRow += "2 "#If player 2 is on St. Charles Place
        else:##If player 2 is on St. Charles Place
            PlayersOnBottomRow += "  "#If player 2 is on St. Charles Place
        if Player3Location == 40:#If player 3 is on St. Charles Place
            PlayersOnBottomRow += "3 "#If player 3 is on St. Charles Place
        else:#If player 3 is on St. Charles Place
            PlayersOnBottomRow += "  "#If player 3 is on St. Charles Place
        if Player4Location == 40:#If player 4 is on St. Charles Place
            PlayersOnBottomRow += "4 "#If player 4 is on St. Charles Place
        else:#If player 4 is on St. Charles Place
            PlayersOnBottomRow += "  "#If player 4 is on St. Charles Place

            
        PlayersOnBottomRow += "     |"
        if Player1Location == 39:#If player 1 is on Electric Company
            PlayersOnBottomRow += "1 "#If player 1 is on Electric Company
        else:#If player 1 is on Electric Company
            PlayersOnBottomRow += "  "#If player 1 is on Electric Company
        if Player2Location == 39:#If player 2 is on Electric Company
            PlayersOnBottomRow += "2 "#If player 2 is on Electric Company
        else:##If player 2 is on Electric Company
            PlayersOnBottomRow += "  "#If player 2 is on Electric Company
        if Player3Location == 39:#If player 3 is on Electric Company
            PlayersOnBottomRow += "3 "#If player 3 is on Electric Company
        else:#If player 3 is on Electric Company
            PlayersOnBottomRow += "  "#If player 3 is on Electric Company
        if Player4Location == 39:#If player 4 is on Electric Company
            PlayersOnBottomRow += "4 "#If player 4 is on Electric Company
        else:#If player 4 is on Electric Company
            PlayersOnBottomRow += "  "#If player 4 is on Electric Company

            
        PlayersOnBottomRow += "     |"
        if Player1Location == 38:#If player 1 is on States Ave.
            PlayersOnBottomRow += "1 "#If player 1 is on States Ave.
        else:#If player 1 is on States Ave.
            PlayersOnBottomRow += "  "#If player 1 is on States Ave.
        if Player2Location == 38:#If player 2 is on States Ave.
            PlayersOnBottomRow += "2 "#If player 2 is on States Ave.
        else:##If player 2 is on States Ave.
            PlayersOnBottomRow += "  "#If player 2 is on States Ave.
        if Player3Location == 38:#If player 3 is on States Ave.
            PlayersOnBottomRow += "3 "#If player 3 is on States Ave.
        else:#If player 3 is on States Ave.
            PlayersOnBottomRow += "  "#If player 3 is on States Ave.
        if Player4Location == 38:#If player 4 is on States Ave.
            PlayersOnBottomRow += "4 "#If player 4 is on States Ave.
        else:#If player 4 is on States Ave.
            PlayersOnBottomRow += "  "#If player 4 is on States Ave.
            
            
        PlayersOnBottomRow += "     |"
        if Player1Location == 37:#If player 1 is on Virginia Ave.
            PlayersOnBottomRow += "1 "#If player 1 is on Virginia Ave.
        else:#If player 1 is on Virginia Ave.
            PlayersOnBottomRow += "  "#If player 1 is on Virginia Ave.
        if Player2Location == 37:#If player 2 is on Virginia Ave.
            PlayersOnBottomRow += "2 "#If player 2 is on Virginia Ave.
        else:##If player 2 is on Virginia Ave.
            PlayersOnBottomRow += "  "#If player 2 is on Virginia Ave.
        if Player3Location == 37:#If player 3 is on Virginia Ave.
            PlayersOnBottomRow += "3 "#If player 3 is on Virginia Ave.
        else:#If player 3 is on Virginia Ave.
            PlayersOnBottomRow += "  "#If player 3 is on Virginia Ave.
        if Player4Location == 37:#If player 4 is on Virginia Ave.
            PlayersOnBottomRow += "4 "#If player 4 is on Virginia Ave.
        else:#If player 4 is on Virginia Ave.
            PlayersOnBottomRow += "  "#If player 4 is on Virginia Ave.
                 
            
        PlayersOnBottomRow += "     |"
        if Player1Location == 36:#If player 1 is on Pennsylvania Railroad
            PlayersOnBottomRow += "1 "#If player 1 is on Pennsylvania Railroad
        else:#If player 1 is on Pennsylvania Railroad
            PlayersOnBottomRow += "  "#If player 1 is on Pennsylvania Railroad
        if Player2Location == 36:#If player 2 is on Pennsylvania Railroad
            PlayersOnBottomRow += "2 "#If player 2 is on Pennsylvania Railroad
        else:##If player 2 is on Pennsylvania Railroad
            PlayersOnBottomRow += "  "#If player 2 is on Pennsylvania Railroad
        if Player3Location == 36:#If player 3 is on Pennsylvania Railroad
            PlayersOnBottomRow += "3 "#If player 3 is on Pennsylvania Railroad
        else:#If player 3 is on Pennsylvania Railroad
            PlayersOnBottomRow += "  "#If player 3 is on Pennsylvania Railroad
        if Player4Location == 36:#If player 4 is on Pennsylvania Railroad
            PlayersOnBottomRow += "4 "#If player 4 is on Pennsylvania Railroad
        else:#If player 4 is on Pennsylvania Railroad
            PlayersOnBottomRow += "  "#If player 4 is on Pennsylvania Railroad
           
            
        PlayersOnBottomRow += "     |"
        if Player1Location == 35:#If player 1 is on St. James Place
            PlayersOnBottomRow += "1 "#If player 1 is on St. James Place
        else:#If player 1 is on St. James Place
            PlayersOnBottomRow += "  "#If player 1 is on St. James Place
        if Player2Location == 35:#If player 2 is on St. James Place
            PlayersOnBottomRow += "2 "#If player 2 is on St. James Place
        else:##If player 2 is on St. James Place
            PlayersOnBottomRow += "  "#If player 2 is on St. James Place
        if Player3Location == 35:#If player 3 is on St. James Place
            PlayersOnBottomRow += "3 "#If player 3 is on St. James Place
        else:#If player 3 is on St. James Place
            PlayersOnBottomRow += "  "#If player 3 is on St. James Place
        if Player4Location == 35:#If player 4 is on St. James Place
            PlayersOnBottomRow += "4 "#If player 4 is on St. James Place
        else:#If player 4 is on St. James Place
            PlayersOnBottomRow += "  "#If player 4 is on St. James Place
                 
            
        PlayersOnBottomRow += "     |"
        if Player1Location == 34:#If player 1 is on Community Chest
            PlayersOnBottomRow += "1 "#If player 1 is on Community Chest
        else:#If player 1 is on Community Chest
            PlayersOnBottomRow += "  "#If player 1 is on Community Chest
        if Player2Location == 34:#If player 2 is on Community Chest
            PlayersOnBottomRow += "2 "#If player 2 is on Community Chest
        else:##If player 2 is on Community Chest
            PlayersOnBottomRow += "  "#If player 2 is on Community Chest
        if Player3Location == 34:#If player 3 is on Community Chest
            PlayersOnBottomRow += "3 "#If player 3 is on Community Chest
        else:#If player 3 is on Community Chest
            PlayersOnBottomRow += "  "#If player 3 is on Community Chest
        if Player4Location == 34:#If player 4 is on Community Chest
            PlayersOnBottomRow += "4 "#If player 4 is on Community Chest
        else:#If player 4 is on Community Chest
            PlayersOnBottomRow += "  "#If player 4 is on Community Chest
                      
            
        PlayersOnBottomRow += "     |"
        if Player1Location == 33:#If player 1 is on Tennessee Ave.
            PlayersOnBottomRow += "1 "#If player 1 is on Tennessee Ave.
        else:#If player 1 is on Tennessee Ave.
            PlayersOnBottomRow += "  "#If player 1 is on Tennessee Ave.
        if Player2Location == 33:#If player 2 is on Tennessee Ave.
            PlayersOnBottomRow += "2 "#If player 2 is on Tennessee Ave.
        else:##If player 2 is on Tennessee Ave.
            PlayersOnBottomRow += "  "#If player 2 is on Tennessee Ave.
        if Player3Location == 33:#If player 3 is on Tennessee Ave.
            PlayersOnBottomRow += "3 "#If player 3 is on Tennessee Ave.
        else:#If player 3 is on Tennessee Ave.
            PlayersOnBottomRow += "  "#If player 3 is on Tennessee Ave.
        if Player4Location == 33:#If player 4 is on Tennessee Ave.
            PlayersOnBottomRow += "4 "#If player 4 is on Tennessee Ave.
        else:#If player 4 is on Tennessee Ave.
            PlayersOnBottomRow += "  "#If player 4 is on Tennessee Ave.
                          
            
        PlayersOnBottomRow += "     |"
        if Player1Location == 32:#If player 1 is on New York Ave.
            PlayersOnBottomRow += "1 "#If player 1 is on New York Ave.
        else:#If player 1 is on New York Ave.
            PlayersOnBottomRow += "  "#If player 1 is on New York Ave.
        if Player2Location == 32:#If player 2 is on New York Ave.
            PlayersOnBottomRow += "2 "#If player 2 is on New York Ave.
        else:##If player 2 is on New York Ave.
            PlayersOnBottomRow += "  "#If player 2 is on New York Ave.
        if Player3Location == 32:#If player 3 is on New York Ave.
            PlayersOnBottomRow += "3 "#If player 3 is on New York Ave.
        else:#If player 3 is on New York Ave.
            PlayersOnBottomRow += "  "#If player 3 is on New York Ave.
        if Player4Location == 32:#If player 4 is on New York Ave.
            PlayersOnBottomRow += "4 "#If player 4 is on New York Ave.
        else:#If player 4 is on New York Ave.
            PlayersOnBottomRow += "  "#If player 4 is on New York Ave.
                                      
            
        PlayersOnBottomRow += "     |"
        if Player1Location == 31:#If player 1 is on Free Parking
            PlayersOnBottomRow += "1 "#If player 1 is on Free Parking
        else:#If player 1 is on Free Parking
            PlayersOnBottomRow += "  "#If player 1 is on Free Parking
        if Player2Location == 31:#If player 2 is on Free Parking
            PlayersOnBottomRow += "2 "#If player 2 is on Free Parking
        else:##If player 2 is on Free Parking
            PlayersOnBottomRow += "  "#If player 2 is on Free Parking
        if Player3Location == 31:#If player 3 is on Free Parking
            PlayersOnBottomRow += "3 "#If player 3 is on Free Parking
        else:#If player 3 is on Free Parking
            PlayersOnBottomRow += "  "#If player 3 is on Free Parking
        if Player4Location == 31:#If player 4 is on Free Parking
            PlayersOnTopRow += "4 "#If player 4 is on Free Parking
        else:#If player 4 is on Free Parking
            PlayersOnBottomRow += "  "#If player 4 is on Free Parking
        PlayersOnBottomRow += "     |"
        print(PlayersOnBottomRow)    
        print('''                |_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|_____________|''')
        print("Player 1 - " + str(Player1Money))
        print("Player 2 - " + str(Player2Money))
        if Player3Location != 99999:
            print("Player 3 - " + str(Player3Money))
        if Player4Location != 99999:
            print("Player 4 - " + str(Player4Money))
        print("Free Parking amount - " + str(FreeParkingMoney))













def HowManyPlayers():
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
        rollOne = random.randint(1, 6)
        rollTwo = random.randint(1, 6)
        return rollOne + rollTwo

















def GameOver():
    if Player1Money < 0:
        print("Player 1 has no more money.")
        if Player2Money > Player3Money and Player2Money > Player4Money:
            print("Player 2 has the most money, Player 2 is the winner.")
        elif Player3Money > Player2Money and Player3Money > Player4Money:
            print("Player 3 has the most money, Player 3 is the winner.")
        else:
            print("Player 4 has the most money, Player 4 is the winner.")
        sys.exit(0)
    elif Player2Money < 0:
        print("Player 2 has no more money.")
        if Player1Money > Player3Money and Player1Money > Player4Money:
            print("Player 1 has the most money, Player 1 is the winner.")
        elif Player3Money > Player1Money and Player3Money > Player4Money:
            print("Player 3 has the most money, Player 3 is the winner.")
        else:
            print("Player 4 has the most money, Player 4 is the winner.")
        sys.exit(0)
    elif Player3Money < 0:
        print("Player 3 has no more money.")
        if Player1Money > Player2Money and Player1Money > Player4Money:
            print("Player 1 has the most money, Player 1 is the winner.")
        elif Player2Money > Player1Money and Player2Money > Player4Money:
            print("Player 2 has the most money, Player 2 is the winner.")
        else:
            print("Player 4 has the most money, Player 4 is the winner.")
        sys.exit(0)
    elif Player4Money < 0:
        print("Player 4 has no more money.")
        if Player1Money > Player2Money and Player1Money > Player3Money:
            print("Player 1 has the most money, Player 1 is the winner.")
        elif Player2Money > Player1Money and Player2Money > Player3Money:
            print("Player 2 has the most money, Player 2 is the winner.")
        else:
            print("Player 3 has the most money, Player 3 is the winner.")
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
            print("Player 1 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player1Money < list2[LandedOn]:
                    print("You don't have enouge money to pay " + str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes':
                    list3[LandedOn] = 1
                    Player1Money -= list2[LandedOn]
                    break
                elif Answer == 'no':
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
            print("Player 2 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player2Money < list2[LandedOn]:
                    print("You don't have enouge money to pay " + str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes':
                    list3[LandedOn] = 2
                    Player2Money -= list2[LandedOn]
                    break
                elif Answer == 'no':
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
            print("Player 3 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player3Money < list2[LandedOn]:
                    print("You don't have enouge money to pay "+str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes':
                    list3[LandedOn] = 3
                    Player3Money -= list2[LandedOn]
                    break
                elif Answer == 'no':
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
            print("Player 4 has landed on "+str(list1[LandedOn])+"\nWould you like to buy it for $"+str(list2[LandedOn])+" (Yes/No)(Rent - "+str(list4[LandedOn])+").")
            while True:
                if Player4Money < list2[LandedOn]:
                    print("You don't have enouge money to pay "+str(list1[LandedOn]))
                    break
                Answer = input().lower()
                if Answer == 'yes':
                    list3[LandedOn] = 4
                    Player4Money -= list2[LandedOn]
                    break
                elif Answer == 'no':
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
    '''global MediterraneanAve
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
    global NewYorkAve'''
    global list4
    global FreeParkingMoney
    '''global KentuckyAve
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
    global BoardwalkRent'''
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
                    #print("Player 1 has landed on the Electric Company. (Press Enter)")
                    UseTheList(26, WhosThis)
                    #input()
            elif WhosThis == 2:
                    #print("Player 2 has landed on the Electric Company. (Press Enter)")
                    UseTheList(26, WhosThis)
                    #input()
            elif WhosThis == 3:
                    #print("Player 3 has landed on the Electric Company. (Press Enter)")
                    UseTheList(26, WhosThis)
                    #input()
            else:
                    #print("Player 4 has landed on the Electric Company. (Press Enter)")
                    UseTheList(26, WhosThis)
                    #input()


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
        for x in range(0, 26):
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
                        for x in range(0, 26):
                                 if list3[x] == StarterOfTrade:
                                         print(list1[x])
                                         
                        print("And player " + str(WhoTheyWantToTrade) + " can trade...")
                        for x in range(0, 26):
                                 if list3[x] == WhoTheyWantToTrade:
                                         print(list1[x])
                        print("(Type finish when you're done. If you type the same place again, it will trade back the places to the original owner.)")                 
                        while True:
                                #list1 = ["Mediterranean Ave.", "Baltic Ave.", "Oriental Ave.", "Vermont Ave.", "Connecticut Ave.", "St. Charles Place", "States Ave.", "Virginia Ave.","St. James Place", "Tennessee Ave.", "New York Ave.", "Kentucky Ave.","Indiana Ave.","Illinois Ave.","Atlantic Ave.","Ventnor Ave.", "Marvin Gardens", "Pacific Ave.", "North Carolina Ave.", "Pennsylvania Ave.","Park Place", "Boardwalk", "Reading Railroad", "Pennsylvania Railroad","B. & O. Railroad","Short Line Railroad"]
                                TradingABuilding = input().lower()
                                for x in range(0, 26):
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
                                for x in range(0, 26):
                                        if list5[x] == WhoTheyWantToTrade:
                                                print(list1[x] + ", ")   
                                print("for...")
                                print(str(GiveMoney2) + " of player " + str(WhoTheyWantToTrade)+"'s gold and ")
                                for x in range(0, 26):
                                        if list5[x] == StarterOfTrade:
                                                print(list1[x]+", ")
                                                
                                print("Does player " + str(WhoTheyWantToTrade) + " agree to this? (yes or no)")
                        else:
                                print("Player " + str(WhoTheyWantToTrade) + " wants player "+str(StarterOfTrade) +" to instead give them $"+ str(GiveMoney1) + " and ")
                                for x in range(0, 26):
                                        if list5[x] == WhoTheyWantToTrade:
                                                print(list1[x] + ", ")
                                print("for...")
                                print("Player " + str(WhoTheyWantToTrade) +"'s $"+ str(GiveMoney2) + " and ")
                                for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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
                                                        for x in range(0, 26):
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





#def ElectricCompanyWaterWorks(PlayerWhoLandedOnOneOfThem, LandedOn):
#        print()
def GetAllBuildings():
        for x in range(0, 28):
                list3[x] = 1
        





        
x = HowManyPlayers()
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
        MonopolyMap()
        print("It is currently Player " + str(playerTurn) + " Turn.\nType 'Roll' or 'r' to Roll.\nType 'Trade' or 't' to switch money/buildings with other players.\n'Add' or 'a' a house to one of your monopolies.\nType 'Stats' or 's' to learn about what people currently have and have not.")
        WhatTheyWantToDo = input().lower()
        if WhatTheyWantToDo.lower() == "roll" or WhatTheyWantToDo.lower() == "r" or WhatTheyWantToDo.lower() == "ro" or WhatTheyWantToDo.lower() == "rol":
                if playerTurn == 1:
                    Roll = 0
                    Roll = DiceRoll(1)
                    print("You roll a " + str(Roll) + "!\nPress Enter to Move.")
                    input()
                    if int(Player1Location + Roll) > 40:
                        Player1Money += 200
                        Player1Location = int(Player1Location + Roll) - 40
                        LandedPlaces(Player1Location, 1)
                    else:
                        Player1Location += Roll
                        LandedPlaces(Player1Location, 1)
                elif playerTurn == 2:
                    Roll = 0
                    Roll = DiceRoll(2)
                    print("You roll a " + str(Roll) + "!\nPress Enter to Move.")
                    input()
                    if int(Player2Location + Roll) > 40:
                        Player2Money += 200
                        Player2Location = int(Player2Location + Roll) - 40
                        LandedPlaces(Player2Location, 2)
                    else:
                        Player2Location += Roll
                        LandedPlaces(Player2Location, 2)
                elif playerTurn == 3:
                    Roll = 0
                    Roll = DiceRoll(3)
                    print("You roll a " + str(Roll) + "!\nPress Enter to Move.")
                    input()
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
                    print("You roll a " + str(Roll) + "!\nPress Enter to Move.")
                    input()
                    if int(Player4Location + Roll) > 40:
                        Player4Money += 200
                        Player4Location = int(Player4Location + Roll) - 40
                        LandedPlaces(Player4Location, 4)
                    else:
                        Player4Location += Roll
                        LandedPlaces(Player4Location, 4)
                playerTurn += 1
        elif WhatTheyWantToDo.lower() == "stats" or WhatTheyWantToDo.lower() == "stat" or WhatTheyWantToDo.lower() == "sta" or WhatTheyWantToDo.lower() == "st" or WhatTheyWantToDo.lower() == "s":
                #list1 is names
                #list2 is cost of places
                #list3 is the owner
                #list4 is the rent
                for x in range(0, 28):
                        if x < 22:
                                print(list1[x] + ", cost - " + str(list2[x])+ ", the owner is player - " + str(list3[x]) + " and the rent is currently " + str(list4[x])+" Houses on this place "+ str(HousesArray[x]) +".")
                        else:
                                print(list1[x] + ", cost - " + str(list2[x])+ ", the owner is player - " + str(list3[x]) + " and the rent is currently " + str(list4[x])+".")
                                
                '''print(list1[0] + ", cost - " + str(list2[0])+ ", the owner is player - " + str(list3[0]) + " and the rent is currently " + str(list4[0])+".")
                print(list1[1] + ", cost - " + str(list2[1])+ ", the owner is player - " + str(list3[1]) + " and the rent is currently " + str(list4[1])+".")
                print(list1[2] + ", cost - " + str(list2[2])+ ", the owner is player - " + str(list3[2]) + " and the rent is currently " + str(list4[2])+".")
                print(list1[3] + ", cost - " + str(list2[3])+ ", the owner is player - " + str(list3[3]) + " and the rent is currently " + str(list4[3])+".")
                print(list1[4] + ", cost - " + str(list2[4])+ ", the owner is player - " + str(list3[4]) + " and the rent is currently " + str(list4[4])+".")
                print(list1[5] + ", cost - " + str(list2[5])+ ", the owner is player - " + str(list3[5]) + " and the rent is currently " + str(list4[5])+".")
                print(list1[6] + ", cost - " + str(list2[6])+ ", the owner is player - " + str(list3[6]) + " and the rent is currently " + str(list4[6])+".")
                print(list1[7] + ", cost - " + str(list2[7])+ ", the owner is player - " + str(list3[7]) + " and the rent is currently " + str(list4[7])+".")
                print(list1[8] + ", cost - " + str(list2[8])+ ", the owner is player - " + str(list3[8]) + " and the rent is currently " + str(list4[8])+".")
                print(list1[9] + ", cost - " + str(list2[9])+ ", the owner is player - " + str(list3[9]) + " and the rent is currently " + str(list4[9])+".")
                print(list1[10] + ", cost - " + str(list2[10])+ ", the owner is player - " + str(list3[10]) + " and the rent is currently " + str(list4[10])+".")
                print(list1[11] + ", cost - " + str(list2[11])+ ", the owner is player - " + str(list3[11]) + " and the rent is currently " + str(list4[11])+".")
                print(list1[12] + ", cost - " + str(list2[12])+ ", the owner is player - " + str(list3[12]) + " and the rent is currently " + str(list4[12])+".")
                print(list1[13] + ", cost - " + str(list2[13])+ ", the owner is player - " + str(list3[13]) + " and the rent is currently " + str(list4[13])+".")
                print(list1[14] + ", cost - " + str(list2[14])+ ", the owner is player - " + str(list3[14]) + " and the rent is currently " + str(list4[14])+".")
                print(list1[15] + ", cost - " + str(list2[15])+ ", the owner is player - " + str(list3[15]) + " and the rent is currently " + str(list4[15])+".")
                print(list1[16] + ", cost - " + str(list2[16])+ ", the owner is player - " + str(list3[16]) + " and the rent is currently " + str(list4[16])+".")
                print(list1[17] + ", cost - " + str(list2[17])+ ", the owner is player - " + str(list3[17]) + " and the rent is currently " + str(list4[17])+".")
                print(list1[18] + ", cost - " + str(list2[18])+ ", the owner is player - " + str(list3[18]) + " and the rent is currently " + str(list4[18])+".")
                print(list1[19] + ", cost - " + str(list2[19])+ ", the owner is player - " + str(list3[19]) + " and the rent is currently " + str(list4[19])+".")
                print(list1[20] + ", cost - " + str(list2[20])+ ", the owner is player - " + str(list3[20]) + " and the rent is currently " + str(list4[20])+".")
                print(list1[21] + ", cost - " + str(list2[21])+ ", the owner is player - " + str(list3[21]) + " and the rent is currently " + str(list4[21])+".")
                print(list1[22] + ", cost - " + str(list2[22])+ ", the owner is player - " + str(list3[22]) + " and the rent is currently " + str(list4[22])+".")
                print(list1[23] + ", cost - " + str(list2[23])+ ", the owner is player - " + str(list3[23]) + " and the rent is currently " + str(list4[23])+".")
                print(list1[24] + ", cost - " + str(list2[24])+ ", the owner is player - " + str(list3[24]) + " and the rent is currently " + str(list4[24])+".")
                print(list1[25] + ", cost - " + str(list2[25])+ ", the owner is player - " + str(list3[25]) + " and the rent is currently " + str(list4[25])+".")'''
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
        #elif WhatTheyWantToDo == "adfasfsgaegaeury77234146347935632196c10381056351056371045713501":
        #        GetAllBuildings()
        else:
                print("What do you want to do? Roll or Look at stats?")
