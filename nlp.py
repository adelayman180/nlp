import nltk
import string
from nltk.corpus import brown

inputText = input('Enter a string :\n')
inputText = nltk.word_tokenize(inputText)

tokens = list(brown.words(categories='news'))
pn = list(string.punctuation)
for i in tokens:
  if i in pn:
    tokens.remove(i)

vocabulary = set(tokens)
suggestionsIndex = [i+1 for i in range(0,len(tokens)) if tokens[i]==inputText[-1]]
bigram = nltk.bigrams(tokens)
bigram = [' '.join(grams) for grams in bigram]
bigramFreq = nltk.FreqDist(bigram)
wordsFreq = nltk.FreqDist(tokens)


def probability(predict):
 l = inputText[:]
 l.append(predict)
 inputbigram = nltk.bigrams(l) 
 inputbigram = [' '.join(grams) for grams in inputbigram]
 prob = 1
 for i in inputbigram:
  prob*= (bigramFreq[i]+1)/(wordsFreq[nltk.word_tokenize(i)[0]]+len(vocabulary))
 return prob

finalList = []

for i in suggestionsIndex:
 finalList.append(probability(tokens[i]))

if finalList  != []:
 predictionIndex = suggestionsIndex[finalList.index(max(finalList))]
 print(tokens[predictionIndex])
else:
 print('not found')
