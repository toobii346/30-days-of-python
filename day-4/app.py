# Day 4: String Methods and Comparison Operators

first_name = "tobi"
last_name = "eboka"
language = "python"
challenge = "30DaysOfPython"

print("Capitalize:", first_name.capitalize())    
print("Title:", challenge.title())                
print("Upper:", language.upper())                  
print("Lower:", challenge.lower())                 
print("Swapcase:", first_name.swapcase())          

print("Replace:", challenge.replace("Python", "JavaScript"))

print("Find 'Days':", challenge.find("Days"))      
print("Index 'P':", challenge.index("P"))          

print("Starts with '30':", challenge.startswith("30"))  
print("Ends with 'Python':", challenge.endswith("Python"))  

print("Split:", challenge.split("Of"))             

text = "   Hello, world   "
print("Strip:", text.strip())                      

print("Equal:", 5 == 5)        
print("Not equal:", 5 != 3)    
print("Greater than:", 7 > 4)   
print("Less than or equal:", 2 <= 2)  
