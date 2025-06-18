try:

 file = open('sample.txt','r')
 reading_file=file.read()
 print(reading_file)
 file.close()
except FileNotFoundError:
 print("Error: The file \'sample.txt\' not found")
