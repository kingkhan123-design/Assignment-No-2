#2.Write a program to accept a string and reverse it.

def reverse(string):  #Create a function for the reverse string
    str = ""
    for i in string:   #Reverse string using for loop
        str = i + str
    return str
  
string = str(input("Enter String \n")); #Accept String
  
print("The original string is : ",string)
  
print("The reversed string(using loops) is : ",reverse(string), end="")

