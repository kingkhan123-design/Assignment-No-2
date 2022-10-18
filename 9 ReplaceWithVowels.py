#9. Write a program to accept a string and replace every vowel in the string with the '*' character.

string=str(input("Enter String \n")); #Accept string
char="*"
newstr = ""
for i in range(len(string)): 
    if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'or string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or string[i]=='U':
            #Chech every character of string is vowles or not.
        newstr = newstr + char
    else:
        newstr = newstr + string[i]


print("String after replacing vowels to character", newstr)
