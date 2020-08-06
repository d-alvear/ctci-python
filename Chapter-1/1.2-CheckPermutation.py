# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other

# Clarify the Problem
# 	What is a permutation:
#	-- A Permutation of a string is another string that contains same characters, only 
#		the order of characters can be different. For example, “abcd” and “dabc” are 
#		Permutation of each other.

# Inputs: two strings; Outputs: True/False
# Test/Edge Cases: empty strings, a string == None

# Possible Algorithms:
#	1. We could implement a dict for each string to keep track of how many times each 
#		char appears in a string, then check if the dicts are equal to each other.
#	2. Like the last problem, checking the length of the strings is an easy and quick
#		way to check if the string are not permutations. If then lengths aren't equal 
#		then the strings can't be permutations
#	3. Use a combo of algs 1 & 2; ask if python built-ins can be used

import collections

def check_permutation(string_1, string_2):
	# check if either string is None
	if (type(string_1) == None) or (type(string_2) == None):
		return False

	else:
		if len(string_1) != len(string_2):
			return False

		else:
			c1 = collections.Counter(string_1)
			c2 = collections.Counter(string_2)

			if c1 == c2:
				return True
			else:
				return False
			


print(check_permutation("cat","dog"))
print(check_permutation("hasta manana", "ananam atsah"))
print(check_permutation("", "hello"))
print(check_permutation("apple","orange"))
print(check_permutation(" ", "3"))

# Should eval to:
# False
# True
# False
# False
# False
