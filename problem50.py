#
# Solution to Project Euler Problem 50
#

def is_prime(n):
    check = True
    for count in range(2, int(n**0.5)+1):
        if n % count == 0:
            check = False
            break
    if n == 1:
        check = False
    return check


primelist = []
for number in range(1,1000000):
	if is_prime(number): primelist.append(number)

print "Finished constructing list of primes"

maxprime = 0
previouslength = 0
maxprimefactors = []
for length in sorted(range(2, len(primelist) + 1), reverse = True):
	print "Checking lists of size", length
	for y in range(len(primelist)-length):
		currentsum = sum(primelist[y:y+length])
		if currentsum > 1000000: break
		if currentsum in primelist and length > previouslength:
			maxprime = currentsum
			previouslength = length
			maxprimefactors = primelist[y:y+length]
	if maxprime <> 0: break

print maxprime
print maxprimefactors

