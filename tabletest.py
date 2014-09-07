#!/usr/bin/python
from table import *
from sets import Set 

def main():
	parseFile("matchEntCor.xml")

	# A = getCitedList()
	# print A
	# B = getCiterList()
	# print B

	# for x in B:
	# 	print x # this is how to loop over a Set



	print getTagGivenWord("aan","systems")
	print getTagCountGivenPaper("bg","  C04-1146.xml  ")

	# print doesCite(" W05-1511.xml"," W97-0302 ")
	# print doesCite(" W05-1511.xml"," W97-0302.xml ")
	# print doesCite(" W05-1511"," W97-0302.Xml ")

	# print doesCite(" W05-1511.xml"," W97-02302 ")

	print getCitationContext(" W05-1511.xml"," W97-0302.xml ")

	print getCitationContext(" W05-1511.xml"," W97-02302 ")
	
	# S = Set()
	# S.add(1)
	# S.add(2)
	# print S
	# S.add(2)
	# print S


	return

if __name__ == "__main__":
    main()