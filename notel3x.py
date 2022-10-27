import tkinter as tk
from tkinter import *
from tkinter import filedialog

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 1000, height = 300, relief = 'raised')
canvas1.pack()

# Variables -------------------------------------------------------
showNoteManager = False
data = "Default.txt"
note = 0

# FUNCTIONS -------------------------------------------------------
def GetUsername():
    with open(data) as f:
        lines = f.readlines()
        return str(lines[1].strip())

def GetPassword():
    with open(data) as f:
        lines = f.readlines()
        return str(lines[2].strip())

def SignIn():
    global showNoteManager

    if entry1.get() == GetUsername() and entry2.get() == GetPassword():
        # hide stuff:
        canvas1.itemconfig(1, state='hidden')
        canvas1.itemconfig(2, state='hidden')
        canvas1.itemconfig(3, state='hidden')
        canvas1.itemconfig(4, state='hidden')
        canvas1.itemconfig(5, state='hidden')
        canvas1.itemconfig(6, state='hidden')
        canvas1.itemconfig(7, state='hidden')
        # show stuff:
        canvas1.create_window(500, 25, window=label4)
        canvas1.create_window(500, 45, window=label5)
        canvas1.create_window(500, 90, window=button2)
        canvas1.create_window(500, 120, window=label6)
        canvas1.create_window(500, 200, window=listbox1)
        LoadLastNotesList()
        canvas1.create_window(500, 280, window=button3)
        canvas1.create_window(920, 20, window=button13)
    else:
        if showNoteManager == False:
            canvas1.create_window(500, 240, window=label1)
            showNoteManager = True

def LoadLastNotesList():
    listbox1.delete(0,END)
    with open(data) as f:
        lines = f.readlines()
        num1 = int(lines[0].strip()) + 1

        for i in range(num1):
            for j in range(len(lines)):
                if lines[j].strip() == ("$$" + str(i)).strip():
                    listbox1.insert(j, lines[j+1].strip())

def OpenNote():

    for s in listbox1.curselection():
        note = s

    with open(data) as f:
        lines = f.readlines()

        for i in range(len(lines)):
            if lines[i].strip() == "$$" + str(note):
                titulo = lines[i+1].strip()

    #Open note editor in new window
    win = Toplevel(root)
    win.title(titulo)
    canvas2 = tk.Canvas(win, width = 1000, height = 300, relief = 'raised')
    canvas2.pack()

    label7 = tk.Label(win, text='Title:')
    label7.config(font=('helvetica', 11))
    canvas2.create_window(500, 25, window=label7)

    entry3 = tk.Entry (win)
    canvas2.create_window(500, 50, window=entry3)

    label8 = tk.Label(win, text='Text:')
    label8.config(font=('helvetica', 11))
    canvas2.create_window(500, 80, window=label8)

    button4 = tk.Button(win, text='SAVE NOTE', command=lambda: saveNote(str(entry3.get()),str(Preview.get("1.0",'end-1c')),win,note), bg='black', fg='white', font=('helvetica', 9, 'bold'))
    canvas2.create_window(500, 270, window=button4)

    Preview = Text(win, height = 9, width = 60)
    canvas2.create_window(500, 170, window=Preview)

    #Set texts
    with open(data) as f:
        lines = f.readlines()

        for i in range(len(lines)):
            if lines[i].strip() == "$$" + str(note):
                entry3.insert(tk.END, lines[i+1].strip())
                Preview.insert(tk.END, lines[i+2].strip())

def CreateNote():
    #Open note editor in new window
    win = Toplevel(root)
    win.title("EDITING NEW NOTE")
    canvas2 = tk.Canvas(win, width = 1000, height = 300, relief = 'raised')
    canvas2.pack()

    label7 = tk.Label(win, text='Title:')
    label7.config(font=('helvetica', 11))
    canvas2.create_window(500, 25, window=label7)

    entry3 = tk.Entry (win)
    canvas2.create_window(500, 50, window=entry3)

    label8 = tk.Label(win, text='Text:')
    label8.config(font=('helvetica', 11))
    canvas2.create_window(500, 80, window=label8)

    Preview = Text(win, height = 9, width = 60)
    canvas2.create_window(500, 170, window=Preview)

    button4 = tk.Button(win, text='SAVE NOTE', command=lambda: saveNewNote(str(entry3.get()),str(Preview.get("1.0",'end-1c')),win), bg='black', fg='white', font=('helvetica', 9, 'bold'))
    canvas2.create_window(500, 270, window=button4)

