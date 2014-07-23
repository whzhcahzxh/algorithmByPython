#coding:UTF-8
'''
Created on 2014.4.22

tf-idf implementation

@author: hao
'''
from math import log
import jieba

class TFIDF():
    def __init__(self):
        jieba.enable_parallel(5)
#         dictionary type term list records how many articles has certain word
        self.refTermList = {}
#         term score dictionary records every term tfidf score
        self.termScore = {}
#         total article number
        self.articleNum = 0
        
        self.stopword = []
        # read in stopword
        fp = open('../stopwords.txt','r')
        words = fp.readlines()
        for word in words:
            word = word.strip()
            word = word.replace('\n','')
            self.stopword.append(word)
        fp.close()        
    
    '''
    articles are list type documents    ['','']    
    '''
    def readInReference(self, articles):
        for article in articles:
            print 'read in '+str(self.articleNum)+ ' sample'
            self.articleNum += 1
#             record dictionary
            tempDict = dict()
            cutResult = jieba.cut(article)
            for word in cutResult:
                if word not in self.stopword:
                    if not word.isdigit() and word.isalpha():
                        tempDict[word] = 1
            
            for tempTerm in tempDict.iterkeys():
                if tempTerm in self.refTermList:
                    self.refTermList[tempTerm] += 1
                else:
                    self.refTermList[tempTerm] = 1
    
    def getReference(self):
        return self.refTermList
    
    '''
    sentence is string type document
    '''
    def readInQuery(self, sentence):
        cutResult = jieba.cut(sentence)
        tempDict = dict()
        for word in cutResult:
            if word not in self.stopword:
                if not word.isdigit() and word.isalpha():
                    if word in tempDict:
                        tempDict[word] += 1
                    else:
                        tempDict[word] = 1
#         IDF
        totalWordCount = sum(tempDict.itervalues())
        
        for (word,freq) in tempDict.items():
#             tf
            tf = float(freq)/totalWordCount
#             idf
            if word in self.refTermList:
                idf = log(float(self.articleNum)/(self.refTermList[word]+1))
            else:
                idf = log(self.articleNum/1)
            self.termScore[word] = tf*idf
    
    def getTFIDFScore(self):
        return self.termScore
    
if __name__=='__main__':
    test = TFIDF()
    a = ['【广东高州塌桥事故已有4人被警方控制】广东茂名高州市政府新闻发言人梁瑞波昨日告诉记者，据初步调查，施工方罔顾法规利用假期进行赶工强建造成塌桥事故发生。目前该村委会主任、施工承包者等四人已被警方控制。',
         '【五一成交惨淡楼市下行概率增大 万科等看空未来】刚刚结束的五一小长假期间，全国房地产市场有统计数据的城市一片惨淡，北京等城市成交总量同比大跌近八成。4月份的“百城房价指数”显示，近半数城市环比下跌，甚至连万科等知名开发商也对未来楼市流露出悲观态度。']
    test.readInReference(a)
    
    test.readInQuery('原辽宁省长履新住建部 或改变楼市调控思路】原辽宁省长陈政高日前履新中共住房和城乡建设部党组书记一职。分析指出，辽宁较早开始棚户区改造，一直在辽宁从政的陈政高此次就任住建部，意味着住建部门工作重心可能将更多向棚户区改造倾斜。')
#     ret = test.getReference()
#     print ret
    out = test.getTFIDFScore()
    for (word, score) in out.iteritems():
        print word
        print score

    
    
    
    

