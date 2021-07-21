#!/usr/bin/env python

import sys
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize



cats_file = open('cats_txt.txt', 'r', encoding='mbcs')
cats = cats_file.read().replace("\n", " ")
cats_file.close()

tokens =wordpunct_tokenize(cats)

lower_words=[t.lower() for t in tokens]

word_lemmatizer=WordNetLemmatizer()

lemmatized = [word_lemmatizer.lemmatize(t) for t in lower_words]

bow=Counter(lemmatized)

print(bow)