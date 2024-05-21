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
            if self.cowList[i] == 1:
                if i == 0 or i == len(self.cowList) - 1:
                    edge = True
                temp+=1
            elif temp == 0:
                pass
            else:
                if edge:
                    temp = (temp * 2) - 1
                    edge = False
                if first or temp < smallest:
                    smallest = temp
                    first = False
                temp = 0
            i += 1
        return smallest
    
    def maxDays(self):
        return int(self.findSmallestLine() / 2)
    
    def numOrigin(self, numCows, numDays):
        magicNum = (numDays * 2) + 1
        return math.ceil(numCows/magicNum)
    
    def findTheInfected(self):
        total = 0
        tempCluster = 0
        days = self.maxDays()
        for i in self.cowList:
            if i == 1:
                tempCluster += 1
            elif tempCluster == 0:
                pass
            else:
                total += self.numOrigin(tempCluster, days)
                tempCluster = 0
        return total

        



cowNum = "11111"
cowLine = CowFarm(cowNum)
print(cowLine.findTheInfected())
