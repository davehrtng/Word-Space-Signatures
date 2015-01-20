import string
from vector import Vector
from word_counter import WordCounter

def clean(text):
	"""Returns text sans punctuation and numbers, and with all letters in lowercase. Only whitespace and letters remain."""
	delete = string.digits + string.punctuation
	text = string.translate(text, None, delete)
	text = string.lower(text)
	return text
	

def processFile(filename):
	"""Returns a WordCounter representing the text contained in the file with given filename"""
	file = open(filename, 'r')
	text = file.read()
	file.close()
	
	text = clean(text) # now only lowercase and whitespace
	
	words = text.split()
	
	wordCounter = WordCounter()
	
	for w in words:
		wordCounter.count(w)
		
	return wordCounter

def reconcileKeys(wc1, wc2):
	"""Adds keys to both WordCounters to make sure they have the same set of keys."""
	wc1Keys = wc1.wordCountDict.keys()
	wc2Keys = wc2.wordCountDict.keys()
	
	keysToAddList = []
	
	# find keys in wc1 not in wc2
	for key in wc1Keys:
		if key not in wc2Keys:
			keysToAddList.append(key)
	
	# find keys in wc2 not in wc1
	for key in wc2Keys:
		if key not in wc1Keys:
			keysToAddList.append(key)
			
	wc1.addKeys(keysToAddList)
	wc2.addKeys(keysToAddList)

def compare(filename1, filename2):
	"""Create WordCounters for each file and compute semantic distance between them."""
	wc1 = processFile(filename1)
	wc2 = processFile(filename2)
	
	reconcileKeys(wc1, wc2)
	
	v1 = wc1.toVector()
	v2 = wc2.toVector()
	
	result = {}
	
	result['dot'] = v1.dotProduct(v2)
	result['euclidian'] = v1.euclidianDistance(v2)
	result['hamming'] = v2.hammingDistance(v2)
	
	return result

def printResult(resultDict):
	"""Prints out key-value pairs in resultDict."""
	for k, v in resultDict.iteritems():
		print('\t' + k + '\t\t' + str(v))
	
def main():		
	print("Distance between Macbeth and Hamlet: ")
	printResult(compare('macbeth.txt', 'hamlet.txt'))
	print("Distance between Macbeth and Pride and Prejudice: ")
	printResult(compare('macbeth.txt', 'pride.txt'))
	print("Distance between Macbeth and industrial safety report: ")
	printResult(compare('macbeth.txt', 'industrialsafety.txt'))
	
if __name__ == "__main__":
	main()