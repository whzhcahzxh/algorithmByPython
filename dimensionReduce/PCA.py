#coding:UTF-8
'''
Created on 2014年4月21日

@author: hao
'''
import sys
import numpy

class PCA():
	def __init__(self, dataset):
		# check dataset
    if not isinstance(dataset, numpy.ndarray):
        raise ValueError('''Error: input data should be formatted as numpy.ndarray. eg.numpy.array([[1,2],[2,4],[6,7]]), 
                            means three points whose location is [1,2],[2,4],[6,7]''')
        sys.exit(1)
		
		self.matrixData = numpy.matrix(dataset)


if __name__=='__main__':
	test = PCA()