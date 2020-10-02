# Method using inbuilt function to reverse a string: In this method, predefined function ‘ ‘.join(reversed(string)) is used to reverse string. 
# Below is the implementation of the above approach: 

# function to check string is 
# palindrome or not
def isPalindrome(s):
	
	# Using predefined function to 
	# reverse to string print(s)
	rev = ''.join(reversed(s))

	# Checking if both string are 
	# equal or not
	if (s == rev):
		return True
	return False

# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")
