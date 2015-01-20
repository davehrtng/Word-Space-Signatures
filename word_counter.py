from vector import Vector

class WordCounter:
	
	def __init__(self):
		"""Creates a new, empty WordCounter"""
		self.wordCountDict = {}
		
	def count(self, word):
		"""Counts a single word (string), by updating wordCountDict"""
		if word in self.wordCountDict: #actually faster than word in wordCountDict.keys()
			self.wordCountDict[word] += 1
		else:
			self.wordCountDict[word] = 1
			
	def addKeys(self, wordList):
		"""Adds all words in wordList wordCountDict with a count of 0"""
		for word in wordList:
			if word not in self.wordCountDict: # verify that not in wordCountDict
				self.wordCountDict[word] = 0
			
	def uniqueWordCount(self):
		"""Returns the number of unique words counted"""
		return len(self.wordCountDict.keys())
	
	def totalWordCount(self):
		"""Returns the total number of words counted"""
		return reduce(lambda x, y: x+y, self.wordCountDict.values())
		
	def toVector(self):
		"""Returns a Vector representation of the WordCounter. The location of the counts is by alphabetical order of words. So the count of the first word alphabetically gets position 0."""
		wordCountTupleList = sorted(self.wordCountDict.items())
		
		elementList = map(lambda wordCountTuple: wordCountTuple[1], wordCountTupleList)
		
		return Vector(elementList)
		
	