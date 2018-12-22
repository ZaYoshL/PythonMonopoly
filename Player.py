#!/usr/bin/python3

class Player:
    playerNum = 0 # 0 for Player 1, 1 for Player 2, etc.
    location = 0
    money = 2000
    inJail = False
    name = "Player"

    def __init__(self, name, playerNum):
        self.name = name
        self.playerNum = playerNum

    def transaction(self, change):
        self.money = self.money + change
        print(f'{self.name} now has {self.money}.')



def createPlayers(numPlayers):
    playerList = []
    for value in range(numPlayers):
        print(f'What would you like to name Player {value + 1}?')
        name = input()
        playerList.append(Player(name, value))
    return playerList

