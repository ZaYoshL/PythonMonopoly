#####
# Represents a property such as
# Park place or Mediterranean Avenue
#####

class Property:
    cost = 0 
    rent = 0 
    owner = -1 # 0 for player 1, 1 for player 2, etc 
    extra = 0
    mortgage = 0 
    name = ""

    def __init__(self, name, cost, rent, extra, mortgage):
        self.name = name
        self.cost = cost
        self.rent = rent
        self. extra = extra
        self.mortgage = mortgage

    def canBePurchased(self, playerMoney):
        return playerMoney >= self.cost and self.owner == -1

    def canAffordToStay(self, playerMoney):
        return playerMoney > self.rent