#coding:UTF-8
'''
Created on 23 Jul 2014

page rank algorithm

@author: hao
'''
import numpy as np

class pageRank():
    def __init__(self, pageNumber, q = 0.85, threshold = 0.0001):
        '''
        initial [1,1,...,1] and A^-1
        '''
        self.pageNumber = pageNumber
        self.initialRank = np.mat(np.ones(pageNumber)/pageNumber,dtype=np.float64).T
        self.threshold = threshold
        self.q = q
        self.A = np.mat(np.zeros([pageNumber,pageNumber]),dtype=np.float64)
        
    
    def addEdge(self, head, tail):
        '''
        add an edge between pages
        
        head -> tail
        
        index starts from 0
        '''
        if head >= self.pageNumber-1 or tail>=self.pageNumber-1 or tail<0 or head<0:
            print('Warning: index out of range!!!')
        if head != tail:
            self.A[head,tail]=1

        
    def cal(self):
        '''
        recursion
        '''
        # calculate transaction matrix
        tempA = self.A.sum(axis=1)
        for i in range(self.pageNumber):
            if tempA[i,0] == 0:
                continue
            else:
                self.A[i] *= float(1)/tempA[i,0]
        self.A = self.A.T
        # calculate ee^-1/n
        tempE = np.ones((self.pageNumber,self.pageNumber))
        tempEEN = np.mat(tempE, dtype = np.float64)/self.pageNumber
        tempMultiple = self.q*self.A+(1-self.q)*tempEEN
        while(True):
            initialRank = np.dot(tempMultiple,self.initialRank)
            if np.dot((initialRank - self.initialRank).T,(initialRank - self.initialRank))[0,0]<=self.threshold:
                break
            self.initialRank = initialRank
        
        return self.initialRank
        

if __name__=='__main__':
#     test = pageRank(pageNumber=7115)
    test = pageRank(pageNumber=20)
#     with open('Wiki-Vote.txt','r') as fp:
#         lines = fp.readlines()
#     for line in lines:
#         temp = line.strip().split('\t')
#         test.addEdge(eval(temp[0]), eval(temp[1]))
    test.addEdge(1,5)
    test.addEdge(5,1)
    print test.cal()
