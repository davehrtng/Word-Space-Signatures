class Vector:

	def __init__(self, elementList = []):
		self.elementList = elementList
	
		
	def dotProduct(self, otherVector):
		"""Returns the dotProduct of self and otherVector. Returns None if cannot compute."""
		
		# check if lengths are same
		if len(self.elementList) != len(otherVector.elementList):
			return None
		
		result = 0
		
		for i in range(len(self.elementList)):
			result += self.elementList[i] * otherVector.elementList[i]
		
		return result
	
	def hammingDistance(self, otherVector):
		"""Treats vectors as bit-vectors (any number greater than 0 treated as 1). Computes minimum number of substitutions requried to make vectors identical"""
		if len(self.elementList) != len(otherVector.elementList):
			return None
			
		bits = int(self.toBitString(), 2)
		oBits = int(otherVector.toBitString(), 2)
		
		# xor will catch the differences
		xor = bits & oBits
		
		# count up the 1s in xor for the number of differences
		return bin(xor).count('1')
		
	def euclidianDistance(self, otherVector):
		"""Returns the vector distance between self and otherVector. Returns None if cannot compute."""
		#check if lengths are the same
		if len(self.elementList) != len(otherVector.elementList):
			return None
			
		result = 0
		
		for i in range(len(self.elementList)):
			result += (self.elementList[i] - otherVector.elementList[i])**2
			
		return result**.5
		
	def toBitString(self):
		result = '0b'
		for el in self.elementList:
			if el == 0:
				result += '0'
			else:
				result += '1'
		return result

def main():
	v1 = Vector([1,2,3, 4, 5])
	v2 = Vector([1,2,3, 4, 5])
	print(v1.dotProduct(v2))
	print(v1.distance(v2))
		
if __name__ == "__main__":
	main()
