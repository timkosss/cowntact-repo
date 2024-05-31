import math
class CowFarm:
    def __init__(self, cows) :
        self.cowList = []
        for i in cowNum:
            self.cowList.append(int(i))
    
    def findSmallestLine(self):
        first = True
        edge = False
        temp = 0
        i = 0
        while i < len(self.cowList):
            if self.cowList[i] == 0:
                if temp != 0:
                    if first:
                        if edge:
                          smallest = self.maxDays(temp, True)
                        else:
                            smallest = self.maxDays(temp, False)
                    else:
                        if self.maxDays(temp, False) < smallest:
                            smallest = self.maxDays(temp, False)
                    temp = 0
            elif i == len(self.cowList) - 1 and self.cowList[i] == 1:
                temp += 1
                if first:
                    smallest = self.maxDays(temp, True)
                elif self.maxDays(temp, True) < smallest:
                    smallest = self.maxDays(temp, True)
            else:
                temp += 1
            i += 1
        if 'smallest' in locals():
            return smallest
        return 0
    
    def maxDays(self, num, edge):
        if edge:
            return num - 1
        else:
            return int((num - 1) / 2)
    
    def numOrigin(self, numCows, numDays):
        magicNum = (numDays * 2) + 1
        return math.ceil(numCows/magicNum)
    
    def findTheInfected(self):
        total = 0
        temp = 0
        days = self.findSmallestLine()
        i = 0
        while i < len(self.cowList):
            if self.cowList[i] == 0:
                total += self.numOrigin(temp, days)
                temp = 0
            elif i == len(self.cowList) - 1 and self.cowList[i] == 1:
                temp += 1
                total += self.numOrigin(temp, days)
            else:
                temp += 1
            i +=1
        return total

        



cowNum = "1110111110"
cowLine = CowFarm(cowNum)
print(cowLine.findTheInfected())
