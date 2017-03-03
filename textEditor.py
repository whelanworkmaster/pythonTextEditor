import sys
import os.path

def askInput():
	print("Welcome to Whelan's text editor")
	print("Menu Keys: Open File = o; New File = n; Close Program = x")
	selection = input("Please enter a key: ")
	if selection == "x":
		sys.exit(0)
	elif selection == 'n':
		newFile()
	elif selection == 'o':
		fileName = ''
		openFile(fileName)

def newFile():
	fileName = input("Please input file name: ") + '.txt'
	if(os.path.isfile(fileName)):
		print("File exists")
		selection = input("Enter n if you want to overwrite old file, o if you want to open old file: ")
		if selection == 'n':
			writeFile(fileName)
		elif selection == 'o':
			openOldFile(fileName)
	else:
		writeFile(fileName)

def writeFile(fileName):
	print("Creating new text file")

	#try:
	file = open(fileName, 'a')
	print("File Created, Write file now, when finished, enter /exit")
	loopCheck = 1
	while loopCheck > 0:
		newLine = input()
		#print(loopCheck)
		if newLine == "/exit":
			loopCheck = 0
		else:
			file.write(newLine + "\n")

	file.close()

	#except:
	#	print("Didnt work")
	#	sys.exit(0)

def openFile(filePath):
	if filePath == '':
		print("Opening txt file, please provide file path: ")
		filePath = input()
	file = open(filePath, 'r')
	for line in file:
		print(line)



askInput()