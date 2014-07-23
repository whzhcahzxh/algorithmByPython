#coding:UTF-8
'''
Created on 2014年4月21日

@author: hao
'''
import sys

class pearson_distance():
    '''
    calculate the difference between two vectors using pearson-distance
    '''
    def __init__(self, vector1, vector2):
        '''
        vector1 and vector2 should have same dimension
        Both of them are list type, tuple type is acceptable
        '''
        self.v1 = list()
        self.v2 = list()
        
        if not isinstance(vector1, list):
            if isinstance(vector1):
                self.v1 = list(vector1)
        self.v1 = vector1
        
        if not isinstance(vector2, list):
            if isinstance(vector2, tuple):
                self.v2 = list(vector2)
        self.v2 = vector2
        
        self.v1Length = len(self.v1)
        self.v2Length = len(self.v2)
        if self.v1Length != self.v2Length:
            print 'Error: two vector should have same dimension'
            sys.exit(1)
        
    
    def calculate(self):
        '''
        calculate the coefficient
        
        sum((x-mean(x))*(y-mean(y)))
        --------------------------------------------
        (sum((x-mean(x))^2)*sum((y-mean(y))^2))^0.5
        
        '''
        v1Sum = sum(self.v1)
        v2Sum = sum(self.v2)
        v1Mean = float(v1Sum)/float(self.v1Length)
        v2Mean = float(v2Sum)/float(self.v2Length)
        
        v1Deviation = 0
        v2Deviation = 0
        nominator = 0
        for i in range(self.v1Length):
            v1Deviation += pow((self.v1[i]-v1Mean),2)
            v2Deviation += pow((self.v2[i]-v2Mean),2)
            
            nominator += (self.v1[i]-v1Mean)*(self.v2[i]-v2Mean)
            
        denominator = pow(v1Deviation*v2Deviation,0.5)
        
        try:
            rate = float(nominator)/float(denominator)
            return rate
        except:
            print 'no proper denominator'
            return -1
        

if __name__=='__main__':
    vector1 = list()
    vector2 = list()
    vector1 = range(101,1,-1)
    vector2 = range(2,102)
    
    pearsonTest = pearson_distance(vector1, vector2)
    rate = pearsonTest.calculate()
    print rate
    
    