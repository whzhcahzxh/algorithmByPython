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
    '''
    array 记录 节点id
    '''
    def __init__(self, dimension = 10):
        self.idList = range(dimension)
    
    def find(self, aPoint, bPoint):
        aRoot = aPoint
        while(True):
            if aRoot == self.idList[aRoot]:
                break
            aRoot = self.idList[aRoot]
        bRoot = bPoint
        while(True):
            if bRoot == self.idList[bRoot]:
                break
            bRoot = self.idList[bRoot]
        if aRoot == bRoot:
            return 'connected'
        else:
            return 'isolated'
    
    def union(self, aPoint, bPoint):
        aRoot = aPoint
        while(True):
            if aRoot == self.idList[aRoot]:
                break
            aRoot = self.idList[aRoot]
        bRoot = bPoint
        while(True):
            if bRoot == self.idList[bRoot]:
                break
            bRoot = self.idList[bRoot]
        if bRoot != aRoot:
            self.idList[bRoot] = aRoot
    
class quickUnionwithWeight():
    '''
    compare the depth of the tree
    '''
    def __init__(self, dimension = 10):
        self.idList = range(dimension)
        
    def find(self, aPoint, bPoint):
        aRoot = aPoint
        while(True):
            if aRoot == self.idList[aRoot]:
                break
            aRoot = self.idList[aRoot]
        bRoot = bPoint
        while(True):
            if bRoot == self.idList[bRoot]:
                break
            bRoot = self.idList[bRoot]
        if aRoot == bRoot:
            return 'connected'
        else:
            return 'isolated'
    
    def union(self, aPoint, bPoint):
        aRoot = aPoint
        aDepth = 0
        while(True):
            if aRoot == self.idList[aRoot]:
                break
            aRoot = self.idList[aRoot]
            aDepth+=1
        bRoot = bPoint
        bDepth = 0
        while(True):
            if bRoot == self.idList[bRoot]:
                break
            bRoot = self.idList[bRoot]
            bDepth+=1
        if bRoot != aRoot:
            if bDepth>=aDepth:
                self.idList[aRoot] = bRoot
            else:
                self.idList[bRoot] = aRoot
    
    
class quickUnionwithWeightwithPathCompression():
    '''
    compare the depth of the tree
    '''
    def __init__(self, dimension = 10):
        self.idList = range(dimension)
        
    def find(self, aPoint, bPoint):
        aRoot = aPoint
        while(True):
            if aRoot == self.idList[aRoot]:
                break
            aRoot = self.idList[aRoot]
        bRoot = bPoint
        while(True):
            if bRoot == self.idList[bRoot]:
                break
            bRoot = self.idList[bRoot]
        if aRoot == bRoot:
            return 'connected'
        else:
            return 'isolated'
    
    def union(self, aPoint, bPoint):
        aRoot = aPoint
        aPreRoot = 0
        aDepth = 0
        while(True):
            if aRoot == self.idList[aRoot]:
                break
            aPreRoot = aRoot
            aRoot = self.idList[aRoot]
            self.idList[aPreRoot] = aRoot
            aDepth+=1
            
        bRoot = bPoint
        bPreRoot = 0
        bDepth = 0
        while(True):
            if bRoot == self.idList[bRoot]:
                break
            bPreRoot = bRoot
            bRoot = self.idList[bRoot]
            self.idList[bPreRoot] = bRoot
            bDepth+=1
        if bRoot != aRoot:
            if bDepth>=aDepth:
                self.idList[aRoot] = bRoot
            else:
                self.idList[bRoot] = aRoot
      
  
    
if __name__=='__main__':
    a=time.time()
    test = quickFind(100000)
    test.union(1,2)
    test.union(1,3)
    print test.find(2,3)
    print time.time()-a
    
    a=time.time()
    test = quickUnion(100000)
    test.union(1,2)
    test.union(1,3)
    print test.find(2,3)
    print time.time()-a
    
    a=time.time()
    test = quickUnionwithWeight(100000)
    test.union(1,2)
    test.union(1,3)
    print test.find(2,3)
    print time.time()-a
    
    a=time.time()
    test = quickUnionwithWeightwithPathCompression(100000)
    test.union(1,2)
    test.union(1,3)
    print test.find(2,3)
    print time.time()-a

