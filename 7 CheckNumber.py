#7. Write a program to accept a string and check if all the characters in the string are digits.

import re   #Import Re( regula expression)

String=str(input("Enter string \n")); #Accept String


match = re.match('^[0-9]+$',String ) #compare aplabhet and numbers with string

if match:
    print('The all character in the string are numbers')
else:
    print('The all character in the string are not numbers')
