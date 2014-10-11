from math import floor, sqrt
from collections import Counter

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

primes = []

for test in range (1000, 10000):
	if isprime(test):
		primes.append(test)

for bigprime in range(2, len(primes)+1):
	for smallprime in range(1, bigprime):
		if Counter(str(primes[bigprime])) == Counter(str(primes[smallprime])):
			if (2*primes[bigprime] - primes[smallprime] in primes) and (2*primes[bigprime] - primes[smallprime] < 10000):
				if Counter(str(primes[bigprime])) == Counter(str(2*primes[bigprime] - primes[smallprime])):
					print str(primes[smallprime]) + " " + str(primes[bigprime]) + " " + str(2*primes[bigprime] - primes[smallprime]) + " , Sum = " + str(3*primes[bigprime])
					break
