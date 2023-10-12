from nuts_and_bolts.matrix import alph

def matrices(numlist):
	"""First, this function runs through all possible 2x2 invertible
	matrices modulo 27, keeping only those that are invertible. If a 
	matrix is invertible, it becomes a key in the dct dictionary. Next,
	the function uses this matrix key to transform the ciphertext into a 
	possible plaintext, and then stores it along with the matrix.
	Finally, the function returns a Set() of all the possible 
	plaintext values, so as to eliminate possible duplicates."""
	
	dct = {}

	for a in range(1, 27):
		for b in range(1, 27):
			for c in range(1, 27):
				for d in range(1, 27):
					det = a * b - c * d
				
					for i in range(1, 27):
						if (i * det) % 27 == 1:
							dct[(a, b, c, d)] = ''
		
	# The matrix multiplication is performed here.					
	for i in range(len(numlist)):
		if i % 2 == 0:
			continue
		else:
			for x in dct:
				
				chr1 = (x[0] * numlist[i-1] + x[1] * numlist[i]) % 27
				chr2 = (x[2] * numlist[i-1] + x[3] * numlist[i]) % 27
		
				# This step takes the integer values computed by matrix multiplication
				# and converts them into the letters making up the possible plaintext.
				chr1 = alph(chr1)
				chr2 = alph(chr2)
		
				dct[x] = dct[x] + chr1 + chr2

	return set(dct.values())
