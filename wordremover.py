#!/usr/bin/env python
 
import sys
from nltk.corpus import stopwords, wordnet



def determine(word):
	if not wordnet.synsets(word):
		return False
	else:
		return True

def wordremover(txt):
	s = set(stopwords.words('english'))
	wordWithNoun = filter(lambda w: not w in s,txt.split())
	wordWithoutNoun = [word for word in wordWithNoun if determine(word)]
	#print wordWithoutNoun
	#print wordWithNoun

