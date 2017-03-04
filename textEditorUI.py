import tkinter
import tkinter.filedialog

def saveFunc():
	global text

	t = text.get("1.0", "end-1c")
	saveFileName = tkinter.filedialog.asksaveasfilename()
	file = open(saveFileName, "w+")
	file.write(t)
	file.close()

def openFunc():
	global text

	openFile = tkinter.filedialog.askopenfilename()
	print(openFile)
	file = open(openFile, "r")
	newtext = file.read()
	text.insert("end", newtext)
	print(newtext)

top = tkinter.Tk()
top.title("Text Editor")

text = tkinter.Text(top)
text.pack()

buttonSave = tkinter.Button(top, text = "Save", command = saveFunc)
buttonSave.pack()

buttonOpen = tkinter.Button(top, text = "Open", command = openFunc)
buttonOpen.pack()

top.mainloop()