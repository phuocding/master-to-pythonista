# Method using one extra variable: In this method user take a character of string one by one and store in an empty variable. 
# After storing all the character user will compare both the string and check whether it is palindrome or not. 

# Python program to check
# if a string is palindrome or not

x = "malayalam"

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")

