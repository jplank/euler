from math import floor, sqrt

def isprime(n):
	if n == 1:
		return False
	elif n == 2:
		return True
	elif n == 3:
		return True
	elif n == 5:
		return True
	elif n % 2 == 0:
		return False
	else:
		for test in range(3, int(2+max(floor(sqrt(n)), 4)), 2):
			if n % test == 0:
				return False
				break
		return True

lowerleft = 1
upperleft = 1
upperright = 1
lowerright = 1
count = 1
primecount = 0

for i in range(1, 40000):
	lowerleft = lowerleft + 8*i - 2 # lower left list
	upperleft = upperleft + 8*i - 4 # upper left list
	upperright = upperright + 8*i - 6 # upper right list
	lowerright = lowerright + 8*i # lower right list
	count = count + 4 
	primecount = primecount + isprime(lowerleft) + isprime(lowerright) + isprime(upperright) + isprime(upperleft)
	if primecount/float(count) < 0.1:
		print "Side Length is " + str(2*i+1)
		break
print "Final layer: " +	str(upperright) + " " + str(upperleft) + " " + str(lowerleft) + " " + str(lowerright)
print str(primecount) + " / " + str(count) + " = " + str(primecount/float(count))

















