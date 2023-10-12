from nuts_and_bolts.stringcheck import strcheck, intconvert
from nuts_and_bolts.intcheck import intpull, detcheck
from nuts_and_bolts.matrix import encmat, decmat, invmat

def encryptdecrypt():
	"""This function controls the encryption/ decryption process."""
	
	print("\n\n\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
		" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
	
	print("|Enter text to be encoded/ decoded, containing" +
		" only letters from the English\t    |")
	print("|alphabet and spaces.\t\t\t\t\t\t\t\t    |")
	print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
		" _ _ _ _ _ _ _ _ _ _ _ _ _|")
	rawstrng = input("\n\tText: ")
	
	# These steps simply check and see if the input text meets the 
	# requirements as laid out above.
	retstrng = ""
	strng, flag1 = strcheck(rawstrng)
	flag2 = False
	
	while flag1 != True:
		print("\n\tERROR")
		rawstrng = input("\n\tText: ")
		
		strng, flag1 = strcheck(rawstrng)
		
	# This step converts the input text into non-negative integers.
	numlist = intconvert(strng)
	
	print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
		" _ _ _ _ _ _ _ _ _ _ _ _ _")
	print("|Please enter invertible (mod 27) key matrix in the " +
		"following format:\t\t    |")
	print("|\t\t\t\t\t\t\t\t\t|a, b|\t    |")
	print("|\t\t\t\t\t\t\t\t\t|c, d|\t    |")
	print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
		" _ _ _ _ _ _ _ _ _ _ _ _ _|")
	
	# These steps allow the user to input a 2x2 matrix of their choice. 
	# So long as the matrix is invertible modulo 27, the computer prints 
	# both the user matrix and its inverse matrix, and uses one of these for 
	# further computations.
	while flag2 != True:
		
		matlst = intpull()
		
		flag2 = detcheck(matlst)
	
	invmatlst = invmat(matlst)
	
	print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
		" _ _ _ _ _ _ _ _ _ _ _ _ _")
	print("|Your key matrix (modulo 27) is:\t\t\t\t\t\t    |")
	print("|\t\t\t\t\t\t\t\t\t " + str(matlst[0]) + ", " + 
		str(matlst[1]) + "\t    |")
	print("|\t\t\t\t\t\t\t\t\t " + str(matlst[2]) + ", " + 
		str(matlst[3]) + "\t    |")
	print("|\t\t\t\t\t\t\t\t\t\t    |")
	print("|Your inverse key matrix (modulo 27) is:\t\t\t\t\t    |")
	print("|\t\t\t\t\t\t\t\t\t " + str(invmatlst[0]) + ", " + 
		str(invmatlst[1]) + "\t    |")
	print("|\t\t\t\t\t\t\t\t\t " + str(invmatlst[2]) + ", " + 
		str(invmatlst[3]) + "\t    |")
	print("|\t\t\t\t\t\t\t\t\t\t    |")
	print("|Are you encoding or decoding?\t\t\t\t\t\t\t    |")
	print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
		" _ _ _ _ _ _ _ _ _ _ _ _ _|")
	
	# Here the user decides if they would like to quickly encode or decode
	# their text, given the matrix values above.
	inp = input("\n\tPress E for encoding or D for decoding: ")
	
	while inp != 'e' and inp != 'E' and inp != 'd' and inp != 'D':
		print("\n\tERROR")
		inp = input("\n\tPress E for encoding or D for decoding: ")
	
	# Prints encoded text (i.e., 'ciphertext').
	if inp == 'e' or inp == 'E':
		print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
			" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
		print("|Your encoded text is:\t\t\t\t\t\t\t\t    |")
		print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
			" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
	
		for i in range(len(numlist)):
			if (i % 2 != 0):
				continue
			else:
				retstrng += encmat(matlst, [numlist[i], numlist[i+1]])
			
		print("\t" + "'" + retstrng + "'")
		
	# Prints decoded text (i.e., 'plaintext').
	else:
		print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
			" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
		print("|Your decoded text is:\t\t\t\t\t\t\t\t    |")
		print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" +
			" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
		
		for i in range(len(numlist)):
			if (i % 2 != 0):
				continue
			else:
				retstrng += decmat(invmatlst, [numlist[i], 
					numlist[i+1]])
			
		print("\t\t" + "'" + retstrng + "'")
	
