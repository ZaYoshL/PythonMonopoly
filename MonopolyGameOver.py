def GameOver(Player1Money, Player2Money, Player3Money, Player4Money):
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
