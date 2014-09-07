#!/usr/bin/python
import sys
import math
import random
import xml.etree.ElementTree as ET
import re as re
import os
from wordremover import *
from sets import Set

TAG = ["aan","md","ne","bg","cm"]

wordtag = 0
papertag = 0
citerlist = 0
citedlist = 0
citeinfo = 0



def initDictionaries():
	global wordtag
	global papertag
	global citerlist
	global citedlist
	global citeinfo
	wordtag = {}
	papertag = {}
	citerlist = Set()
	citedlist = Set()
	citeinfo = {}
	return

def parseFile(filename):
	initDictionaries()
	tree = ET.parse(filename)
	paper = tree.getroot()
	for cited in paper:
		title = cited.find("title")
		paperid = title.get("id")
		paperid = normalizePaperId(paperid)

		citerlist.add(paperid) # adding the citer id to the siter list

		tag = cited.find("tag").text

		citcontext = cited.find("citcontext")
		prevsection = citcontext.find("prevsection")
		citsent = citcontext.find("citsent")
		aftsection = citcontext.find("aftsection")
		
		citstr = citsent.get("citstr") # id of the cited paper
		citationtext = citsent.text
		citationtext = re.sub('<papid>[A-Za-z\/][^>]*</papid>', '', citationtext)
		wordlist = wordremover(citationtext)
		insertwordlist(wordlist,tag)
		insertpaper(citstr,tag)

		citedlist.add(normalizePaperId(citstr)) # add the cited paper to the cited Set
		addCiteInfo(paperid,normalizePaperId(citstr),wordlist)
	# print wordtag
	# print papertag
	# print citeinfo["w05-1511"]["w97-0302"]
	# print citeinfo
	# for x in citeinfo:
	# 	print "citer = ",x
	# 	for y in citeinfo[x]:
	# 		print "cited",y
	# 		print citeinfo[x][y]
	# 		print "\n"
	# 	print "\n\n"
	return

def tagtoindex(tag):
	tag = tag.strip(" \n\t\r")
	return TAG.index(tag.lower())

def tagtolist(tag):

	tag = tag.lower()
	tag = tag.strip(" \n\t\r")
	# print tag
	if tag == "aan":
		return [1,0,0,0,0]
	elif tag == "md":
		return [0,1,0,0,0]
	elif tag == "ne":
		return [0,0,1,0,0]
	elif tag == "bg":
		return [0,0,0,1,0]
	elif tag == "cm":
		# print "cm"
		return [0,0,0,0,1]
	else:
		return [1,0,0,0,0]
		#TODO

def insertword(word, tag):
	global wordtag
	normalizedword = normalizeWord(word)
	if normalizedword in wordtag:
		# wordtag[word] = map(sum, zip(wordtag[word],tagtolist(tag)))
		wordtag[normalizedword] = [x + y for x, y in zip(wordtag[normalizedword], tagtolist(tag))]
	else:
		wordtag[normalizedword] = tagtolist(tag)

def insertwordlist(wordlist, tag):
	global wordtag
	for word in wordlist:
		insertword(word,tag)

def rchop(thestring, ending):
	if thestring.endswith(ending):
		return thestring[:-len(ending)] 
	return thestring


def normalizePaperId(paper):
	paperid = paper.lower()
	paperid = re.sub('\.xml$','',paperid)
	paperid = paperid.strip(" \t\n\r")
	# paperid = paperid.strip('.xml')
	paperid = rchop(paperid,".xml")
	return paperid

def normalizeWord(word):
	normalizedword = word.lower()
	normalizedword = normalizedword.strip(" \t\n\r")
	return normalizedword

def insertpaper(paper, tag):
	global papertag
	normalizedpaper = normalizePaperId(paper)
	if normalizedpaper in papertag:
		papertag[normalizedpaper] = [x + y for x, y in zip(papertag[normalizedpaper], tagtolist(tag))]
	else:
		papertag[normalizedpaper] = tagtolist(tag)

def addCiteInfo(citer,cited,wordlist):
	if citer in citeinfo:
		if cited in citeinfo[citer]:
			citeinfo[citer][cited] = citeinfo[citer][cited] + wordlist
		else:
			citeinfo[citer][cited] = wordlist
	else:
		citeinfo[citer] = {}
		citeinfo[citer][cited] = wordlist

def import_test():
	print "import works"
	return
# USE ONLY THE FOLLOWING FUNCTIONS
# 
# 
# USE THEM IN YOUR CODE ************************
def getTagGivenWord(tag,word):
	p = 0.0
	normalizedword = normalizeWord(word)
	normalizedword
	l = 0
	if normalizedword in wordtag:
		l = wordtag[normalizedword]
		# print l,l[tagtoindex(tag)],sum(l)
		p = (l[tagtoindex(tag)]*1.0)/(sum(l)*1.0)
		return p
	else:
		return 0.0 # TODO smoothing
# tag is a string in "aan","md","ne","bg","cm"
# word is any string

def getTagCountGivenPaper(tag,paperId):
	normalizedpaper = normalizePaperId(paperId)
	# print normalizedpaper
	if normalizedpaper in papertag:
		l = papertag[normalizedpaper]
		# print l
		return l[tagtoindex(tag)]
	return 

# returns a 'Set' of paperids who site [set of all titles] https://docs.python.org/2/library/sets.html
def getCiterList():
	return citerlist

# returns the 'Set' of all cited papers
def getCitedList():
	return citedlist
# note for given data set citer and cited set are not same
# note all strings are normalized (in lowe case with no extra space)
# from paperid if it ends with .xml then it is removed
def doesCite(citerx,citedx):
	# returns True if citer cites cited otherwise False
	citer = normalizePaperId(citerx)
	cited = normalizePaperId(citedx)
	if citer in citeinfo:
		if cited in citeinfo[citer]:
			return True
	return False

def getCitationContext(citerx,citedx):
	# returns an empty list if citer does not cite cited
	# otherwise set of major words
	citer = normalizePaperId(citerx)
	cited = normalizePaperId(citedx)
	if(doesCite(citer,cited)):
		return citeinfo[citer][cited]
	return []
# USE THEM IN YOUR CODE ************************