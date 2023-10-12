from nuts_and_bolts.ciphercheck import ciphcheck, intconvert
from nuts_and_bolts.brutematrix import matrices
from nuts_and_bolts.wordchecker import splitter, wordcount

def bruteforce():
	"""This function controls the brute force process."""
	
	print("\n\n\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
	"_ _ _ _ _ _ _ _ _ _ _ _")
	print("|Enter text to be decoded (i.e. 'ciphertext'), " +
		"containing only lowercase letters    |")
	print("|from the English alphabet and spaces. Ciphertext should " +
		"be at least four\t    |")
	print("|characters long, with an even number of values.\t\t\t\t    |")
	print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
	"_ _ _ _ _ _ _ _ _ _ _ _|")
		
	print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
	"_ _ _ _ _ _ _ _ _ _ _ _")
	print("|DISCLAIMER #1: If the original text (i.e. 'plaintext') " + 
		"includes slang words,\t    |") 
	print("|non-English words, names, and/ or " +
		"misspellings or improper grammar, a correct match|")
	print("|is not guaranteed.\t\t\t\t\t\t\t\t    |")
	print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
		"_ _ _ _ _ _ _ _ _ _ _ _|")
		
	print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
	"_ _ _ _ _ _ _ _ _ _ _ _")	
	print("|DISCLAIMER #2: Longer ciphertext will take longer to " +
		"compute. Shorter ciphertext   |")
	print("|will be quicker, but may return several possible plaintext values.\t\t    |")
	print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
		"_ _ _ _ _ _ _ _ _ _ _ _|")
	
	rawstrng = input("\n\tCiphertext: ")
	
	# These steps determine if the ciphertext meets the requirements laid
	# out above.
	flag = ciphcheck(rawstrng)
	
	while flag != True:
		print("\n\tERROR")
		rawstrng = input("\n\tCiphertext: ")
		
		flag = ciphcheck(rawstrng)
	
	# Converts the ciphertext to non-negative integers.	
	numlist = intconvert(rawstrng)
	
	print("\n\t*computing plaintexts*")
	
	# Gets all possible plaintexts.
	deciphered_strnglst = matrices(numlist)
	
	print("\n\t*analyzing plaintexts*")
	
	# Determines likeliest plaintexts.
	results = splitter(deciphered_strnglst)
	
	# Scores plaintexts by likelihood of containing several English words.
	# Scores are integer values corresponding to length of individual 
	# clusters of letters within each plaintext, and whether each cluster is
	# an English word or not.
	resultslst = results.values()
	
	# Obtains the highest score (i.e., integer value), and the next few steps print out
	# any plaintexts with this score.
	m = max(resultslst)
	
	print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
	"_ _ _ _ _ _ _ _ _ _ _ _")
	print("|Most likely plaintext(s) is/ are:\t\t\t\t\t\t    |")
	print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ " +
		"_ _ _ _ _ _ _ _ _ _ _ _|\n")
	
	for n in results:
		if results[n] == m:
			print("\t'" + n.strip() + "'")
		else:
			continue
	
