pent = []
from math import sqrt

def check(n):
	for test in pent:
		x = (sqrt(abs(test - n)*24+1)+1)/6.0
		if x.is_integer():
			y = (sqrt(abs(test + n)*24+1)+1)/6.0
			if y.is_integer():
				print "Num1: " + str(test) + ", Num2: " + str(n) + ", Diff: " + str(abs(test-n))

for i in range (1, 10000):
	check(i*(3*i-1)/2)
	pent.append(i*(3*i-1)/2)


