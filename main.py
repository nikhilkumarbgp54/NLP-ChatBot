import nltk
import numpy as np
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentsnce):
    return nltk.word_tokenize(sentsnce)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_word):

    tokenized_sentence=[stem(w) for w in tokenized_sentence]
    bag=np.zeros(len(all_word), dtype=np.float32)
    for index,w in enumerate(all_word):
        if w in tokenized_sentence:
            bag[index]=1.0
    return (bag)

# testing of tokenize

#a="How does long shipping takes?"
#a = tokenize(a)
#print(a)

# testing of stemming

#words = ["Oeganize","Organizes","Organizing"]
#stemmed_word=[stem(w) for w in words]
#print(stemmed_word)