#!/usr/bin/python
# ***************************************************************
# NAME     : 	Sourav Sarkar
# Roll No  :	11CS30037  
# ***************************************************************
# To Execute : ./11CS30037.py
# If python interpreter is not found in /usr/bin but its available elsewhere
# try with "python 11CS30037.py"
import sys
import math
import random

def mod_Exp(a,n,p):
	# tested
	result = 1
	a = a % p
	while(n>0):
		if(n%2 == 1):
			result = (result * a) % p
		n = n >> 1
		a = (a * a) % p
	return result

def sqrt_minus1(p):
	# return a such that a^2 = -1 mod p
	# tested for primes >=2
	# returns p+1 for 4k+3 or if not found
	# otherwise if its a prime returns correct result
	if(p%4 == 3):
		print "No result exists for primes of the form 4k+3"
		return p+1
	s = [int]*(p-1)
	for i in range(0,p-1):
		s[i] = i + 1
	power = (p-1)/4
	a = -1
	for i in range(0,p-1):
		choice = random.randint(0,i)
		a = mod_Exp(s[choice],power,p)
		if((a * a)%p == (p-1)):
			# output found
			return a
	print "ERROR SQRT(-1) mod ",p," does not exist !!"
	return p+1

def extended_GCD_thues(l,s):
	# the modified extended gcd computation function
	r0 = l
	r1 = s
	x0 = 1
	x1 = 0
	y0 = 0
	y1 = 1
	sqrt_s = int(math.sqrt(r1))
	# print "LIMIT = ",sqrt_s
	while(r0 >sqrt_s):
		q = int(r0/r1)
		rt = r0 % r1
		r0 = r1
		r1 = rt
		xt = x0 - x1 * q
		yt = y0 - y1 * q
		x0 = x1
		x1 = xt
		y0 = y1
		y1 = yt
		# print "x0 = ",x0," y0 = ",y0," r0 = ",r0," r1 = ",r1,"\n"
	X0 = x0
	Y0 = r0
	# print "X0 = ",x0," Y0 = ",r0,"\n"
	return (X0,Y0)

def prime_to_sum_of_square(p):
	# returns the result if p = 2 or a prime of 4k+1
	a = sqrt_minus1(p)
	if(a>p):
		return -1,-1
	# print "a = ",a
	return extended_GCD_thues(a,p)

def get_as_sum_of_squares(n):
	if(n == 2):
		return 1,1
	if(n == 1):
		return 0,1
	if(n == 0):
		return 0,0
	if(n < 0):
		return -1,-1
	# currently doing for only primes of 4k+1
	if(n%4 == 3):
		return -1,-1
	return prime_to_sum_of_square(n)



def main():
	s = raw_input("\nEnter p:")
	a = int(s)
	x,y = get_as_sum_of_squares(a)
	if(x == -1 and y == -1):
		print "\nERROR no result found !!"
	else:
		print a," = (",x,")^2 + (",y,")^2"
	print "\n"
	return

if __name__ == "__main__":
    main()


# ####################### test suite ############################################## #
# 
# def test_mod_exp():
# 	while(True):
# 		a = int(raw_input("a = "))
# 		n = int(raw_input("n = "))
# 		p = int(raw_input("p = "))
# 		print a,"^",n," = ",mod_Exp(a,n,p),"mod ",p,"\n"
# 
# def test_sqrt_minus1():
# 	while(True):
# 		p = int(raw_input("Enter a prime:"))
# 		a = sqrt_minus1(p)
# 		print a,"^2 = -1 mod ",p
# 		x = mod_Exp(a,2,p)
# 		if(x == p-1):
# 			print "Success !!"
# 		else:
# 			print "failure !!"
# 
# def test_extended_GCD_thues():
# 	while(True):
# 		a = int(raw_input("a = "))
# 		p = int(raw_input("p = "))
# 		x,y = extended_GCD_thues(a,p)
# 		print "GCD = ",d,":::(",x,")*",a," + (",y,")*",p," = ",d  
# 
# 
# def test():
# 	x = [5,13,17,29,37,41,53,61,73,89,97,101,109,113,137, 149,157,173,181,193,197,229,233,241,257,269,277, 281,293,313,317,337,349,353,373,389,397,401,409, 421,433,449,457,461,509,521,541,557,569,577,593,601,613,617]
# 	for i in range(0,54):
# 		X0,Y0 = get_as_sum_of_squares(x[i])
# 		if((X0*X0 + Y0*Y0) == x[i]):
# 			print "SUCCESS !! X0 = ",X0," Y0 = ",Y0," p = ",x[i]
# 		else:
# 			print "FAILURE !! X0 = ",X0," Y0 = ",Y0," p = ",x[i],"******************"
# 	return