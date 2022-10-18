#8. Write a program to accept a string and starting with first character replace every alternate character with the '*' character.
string=str(input("Enter String")); #Accept String

ch=[]

for i in string:  #Seperate string into array
    ch.append(i)
for j in range(1,len(ch),2): #Replace alternate character with *
    ch[j]="*"

s=''  
for k in ch: 
    s=s+k

print(s)
