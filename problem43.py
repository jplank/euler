from itertools import permutations

check = True
numberlist = []

perms = list(permutations(range(0, 10)))
numberlist = []

joinednumber = ""
for num in perms:
	for digit in num:
		joinednumber = joinednumber + str(digit)
	numberlist.append(int(joinednumber))
	joinednumber =""

count = 0
for testnumber in numberlist:
	div17 = int(str(testnumber)[7:10])
	if div17 % 17 == 0:
		div13 = int(str(testnumber)[6:9])
		if div13 % 13 == 0:
			div11 = int(str(testnumber)[5:8])
			if div11 % 11 == 0:
				div7 = int(str(testnumber)[4:7])
				if div7 % 7 == 0:
					div5 = int(str(testnumber)[3:6])
					if div5 % 5 == 0:
						div3 = int(str(testnumber)[2:5])
						if div3 % 3 == 0:
							div2 = int(str(testnumber)[1:4])
							if div2 % 2 == 0:
								print testnumber
								count += testnumber
print count