def saveNote(titleentry, bodyentry, win,noteIndex):
    with open(data) as f:
        lines = f.readlines()
         
        for i in range(len(lines)):
            if lines[i].strip() == "$$" + str(noteIndex):
                titIndex = i+1

        lines[titIndex] = titleentry + "\n"
        lines[titIndex+1] = bodyentry + "\n"

        with open(data, 'w') as file:
            file.writelines(lines)
    LoadLastNotesList()
    win.destroy()

def saveNewNote(titleentry, bodyentry, win):
    #Check and add 1 to lines lenght
    with open(data) as f:
        lines = f.readlines()
        num = int(lines[0].strip()) + 1
        lines[0] = str(num) + "\n"

        with open(data, 'w') as file:
            file.writelines(lines)

        #Create 3 new lines ($$X, Title, Body)
        with open(data, 'a') as f:

            f.write("$$" + str(num-1) + "\n")
            f.write(titleentry + "\n")
            f.write(bodyentry + "\n")

    LoadLastNotesList()
    win.destroy()

def openFile():
    global data
    # Get the file path and store it on "data" variable and update notes list
    stringpath = str(filedialog.askopenfilenames())
    replace = ["\"",",",")","(","'"]
    for i in range(len(replace)):
        stringpath = stringpath.replace(replace[i],"")

    canvas1.itemconfig(1, state='normal')
    canvas1.itemconfig(2, state='normal')
    canvas1.itemconfig(3, state='normal')
    canvas1.itemconfig(4, state='normal')
    canvas1.itemconfig(5, state='normal')
    canvas1.itemconfig(6, state='normal')
    canvas1.itemconfig(7, state='normal')
    for p in range(150):
        canvas1.itemconfig(p+8, state='hidden')
    data = stringpath
    LoadLastNotesList()

# GUI -------------------------------------------------------

# LOGIN PAGE
label1 = tk.Label(root, text="SAFE AND SECURE NOTES")
label1.config(font=('helvetica', 9))
canvas1.create_window(500, 45, window=label1)

label1 = tk.Label(root, text="MADE BY C0MPL3X#3733")
label1.config(font=('helvetica', 8))
canvas1.create_window(500, 280, window=label1)

label2 = tk.Label(root, text="LOGIN")
label2.config(font=('helvetica', 11))
canvas1.create_window(500, 100, window=label2)

label3 = tk.Label(root, text='NOTEL3X©')
label3.config(font=('helvetica', 14))
canvas1.create_window(500, 25, window=label3)

entry1 = tk.Entry (root)
canvas1.create_window(500, 140, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(500, 164, window=entry2)

button1 = tk.Button(text='SIGN-IN', command=SignIn, bg='black', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(500, 200, window=button1)

label1 = tk.Label(root, text="WRONG CREDENTIALS TRY AGAIN") 
label1.config(font=('helvetica', 7))

# NOTES MANAGER PAGE
label4 = tk.Label(root, text='NOTES MANAGER')
label4.config(font=('helvetica', 14))

label5 = tk.Label(root, text="HERE YOU CAN CREATE A NEW NOTE OR VIEW PREVIOUS ONES") 
label5.config(font=('helvetica', 9))

button2 = tk.Button(text='CREATE NEW', command=CreateNote, bg='black', fg='white', font=('helvetica', 9, 'bold'))

label6 = tk.Label(root, text="ALL NOTES") 
label6.config(font=('helvetica', 9))

listbox1 = tk.Listbox(root, height=7, width= 100)

button3 = tk.Button(text='OPEN SELECTED NOTE', command=OpenNote, bg='black', fg='white', font=('helvetica', 9, 'bold'))

button13 = tk.Button(text='SELECT DATA FILE', command=openFile, bg='black', fg='white', font=('helvetica', 9, 'bold'))

root.mainloop()