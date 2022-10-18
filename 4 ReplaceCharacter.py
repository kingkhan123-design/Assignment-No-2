#4. Write a program to accept a string, a position P and a character T. Replace the character at position P in the string with character T.

string = str(input("Enter String"));   #Accept String

position = int(input("Enter Position"));  #Accept position

character = str(input("Enter String"));   #Accept character

string = string[:position] + character + string[position+1:]  #create new string using string slicing
print(string)
