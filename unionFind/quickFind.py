#coding:UTF-8
'''
Created on 2014年7月21日

@author: hao
'''
import time
class quickFind():
    '''
    array中的值是所属的类别
    '''
    def __init__(self, dimension = 10):
        self.idList = range(dimension)
    
    def find(self, aPoint, bPoint):
        if self.idList[aPoint]==self.idList[bPoint]:
            return 'connected'
        else:
            return 'isolated'
    
    def union(self, aPoint, bPoint):
        if self.idList[aPoint]!=self.idList[bPoint]:
            preIndex = self.idList[bPoint]
            for i in range(len(self.idList)):
                if self.idList[i]==preIndex:
                    self.idList[i] = self.idList[aPoint]


class quickUnion():
    def __init__(self, dimension = 10):
        self.idList = [1]*dimension
    
    def find(self, aPoint, bPoint):
        pass
    
    def union(self, aPoint, bPoint):
        pass
    
class quickUnionwithWeight():
    def __init__(self, dimension = 10):
        self.idList = [1]*dimension
        
    def find(self, aPoint, bPoint):
        pass
    
    def union(self, aPoint, bPoint):
        pass
    
    
if __name__=='__main__':
    a=time.time()
    test = quickFind(100000)
    test.union(1,2)
    test.union(1,3)
    print test.find(2,3)
    print time.time()-a
    

