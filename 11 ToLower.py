#11. Write a program to accept a string and convert all its characters to lower case.
string = str(input("Enter String"));
out = ''
for i in string:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        out = out + i
    else:
        k = ord(i)
        l = k + 32
        out = out + chr(l)
print(out)    

