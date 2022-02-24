str1 = input("Enter str1: ")
str2 = input("Enter str2: ")
charCount = 0
minLength = 0

if len(str1) > len(str2):
    minLength = len(str2)
else: 
    minLength = len(str1)

while minLength > 0:
    minLength -= 1
    if str1[minLength] == str2[minLength]:
        charCount += 1
        
print("Result: ", charCount);
    