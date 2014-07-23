#coding:UTF-8
'''
Created on 2014年5月4日

@author: hao
'''
import sys
from random import uniform

import numpy

from distance.distanceClasses import distanceCalculate


class kmeansClustering():
    def __init__(self, dataset, clusterNumber, iterationTime = 5, distanceClass = 1):
        '''        
        distanceClass:2 Cosines distance
        distanceClass:3 Manhattan distance
        distanceClass:3 Chebyshev distance
        others(1): Euclidean Distance
        '''
        # check clusterNumber
        if clusterNumber<1 or int(clusterNumber)!= clusterNumber:
            raise ValueError('Error: clusterNumber should be a positive integer!')
            sys.exit(1)
        self.clusterNumber = clusterNumber

        # check clusterNumber
        if iterationTime!=-1:
            if iterationTime<1 or int(iterationTime)!= iterationTime:
                raise ValueError('Error: iterationTime should be a positive integer or -1 means infinite!')
                sys.exit(1)
        self.iterationTime = iterationTime
        
        # distanceCalculate
        self.distanceClass = distanceCalculate()
        # check dataset
        if not isinstance(dataset, numpy.ndarray):
            raise ValueError('''Error: input data should be formatted as numpy.ndarray. eg.numpy.array([[1,2],[2,4],[6,7]]), 
                                means three points whose location is [1,2],[2,4],[6,7]''')
            sys.exit(1)
        
        self.dataset = numpy.matrix(dataset)
        
        if isinstance(self.dataset.getA1()[0], list):
            raise ValueError('''Error: input data should be matrix-like dimensions. eg. 300x200 ''')
            sys.exit(1)
        
        self.datasetShape = self.dataset.shape        
        self.clusterDimension = self.datasetShape[1]
        self.dataSetNum = self.datasetShape[0]
#         print uniform(10,20)
        self.kmeansClasses = list()
        '''
        iteration
        '''
        # matrix maximum and minimum value for random
        maxValue = self.dataset.max()
        minValue = self.dataset.min()
        
        tempCenters = [[uniform(minValue,maxValue) for j in range(self.clusterDimension)] for i in range(self.clusterNumber)]
#         # initial centroids location
        self.centroids = numpy.matrix(numpy.array(tempCenters))
        self.tempcentroids = numpy.matrix(numpy.array(tempCenters))
        
        self.clustering(iterationTime, distanceClass = 1)
        
    def getDataSet(self):
        '''
        get the matrix type dataset
        '''
        return self.dataset
    
    def getCentroids(self):
        '''
        get the final centroids locations
        '''
        return self.centroids
    
    def getClasses(self):
        '''
        get the final classified index
        '''
        return self.kmeansClasses
    
    
    def clustering(self, iterationTime, distanceClass = 1):
        '''
        Data matrix and center matrix calculation
        '''
        if distanceClass==2:
            distanceCalculate = self.distanceClass.cosineDistance
        elif distanceClass==3:
            distanceCalculate = self.distanceClass.manhattanDistance
        elif distanceClass==4:
            distanceCalculate = self.distanceClass.chebyshevDistance
        else:
            distanceCalculate = self.distanceClass.euclideanDistance
        
        if iterationTime == -1:
            while True:
                distanceMatrix = numpy.matrix([[distanceCalculate(list(centroid.getA1()), list(data.getA1())) 
                                   for centroid in self.centroids] for data in self.dataset])
    #             print distanceMatrix
                tempCluterIndex = distanceMatrix.argmin(1)
                centerChanged = [0]*self.clusterNumber
                newCentroids = [[0]*self.clusterDimension for j in range(self.clusterNumber)]
    #             print tempCluterIndex.A1
                for j in range(self.dataSetNum):
    #                 new centroid location
                    newCentroids[tempCluterIndex.getA1()[j]] = [x+y for (x,y) in zip(newCentroids[tempCluterIndex.getA1()[j]], self.dataset[j].getA1())]
                    # changed number
    #                 print tempCluterIndex.getA1()[j]
                    centerChanged[tempCluterIndex.getA1()[j]]+=1
                    
    #             print newCentroids
    #             print centerChanged
                tempCenter = list()
                for (x,y) in zip(newCentroids, centerChanged):
                    tmp = list()
                    for j in range(len(x)):
                        if y!=0:
                            tmp.append(float(x[j])/y)
                        else:
                            tmp.append(0)
                    tempCenter.append(tmp)
                    
    #             newCentroids = [float(x)/y for (x,y) in zip(newCentroids, centerChanged) if y!=0]
                for j in range(self.clusterNumber):
                    if centerChanged[j]!=0:
                        self.centroids[j] = tempCenter[j]
                self.kmeansClasses = tempCluterIndex.A1
                
                if list(self.tempcentroids.A1) == list(self.centroids.A1):
                    break     
                self.tempcentroids = self.centroids     
        else:
            for i in range(self.iterationTime):
                distanceMatrix = numpy.matrix([[distanceCalculate(list(centroid.getA1()), list(data.getA1())) 
                                   for centroid in self.centroids] for data in self.dataset])
    #             print distanceMatrix
                tempCluterIndex = distanceMatrix.argmin(1)
                centerChanged = [0]*self.clusterNumber
                newCentroids = [[0]*self.clusterDimension for j in range(self.clusterNumber)]
    #             print tempCluterIndex.A1
                for j in range(self.dataSetNum):
    #                 new centroid location
                    newCentroids[tempCluterIndex.getA1()[j]] = [x+y for (x,y) in zip(newCentroids[tempCluterIndex.getA1()[j]], self.dataset[j].getA1())]
                    # changed number
    #                 print tempCluterIndex.getA1()[j]
                    centerChanged[tempCluterIndex.getA1()[j]]+=1
                    
    #             print newCentroids
    #             print centerChanged
                tempCenter = list()
                for (x,y) in zip(newCentroids, centerChanged):
                    tmp = list()
                    for j in range(len(x)):
                        if y!=0:
                            tmp.append(float(x[j])/y)
                        else:
                            tmp.append(0)
                    tempCenter.append(tmp)
                    
    #             newCentroids = [float(x)/y for (x,y) in zip(newCentroids, centerChanged) if y!=0]
                for j in range(self.clusterNumber):
                    if centerChanged[j]!=0:
                        self.centroids[j] = tempCenter[j]  
                self.kmeansClasses = tempCluterIndex.A1
                
                if list(self.tempcentroids.A1) == list(self.centroids.A1):
                    break
                self.tempcentroids = self.centroids   
#             print self.centroids
    
    
    
if __name__=='__main__':

    data = numpy.array([[7,2,5],[2,4,7],[2,5,7],[6,8,9],[9,2,3]])
    
    testKmeans = kmeansClustering(dataset=data, clusterNumber=2, iterationTime=201, distanceClass=1)
    
    print testKmeans.getCentroids()
    print testKmeans.getClasses()
    print testKmeans.getDataSet()



