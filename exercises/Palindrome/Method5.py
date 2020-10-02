# Method using flag: In this method user compare each character from starting and ending in a for loop and 
# if the character does not match then it will change the status of the flag. 
# Then it will check the status of flag and accordingly and print whether it is a palindrome or not. 

# Python program to check
# if a string is palindrome or not
st = 'malayalam'
j = -1
flag = 0
for i in st:
	if i != st[j]:
	j = j - 1
	flag = 1
	break
	j = j - 1
if flag == 1:
	print("NO")
else:
	print("Yes")
