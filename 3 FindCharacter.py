#3. Write a program to accept a string and a position P. Print the character at position P in the string.

string =str(input("Enter String \n"));   #Accept String

c = str(input("Enter Alphabet \n")); # Character to find

res = 0
for i in range(0, len(string)):  #Find character in string
	if string[i] == c:
		res = i
		break
	
if res == 0:
	print("No alphabet available in string") #If alphabet not available in string
else:
	print("Character {} is present at {}".format(c, str(res)))
