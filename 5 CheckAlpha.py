#5. Write a program to accept a string and check if all the characters in the string are alphabets.

import re   #Import Re( regula expression)

String=str(input("Enter string \n")); #Accept String

match = re.match('^[a-zA-Z]+$', String ) #compare aplabhet with string

if match:
    print('The string contains only letters')
else:
    print('The string does NOT contain only letters')
