def multisplit(string, delimiters):
	"""	Uses the split function over multiple delimiters

		Parameters:
		string (string): The string to apply the dleimiters to
		delimiters (list): list of the delimiters to apply to the string

		Returns:
		newlist (list): A list of strings analagous to the output of the split function

	"""
	oldlist = [string]
	for i in range(len(delimiters)):
		newlist = []
		breaker = delimiters[i]
		for j in range(len(oldlist)):
			newlist.extend(oldlist[j].split(breaker))
		oldlist = newlist
	return newlist

dict = {
	"vigintillion": 1000000000000000000000000000000000000000000000000000000000000000,
	"novemdecillion": 1000000000000000000000000000000000000000000000000000000000000,
	"octodecillion": 1000000000000000000000000000000000000000000000000000000000,
	"septendecillion": 1000000000000000000000000000000000000000000000000000000,
	"sexdecillion": 1000000000000000000000000000000000000000000000000000,
	"quindecillion": 1000000000000000000000000000000000000000000000000,
	"quattuordecillion": 1000000000000000000000000000000000000000000000,
	"tredecillion": 1000000000000000000000000000000000000000000,
	"duodecillion": 1000000000000000000000000000000000000000,
	"undecillion": 1000000000000000000000000000000000000,
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

tcid = {value : key for (key, value) in dict.items()}

def word2int(words):
	"""	Takes an integer number written out in English and returns the number it represents

		Parameters:
		words (string): The written words you want converted

		Returns:
		fullnum (int): The number representation of the input words

	"""
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
				tempnum *= 100
			elif (list[i] == "thousand" or list[i][-3:] == "ion"):
				tempnum *= dict[list[i]]
				fullnum += tempnum
				tempnum = 0
			else:
				tempnum += dict[list[i]]
	fullnum += tempnum
	fullnum *= sign

	return fullnum


def int2word (number):
	"""	Takes an integer number and writes it out in English

		Parameters:
		number (int): The number to be written out

		Returns:
		words (string): The written out format of the input

	"""
	number = str(number)
	i = len(number)
	list = []
	while (i>0):
		if (i<3):
			temp = number
			print(number,temp,list)
			list.insert(0,temp)
			print(number,temp,list)
		else:
			temp = number[-3:]
			print(number,temp,list)
			number = number[:-3]
			print(number,temp,list)
			list.insert(0,temp)
			print(number,temp,list)
		i -= 3

	words = ""
	return words

int2word(5545566)
