import numpy as np
import operator
import pickle


def trigrams(words, n):
    trigrams = list()
    for i in range(len(words)-n):
        trigrams.append(tuple([words[i+x] for x in range(n+1)]))
    return trigrams

def calcul_probas(trigrams, n):
    # getting all bigrams
    # for every bigram, keep all the words following this bigram
    # count these words
    # divide by number of bigram occurrences
    # {bigram: {third_word: occurrences}}
    bigrams = dict()
    # init
    for tg in trigrams:
        bigrams[tg[:n]] = dict()
    for tg in trigrams:
        bigrams[tg[:n]][tg[n]] = 0
    # counts
    for tg in trigrams:
        bigrams[tg[:n]][tg[n]] += 1
    # probas
    for bg in bigrams:
        bg_occurrences = sum(bigrams[bg].values())
        for third_word in bigrams[bg]:
            bigrams[bg][third_word] = bigrams[bg][third_word] / bg_occurrences

    return bigrams


def sample_from_discrete_distrib(distrib):
    words, probas = list(zip(*distrib.items()))
    return np.random.choice(words, p=probas)


with open('wine_reviews.txt', 'r', encoding='utf-8') as flow:
    texte = flow.read()

words = texte.split()

n=3

def sentence_starting_words():

	""" The original text data is made for bigram model, so only 2 words are placed at the beginning of sentences (BEGIN and NOW)
		For an n_gram it is necessary to have n words at the beginning of every sentences
		This function replaces 'BEGIN NOW' with decreasing number of x's (ex: for trigram you will find 'xxx xx x') """

	for i in range(len(words)):
		if words[i] == 'BEGIN':
			words.pop(i), words.pop(i)
			for j in range(n):
				words.insert(i, (j+1)*'x')

# preprocessing
sentence_starting_words()

div = int(0.8*len(words))
train = words[:div]
test = words[div:]

# first get all trigrams from the train corpus
trigrams = trigrams(train, n)

# from all those trigrams, compute probability (frequency) of
# the third word considering the two previous words
bigrams = calcul_probas(trigrams, n)

pickle.dump(bigrams, open(str(n)+'grams.pkl','wb'))


