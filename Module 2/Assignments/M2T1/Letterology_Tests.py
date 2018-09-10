# Aaron Bolyard
# 2018-09-10
# Unit tests for letter operations from Letterology.
# M2T1, CSC-221

import Letterology

# has_which_vowels tests
def test_has_which_vowels_partial_match():
	result = Letterology.has_which_vowels("Hello, world!")

	assert('a' not in result)
	assert('e' in result)
	assert('i' not in result)
	assert('o' in result)
	assert('u' not in result)

def test_has_which_vowels_no_match():
	result = Letterology.has_which_vowels("Bwlchgwyn")

	assert(len(result) == 0)

def test_has_which_vowels_complete_match():
	result = Letterology.has_which_vowels("The quick brown fox jumped over the lazy dog.")

	assert('a' in result)
	assert('e' in result)
	assert('i' in result)
	assert('o' in result)
	assert('u' in result)

# Not in assignment, but good idea.
def test_has_which_vowels_case_comparison():
	result = Letterology.has_which_vowels("hEllO, woRld!")

	assert('a' not in result)
	assert('e' in result)
	assert('i' not in result)
	assert('o' in result)
	assert('u' not in result)

# has_which_letters test
def test_has_which_letters_common():
	result = Letterology.has_which_letters("Hello, world!", "hw")

	assert('h' in result)
	assert('e' not in result)
	assert('l' not in result)
	assert('o' not in result)
	assert('w' in result)
	assert('r' not in result)
	assert('l' not in result)
	assert('d' not in result)

def test_has_which_letters_partial_match():
	result = Letterology.has_which_letters("abcdefgtest_hijklmnopqrtstuvwxyz", "abc")

	assert('a' in result)
	assert('b' in result)
	assert('c' in result)
	assert(len(result) == 3)

def test_has_which_letters_no_match():
	result = Letterology.has_which_letters("abcdefgtest_hijklmnopqrtstuvwxyz", "$")

	assert(len(result) == 0)

# Not in assignment, but good idea.
def test_has_which_letters_symbol():
	result = Letterology.has_which_letters("To be or not to be?; that is the question.", "?;")

	assert('?' in result)
	assert(';' in result)
	assert(len(result) == 2)

# Not in assignment, but good idea.
def test_has_which_letters_case_comparison():
	result = Letterology.has_which_letters("hEllO woRld!!", "hED")

	assert('h' in result)
	assert('e' in result)
	assert('d' in result)
	assert('E' not in result)
	assert('D' not in result)
	assert(len(result) == 3)

def test_has_which_letters_empty_input():
	result = Letterology.has_which_letters("How about that?", "")

	assert(len(result) == 0)
