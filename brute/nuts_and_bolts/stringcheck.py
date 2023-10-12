def strcheck(strng):
	"""Determines if the user-supplied text meets the requirements as
	laid out at the program's initiation.
	"""
	
	flag = True
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	strng = strng.strip()
	strng = strng.lower()
	
	while "  " in strng:
		strng = strng.replace("  ", " ")
	
	if len(strng) == 0:
		flag = False

	else:
		for i in strng:
			if i not in alphabet:
				flag = False
			
	return(strng, flag)

def intconvert(strng):
	"""Converts letters to non-negative integers."""
	
	numlist = []
	alphabet = {
		" ": 0, 
		"a": 1, 
		"b": 2, 
		"c": 3, 
		"d": 4, 
		"e": 5, 
		"f": 6, 
		"g": 7, 
		"h": 8, 
		"i": 9, 
		"j": 10, 
		"k": 11, 
		"l": 12, 
		"m": 13, 
		"n": 14, 
		"o": 15, 
		"p": 16, 
		"q": 17, 
		"r": 18, 
		"s": 19, 
		"t": 20, 
		"u": 21, 
		"v": 22, 
		"w": 23, 
		"x": 24, 
		"y": 25, 
		"z": 26
	}
	
	for i in strng:
		numlist.append(alphabet[i])
		
	if len(numlist) % 2 != 0:
		numlist.append(0)
	
	return numlist
	
