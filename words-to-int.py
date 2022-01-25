def multisplit(string, delimiters): #Takes a string and  a list of delimiters and uses the split function sequentially over each delimiter, compiling all remaining strings into a single list
	oldlist = [string]
	for i in range(len(delimiters)):
		newlist = []
		breaker = delimiters[i]
		for j in range(len(oldlist)):
			newlist.extend(oldlist[j].split(breaker))
		oldlist = newlist
	return newlist

dict = {
	"decillion": 1000000000000000000000000000000000,
	"nonillion": 1000000000000000000000000000000,
	"octillion": 1000000000000000000000000000,
	"septillion": 1000000000000000000000000,
	"sextillion": 1000000000000000000000,
	"quintillion": 1000000000000000000,
	"quadrillion": 1000000000000000,
	"trillion": 1000000000000,
	"billion": 1000000000,
	"million": 1000000,
	"thousand": 1000,
	"hundred": 100,
	"ninety": 90,
	"eighty": 80,
	"seventy": 70,
	"sixty": 60,
	"fifty": 50,
	"fourty": 40,
	"thirty": 30,
	"twenty": 20,
	"nineteen": 19,
	"eighteen": 18,
	"seventeen": 17,
	"sixteen": 16,
	"fifteen": 15,
	"fourteen": 14,
	"thirteen": 13,
	"twelve": 12,
	"eleven": 11,
	"ten": 10,
	"nine": 9,
	"eight": 8,
	"seven": 7,
	"six": 6,
	"five": 5,
	"four": 4,
	"three": 3,
	"two": 2,
	"one": 1
}

def word2int(words):
	sign = 1
	if (words[0] == "-"):
		sign = -1
	list = multisplit(words, [",","-"," "])
	if (list[0] == "minus" or list[0] == "negative"):
		sign = -1
		del list[0]
	elif (list[-2:] == ["below","zero"]):
		sign = -1
		del list[-2:]
	tempnum = 0
	fullnum = 0
	for i in range(len(list)):
		if (list[i] == "and" or list[i] == ""):
			continue
		else:
			if (list[i] == "a"):
				list[i] = "one"
			if (list[i] == "hundred"):
				tempnum*=100
			elif (list[i] == "thousand" or list[i][-3:] == "ion"):
				tempnum *= dict[list[i]]
				fullnum += tempnum
				tempnum = 0
			else:
				tempnum += dict[list[i]]
	fullnum += tempnum
	fullnum *= sign
	return fullnum
