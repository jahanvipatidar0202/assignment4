# assignment4
# Task1
This Python program demonstrates how to read the contents of a text file using exception handling. It attempts to open and read a file named sample.txt. If the file is not found, it gracefully handles the error and displays an appropriate message.
# Task1 code

try:
 file = open('sample.txt','r')
 reading_file=file.read()
 print(reading_file)
 file.close()
except FileNotFoundError:
 print("Error: The file \'sample.txt\' not found")

 # Task1 sample.txt file
 Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.

# Task2
This Python script demonstrates how to perform basic file operations:
- Writing to a file
- Appending data to the same file
- Reading and displaying the file content
  # Features
- Prompts the user to input text and writes it to `output.txt`
- Prompts the user again to append more text to the same file
- Reads and prints the final content of `output.txt`
  # Task 2 code
 message = input("Enter text to write to a file:")
file = open('output.txt','w')
file.write(message)
print("Data successfully written to output.txt.")
file.close()

append_txt = input("Enter additional text to append :")
file = open('output.txt','a')
file.write(append_txt)
print("Data successfully appended")
file.close()

file = open('output.txt','r')
reading_file = file.read()
print("Final content of output.txt")
print(reading_file)
file.close()
# Task2 output.txt file
Hello, Python!Learning file handling in python
