''' Write a program to copy entire content from one file into another'''
#-----------------------------------------------------------------------
# Open source file in read mode
file1 = open("sample.txt", "r")
content = file1.read()
# Open destination file in write mode
file2 = open("sentences.txt", "w")
file2.write(content)
#Copy file
print("File copied successfully!")
file1.close()
file2.close()