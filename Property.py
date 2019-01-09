

class Property:
    name = ""
    cost = 0
    owner = 0
    rent = 0
    mortgage = 0


    def __init__(self, name, cost, rent, mortgage):
        self.name = name
        self.cost = cost
        #print(rent)
        self.rent = rent
        #print(mortgage)
        self.mortgage = mortgage

    def stats():
        for x in range(0, 28):
            if x < 22:
                print(list1[x] + ", cost - " + str(list2[x])+ ", the owner is player - " + str(list3[x]) + " and the rent is currently " + str(list4[x])+ ".")#" Houses on this place "+ str(HousesArray[x]) +".")
            else:
                print(list1[x] + ", cost - " + str(list2[x])+ ", the owner is player - " + str(list3[x]) + " and the rent is currently " + str(list4[x])+".")



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
#Mortgage
#
list5 = [0, 0, 0,  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , 0  ,0   ,0]
def createPlayerList():
    propertyList = []
    for value in range(len(list1)):
        propertyList.append(Property(list1[value], list2[value], list4[value], list5[value]))
        #print(list3[value])
    return propertyList

