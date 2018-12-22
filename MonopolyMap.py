#!/usr/bin/python3

#######
# This file generates the monopoly map. It will run after every player move
#######

def MonopolyMap(Player1Location, Player2Location, Player3Location, Player4Location,
    Player1InJail, Player2InJail, Player3InJail, Player4InJail,
    Player1Money, Player2Money, Player3Money, Player4Money,
    FreeParkingMoney):
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
        VeryLongWordThatHasDaMoney = "Player 1 - " + str(Player1Money) +"   Player 2 - " + str(Player2Money)
        #print("Player 1 - " + str(Player1Money))
        #print("Player 2 - " + str(Player2Money))
        if Player3Location != 99999:
            #print("Player 3 - " + str(Player3Money))
            VeryLongWordThatHasDaMoney += "   Player 3 - " + str(Player3Money)
        if Player4Location != 99999:
            #print("Player 4 - " + str(Player4Money))
            VeryLongWordThatHasDaMoney += "   Player 4 - " + str(Player4Money)
        print(VeryLongWordThatHasDaMoney)
        print("Free Parking amount - " + str(FreeParkingMoney))



