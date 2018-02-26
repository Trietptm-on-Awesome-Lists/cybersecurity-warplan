def HammingDistance(x,y):
	"""
	Caclulate tha hamming distance
	"""
	return bin(x^y).count('1')
