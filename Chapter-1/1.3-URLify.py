# URLify
# Write a method to replace all spaces in a string with '%20'. You may assume that the
# string has sufficient space at the end to hold the additional characters, and that 
# you are given the "true" length of the string.

# Ex. 'Mr John Smith  ',13 --> 'Mr%20John%20Smith'


# Approach 1: Simple Python Solution
def urlify(string, length):
	if (string == None) or (string == ""):
		return "Not a valid string"

	else:
		string = string.strip() #removes whitespace from string
		string = string.replace(" ", "%20")

	return string

# Approach 2: The Expected Solution
def urlify(string, length):
	if (string == None) or (string == ""):
		return "Not a valid string"

	string = list(string)
	new_length = len(string)

	for i in reversed(range(length)):
		if string[i] == " ":
			string[new_length-3:new_length] = '%20'
			new_length -= 3

		else:
			string[new_length-1] = string[i]
			new_length -= 1

	return "".join(string)



 print(urlify("much ado about nothing      ", 22))
 print(urlify("Mr John Smith    ", 13))
 print(urlify("Abracadabra", 11))
 print(urlify(None,None))
