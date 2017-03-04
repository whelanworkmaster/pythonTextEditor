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

text = tkinter.Text(top)
text.grid()

buttonSave = tkinter.Button(top, text = "Save", command = saveFunc)
buttonSave.grid()

buttonOpen = tkinter.Button(top, text = "Open", command = openFunc)
buttonOpen.grid()

top.mainloop()