def alph(x):
	"""Unlike the other functions containing the alphabet in use,
	this is the only function that assigns non-negative integers back to 
	letters.
	"""
	
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
	
	for i in alphabet:
		if alphabet[i] == x:
			return i
		else:
			continue

def encmat(matlst, numlist):
	"""This function uses the input matrix to encode the user's input
	text.
	"""
	
	# Matrix multiplication takes place here.	
	enclst = [[matlst[0], matlst[1]], [matlst[2], matlst[3]]]
	dotlst = [enclst[0][0]*numlist[0] + enclst[0][1]*numlist[1], 
		enclst[1][0]*numlist[0] + enclst[1][1]*numlist[1]]
	
	# This step ensures the integer values computed above are within the 
	# range 0 - 26.	
	modlst = [dotlst[0] % 27, dotlst[1] % 27]
	
	# The integer values are converted into letters here.	
	strng = str(alph(modlst[0]))+ str(alph(modlst[1]))
	
	return strng

def decmat(invmatlst, asciilst):
	"""This function uses the inverse matrix to decode the user's
	input text."""
	
	# Matrix multiplication takes place here.
	declst = [[invmatlst[0], invmatlst[1]], [invmatlst[2], invmatlst[3]]]
	dotlst = [declst[0][0]*asciilst[0] + declst[0][1]*asciilst[1],
		declst[1][0]*asciilst[0] + declst[1][1]*asciilst[1]]

	# The steps below ensure the integer values computed above are within 
	# the range 0 - 26.	
	modlst = [dotlst[0] % 27, dotlst[1] % 27]
	
	for i in range(len(modlst)):
		if modlst[i] < 0:
			modlst[i] += 27
		else:
			continue
			
	# The integer values are converted into letters here.	
	strng = str(alph(modlst[0])) + str(alph(modlst[1]))
	
	return strng

def invmat(matlst):
	"""This function computes the inverse matrix corresponding to the
	user's input matrix.
	"""
	
	# The denonminator of the determinant is computed here.	
	det = matlst[0] * matlst[3] - matlst[1] * matlst[2]
	
	while det < 0:
		det += 27	
	
	# The determinant (which is not necessarily an integer)	is transformed
	# into its modulo 27 counterpart, here.
	for i in range(1, 27):
		if (det*i % 27) == 1:
			det = i
			break
		
	# The inverse matrix is computed here.		
	invmatlst1 = [det * matlst[3], -1 * (det * matlst[1]), 
		-1 * (det * matlst[2]), det *matlst[0]]
		
	# The following steps ensure each value within the inverse matrix is in
	# the range 0 - 26.		
	for i in invmatlst1:
		while i < 0:
			i += 27
			
	invmatlst2 = [invmatlst1[0] % 27, invmatlst1[1] % 27, 
		invmatlst1[2] % 27, invmatlst1[3] % 27]
		
	return invmatlst2
