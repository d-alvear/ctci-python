# IsUnique
# Implement an algorithm to determine if a string has all unique characters.
# What is you cannot use additional data structures?

# Inputs: a string of characters, I'm going to assume letters only
# Outputs: True/False
# Edge Cases: empty string? string with one character? For an empty string, we can immediately
#			  return False, a string with one character should technically return True since
#	 		  a string with one character makes the character unique.

# Some possible algorithms:
#	1. set up an empty list to hold chars we've seen already, iterate over chars in the string, 
#      check if the char is in the list, if not then append the char to the list, if the char is
#	   in the list then immediately return False, else return True.
#	2. set up a dict as a character counter, iterate over the string, adding chars to the dict as
#	   we go, and incrementing a char's value everytime we encounter it. Then we can check the dict
#	   for keys with values > 1, if there exists keys with a value > 1.
#	3. a quick check would be storing the length of the original length of the string, then creating
#	   a set from the string. A set will "remove" any duplicate characters. Then we can compare the
#	   length of the original string with the length of the set. 

# Runtime: iterating over the string will be O(n), then iterating over a dict will also be O(n), so
#			worst case the algorithm will have a runtime of O(2n) --> O(n)

# Approach 1:

def is_unique(str):
	if len(str) == 0:
		return "string is empty"

	else:
		if len(str) == len(set(str)):
			return True

		else:
			return False


print(is_unique('abracadabra'))
print(is_unique('dog'))
print(is_unique('hello'))
print(is_unique('charlie'))
print(is_unique(''))

