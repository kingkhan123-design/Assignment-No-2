#6. Write a program to accept a string and check if all the characters in the string are alphanumeric.

import re   #Import Re( regula expression)

String=str(input("Enter string \n")); #Accept String


match = re.match('^[a-zA-Z0-9]+$',String ) #compare aplabhet and numbers with string

if match:
    print('The string is alphanumeric')
else:
    print('The string is not alphanumeric')
