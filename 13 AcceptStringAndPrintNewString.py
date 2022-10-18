#13.Extract from the given string STR, starting from position P, L characters into another string STR2. e.g. STR1="BATATA", P=2, L=4. Then STR2="ATAT".
STR1=str(input("Enter string"));
P=int(input("Enter Position")); #Accept Position
L=int(input("Enter Length")); #ACcept Length
STR2=STR1[P:L+1]
print(STR2)
               
