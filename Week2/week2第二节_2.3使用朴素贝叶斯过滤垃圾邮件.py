
# coding: utf-8

# # 从文本中构建词向量  
# ##讲句子转换为向量
# 

# In[16]:


def locadDateSet():
    poseingList = [['my','dog','has','flea','problems','help','please'],['maybe','not','take','him','to','dog','park','stupid'],['my','dalmation','is','so','cute','I','love','him'],['stop','posting','stupid','worthless','garbage'],['mr','licks','ate','my','steak','how','to','stop','him'],['quit','buying','worthless','dog','food','stupid']]
    classVes = [0,1,0,1,0,1]
    return poseingList,classVes

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(Document)
        return list(vocabSet)
    
def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else : 
            print ('The word: %s is not in my vocabulary!' %word)
    return returnVec


# In[17]:


from numpy import *
#import bayes


# # 朴素贝叶斯分类器训练函数
# 

# In[18]:


def trainNB0(trainMatrix,trainCaregory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = zeros(numWords);
    p1Num = zeros(numWords)
    p0Denom = 0.0;
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCaregory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom
    p0Vect = p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive


# # 朴素贝叶斯分类函数

# In[19]:


def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    tarainMat = []
    for postinDoc in listOPosts :
        tarainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love','my','dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid','garbage']
    thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    


# # 完整的垃圾邮件测试函数

# In[20]:


def textParse(bigString):
	import re
	listOfToken = er.split(r'\w*',bigString)
	return [tok.lower() for tok in listOfToken if len(tok) >2]

def spamTest():
	docList = []; classList = []; fullText = []
	for i in range (1,26):
		wordList = textParse(open('email/spam/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)

		wordList = textParse(open('emaild/ham/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
vocabList = createVocablist(docList)
trainingSet = range(50); testSet = []
for i in range (10):
	randIndex = int (random.uniform(0,len(trainingSet)))
	testSet.append(trainingSet[randIndex])
	del(trainingSet[randIndex])
trainMat = [];trainClasses = []
for docIndex in trainingSet:
	trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
	trainClasses.append(classList[docIndex])
p0V,p1V,pSpam = trainNB0 (array(trainMat),array(trainClasses))
errorCount = 0
for docIndex in testSet:
	wordVector = setOfWords2Vec(vocabList, docList[docIndex])
	if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
		errorCount +=1
print ('The error rate is: ',float(errorCount)/len(testSet))

