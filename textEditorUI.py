import tkinter
import tkinter.filedialog

def saveFunc():
	global text

	t = text.get("1.0", "end-1c")
	saveFileName = tkinter.filedialog.asksaveasfilename()
	file = open(saveFileName, "w+")
	file.write(t)
	file.close()

top = tkinter.Tk()

text = tkinter.Text(top)
text.grid()

button = tkinter.Button(top, text = "Save", command = saveFunc)
button.grid()

top.mainloop()