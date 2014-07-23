#coding:UTF-8
'''
Created on 2014年7月20日

@author: hao
'''

class fastSort():
    
    def process(self, aList):
        lengthList = len(aList)
        if lengthList<=1:
            return aList
        interTemp = aList[0]
        leftList = list()
        rightList = list()
        for i in range(1,lengthList):
            if aList[i]<=interTemp:
                leftList.append(aList[i])
            else:
                rightList.append(aList[i])
        return self.process(leftList)+[interTemp]+self.process(rightList)
        
    
if __name__=='__main__':
    inputList = [1,3,1,2,7,5,90]
    print fastSort().process(aList=inputList)


