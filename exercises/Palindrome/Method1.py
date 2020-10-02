# 1) Find reverse of string 
# 2) Check if reverse and original are same or not.
# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]

# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
