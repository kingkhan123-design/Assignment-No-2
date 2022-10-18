#10.Write a program to accept a string and convert all its characters to upper case.

string=str(input("Enter String \n")); #Accept String

for i in range (0,len(string)):
   x=ord(string[i]) #ord used for get number of character
   
   if x>=97 and x<=122: #Compare characters number with the code
       x=x-32
       
   y=chr(x)
   print(y,end="")
