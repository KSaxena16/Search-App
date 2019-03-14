from tkinter import *
import wikipedia

root = Tk()

def get_me():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        print("Please check your input or internet connection")

topframe = Frame(root)
entry = Entry(topframe)
entry.pack()

button = Button(topframe, text = "Search", command = get_me)
button.pack()
topframe.pack(side=TOP)

bottomframe = Frame(root)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer = Text(bottomframe,width=30, height=10, yscrollcommand = scroll.set, wrap=WORD)
answer.pack()
scroll.config(command=answer.yview)
bottomframe.pack()
root.mainloop()