#coding:UTF-8
'''
Created on 2014年5月3日

@author: hao
'''
import scipy

class distanceCalculate():
    
    def euclideanDistance(self, v1, v2):
        '''
        Euclidean Distance
        '''
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise ValueError('vectors should be list type')
            return -1
        if len(v1) != len(v2):
            raise ValueError('two lists have different dimension')
            return -1
        
        return pow(sum(pow(x1-x2,2) for (x1, x2) in zip(v1,v2)),0.5)
    
    def manhattanDistance(self, v1, v2):
        '''
        Manhattan Distance
        '''
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise ValueError('vectors should be list type')
            return -1
        if len(v1) != len(v2):
            raise ValueError('two lists have different dimension')
            return -1
        
        return sum(abs(x1-x2) for (x1,x2) in zip(v1, v2))

    def chebyshevDistance(self, v1, v2):
        '''
        Chebyshev Distance
        '''
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise ValueError('vectors should be list type')
            return -1
        if len(v1) != len(v2):
            raise ValueError('two lists have different dimension')
            return -1
        
        return max([abs(x1-x2) for (x1,x2) in zip(v1,v2)])

    def hammingDistance(self, s1, s2):
        '''
        the Hamming distance between two strings of equal length is the number of 
        positions at which the corresponding symbols are different.
        '''
        if not isinstance(s1, str) or not isinstance(s2, str):
            raise ValueError('Hamming distance only calculate difference two strings with same length')
            return -1
        if len(s1) != len(s2):
            raise ValueError('two strings have different dimension')
            return -1
        
        return sum(ch1!=ch2 for (ch1,ch2) in zip(s1,s2))
    
    def minkowskiDistance(self, v1, v2, exponential):
        '''
        a set of distance collections
        '''
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise ValueError('vectors should be list type')
            return -1
        if len(v1) != len(v2):
            raise ValueError('two lists have different dimension')
            return -1
        if exponential<1:
            raise ValueError('exponential should be larger or equal to 1')
            return -1
        return pow(sum(pow(x1-x2,exponential) for (x1, x2) in zip(v1,v2)),1/float(exponential))
            
    def jaccardDistance(self, v1, v2):
        '''
        (A or B)-(A and B)
        ------------------
            (A or B)
        '''
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise ValueError('vectors should be list type')
            return -1
        # v1 and v2
        v1ANDv2 = list(set(v1).intersection(set(v2)))
        # v1 or v2
        v1ORv2 = list(set(v1).union(set(v2)))
        return float(len(v1ORv2)-len(v1ANDv2))/len(v1ORv2)
    
    def cosineDistance(self, v1, v2):
        '''
        vector(a)*vector(b)
        -------------------
            |a|*|b|
        '''
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise ValueError('vectors should be list type')
            return -1
        if len(v1) != len(v2):
            raise ValueError('two lists have different dimension')
            return -1
        return float(scipy.dot(v1,v2))/float(pow(scipy.dot(v1,v1)*scipy.dot(v2,v2),0.5))
    
        
if __name__=='__main__':
    test = distanceCalculate()
#     print test.euclideanDistance([4,5], [2,4])
#     print test.manhattanDistance([90,5], [2,4])
#     print test.chebyshevDistance([2.2,5], [2,4])
#     print test.hammingDistance('s162', 's225')
#     print test.minkowskiDistance([4,5], [2,4],3)
#     print test.jaccardDistance([90,5], [2,5,4]) 
    print test.cosineDistance([-5,-10], [2,4])
    
