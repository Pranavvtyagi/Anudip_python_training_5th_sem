'''
To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file
'''
#Open the File in read mode
file = open("sample.txt","r")
content = file.read()
#Count Vowels in the file
vowels = 0
for ch in content:
    if ch.lower in "aeiou":
        vowels = vowels+1
#Count characters in the file
character = len(content)
#Count Lines in the File
lines = content.count("\n")+1
# Display results
print("Number of vowels:", vowels)
print("Number of characters:", content)
print("Number of lines:", lines)
file.close()
 

