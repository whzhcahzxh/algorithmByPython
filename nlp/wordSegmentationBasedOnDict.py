#coding:UTF-8
'''
Created on 2014年6月12日

@author: hao
'''
class wordSegOnDict():
    '''
    基于词典的分词，正向最大匹配和反响最大匹配
    '''
    def __init__(self, dictPath='dataset/Lexicon_full_words.txt'):
        '''
        读入词典
        '''
        self.wordList = tuple()
        self.wordListCount = 0
        #分词规则
        self.maxWordLength = 7
        self.segResult = list()
        
        tempList = list()
        with open(dictPath,'r') as fp:
            words = fp.readlines()
            for word in words:
                tempList.append(word.strip().decode('utf8'))
                self.wordListCount+=1
        self.wordList = tuple(tempList)
    
    def getDict(self):
        '''
        返回词典
        '''
        return self.wordList
    
    def maximumMatching(self, sentence):
        '''
        最大正向匹配分词
        '''
        self.segResult = list()
        sentence = sentence.decode('utf8').strip()
        sentenceLength = len(sentence)
        tempTerm = str()
        tempLength = 0
        #segment continue until no word left
        while (sentenceLength>0):
            #取短句
            if sentenceLength>self.maxWordLength:
                tempTerm = sentence[:self.maxWordLength]
                tempLength = self.maxWordLength
            else:
                tempTerm = sentence
                tempLength = sentenceLength
            #将待选词长度依次缩短
            while(tempLength>0):
                #如果匹配到词典中的词或者只剩一个词
#                 print tempTerm[:tempLength]
                if tempTerm[:tempLength] in self.wordList or tempLength==1:
                    self.segResult.append(tempTerm[:tempLength])
                    sentenceLength -= tempLength
                    sentence = sentence[tempLength:]
                    break
                tempLength-=1
            
        return '|'.join(self.segResult)
    
    def reverseMaximumMatching(self, sentence):
        '''
        最大逆向匹配分词
        '''
        self.segResult = list()
        sentence = sentence.decode('utf8').strip()
        sentenceLength = len(sentence)
        tempTerm = str()
        tempLength = 0
        #segment continue until no word left
        while (sentenceLength>0):
            #取短句
            if sentenceLength>self.maxWordLength:
                tempTerm = sentence[-self.maxWordLength:]
                tempLength = self.maxWordLength
            else:
                tempTerm = sentence
                tempLength = sentenceLength
            #将待选词长度依次缩短
            while(tempLength>0):
                #如果匹配到词典中的词或者只剩一个词
#                 print tempTerm[:tempLength]
                if tempTerm[-tempLength:] in self.wordList or tempLength==1:
                    self.segResult.append(tempTerm[-tempLength:])
                    sentenceLength -= tempLength
                    sentence = sentence[:-tempLength]
                    break
                tempLength-=1
        self.segResult = reversed(self.segResult)    
        return '|'.join(self.segResult)
    
    def doubleDirectionMaximumMatching(self, sentence):
        '''
        最大双向匹配分词
        '''
        
        return self.segResult
    
    

            
if __name__=='__main__':
    test = wordSegOnDict()
    text = '''
    我们在野生动物园玩
    '''
    print test.maximumMatching(text)
    print test.reverseMaximumMatching(text)