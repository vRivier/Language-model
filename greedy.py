# -*- coding: utf-8 -*-

import pickle
import operator
import sys
import pprint


# Usage of model language

# produce best word sequence possible (compare greedy/ beam search/ viterbi)

# (other possible usage : score an existing word sequence)


""" 
Current issue with beam search : with beam size (n) = 1, the predicted sentence is different from the greedy algorithm, which shouldn't be

"""

n=3

bigrams = pickle.load(open(str(n)+'grams.pkl','rb'))


# - - - - - - - - - - - - - - - - - - - - - 
# Greedy

"""  
The algorithm starts with bigram ('BEGIN', 'NOW')
At every iteration, algorithm picks in the language model the most probable next word after the previous bigram.
This word is appended to the final sentence, and the previous bigram is updated.
The algorithm keeps going until the language model predicts the word 'END'.

"""

print('greedy - - - ')


sentence = ''
sentence_proba = 0
# makes a tuple with decreasing number of x's (ex: for n=2, hist=('xx', 'x'))
hist = tuple([(i+1)*'x' for i in reversed(range(n))])
third_word = None

def most_probable_third_word(bigrams, hist):
    return max(bigrams[hist].items(), key=operator.itemgetter(1))[0]


while third_word != 'END':
    third_word = most_probable_third_word(bigrams, hist)
    proba = bigrams[hist][third_word]
    sentence += third_word+' '
    sentence_proba += proba
    hist = list(hist)
    hist = hist[1:] + [third_word]
    hist = tuple(hist)
    

print(sentence)
print(sentence_proba/len(sentence.split())), print()
