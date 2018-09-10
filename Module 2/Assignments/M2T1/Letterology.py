# Aaron Bolyard
# 2018-09-10
# Contains letter operations.
# M2T1, CSC-221

VOWELS = [ 'a', 'e', 'i', 'o', 'u' ]

def has_which_vowels(string):
	"""
	Subset of has_which_vowels which only searches for vowels.
	"""
	return has_which_letters(string, VOWELS)

def has_which_letters(string, letters):
	"""
	Returns a set of letters from 'letters' in 'string'.
	"""

	# THe operation should be case insensitive
	string = string.lower()
	result = set()
	for letter in letters:
		letter = letter.lower()
		if letter.lower() in string:
			result.add(letter)
	return result
