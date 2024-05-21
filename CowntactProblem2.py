import math
class CowFarm:
    def __init__(self, cows) :
        self.cowList = []
        for i in cowNum:
            self.cowList.append(int(i))
    
    def findSmallestLine(self):
        first = True
        temp = 0
        i = 0
        while i < len(self.cowListcowList):
            if self.cowList[i] == 1:
                temp+=1
            elif temp == 0:
                pass
            else:
                if first or temp < smallest:
                    smallest = temp
                    first = False
                temp = 0
        return smallest
    
    def maxDays(numCows):
        return int(numCows / 2)
    
    def numOrigin(numCows, numDays):
        magicNum = (numDays * 2) + 1
        return math.ceil(numCows/magicNum)
        



cowNum = "111110111110"
cowLine = CowFarm(cowNum)