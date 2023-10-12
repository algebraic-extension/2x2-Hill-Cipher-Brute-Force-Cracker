def intpull():
	"""This function determines that the user puts in proper values
	for their matrix.
	"""
	
	flag1 = True
	flag2 = True
	flag3 = True
	flag4 = True
	
	while flag1:
		w = input("\n\ta = ")
		try:
			a = int(w)
			if (a % 1 == 0):
				flag1 = False
		except ValueError:
			print("\tPlease enter an integer.")
	
	while flag2:
		x = input("\tb = ")
		try:
			b = int(x)
			if (b % 1 == 0):
				flag2 = False
		except ValueError:
			print("\tPlease enter an integer.\n")
			
	while flag3:
		y = input("\tc = ")
		try:
			c = int(y)
			if (c % 1 == 0):
				flag3 = False
		except ValueError:
			print("\tPlease enter an integer.\n")
			
	while flag4:
		z = input("\td = ")
		try:
			d = int(z)
			if (d % 1 == 0):
				flag4 = False
		except ValueError:
			print("\tPlease enter an integer.\n")
	
	intlst = [a % 27, b % 27, c % 27, d % 27]
	
	return intlst
	
def detcheck(lst):
	"""This function uses the integers given by the user to determine if
	that matrix has an inverse modulo 27.
	"""
	
	# The denominator of the determinant is computed below.
	flag = False
	det = (lst[0] * lst[3]) - (lst[1] * lst[2])
	retlst = []
	
	while det < 0:
		det += 27
	
	gcdlst = []
	for i in range(1, det + 1):
		if (det % i == 0) and (27 % i == 0):
			gcdlst.append(i)
		else: 
			continue
			
	if (len(gcdlst) > 1) or (((lst[0] * lst[3]) - (lst[1] * lst[2])) == 0):
		print("\n\tThis matrix does not have an inverse modulo 27. ")
		print("\tPlease try different integers.")
		
	else:
		flag = True
		
	return flag
