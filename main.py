import tkinter
from tkinter import *
import tkinter.messagebox
import hashlib
import pyperclip






def hash1():
    password = entry1.get()
    f = open('Common Passwords', 'a')
    f.write('\n'+password)
    f.close()
    password = password.encode('utf-8')

    hashPass = hashlib.md5(password).hexdigest()
    pyperclip.copy(hashPass)
    tkinter.messagebox.showinfo("Results Copied", "Hash was copied to Clip-Board")
    tkinter.messagebox.showinfo("Hash Results", hashPass)
    entry1.delete(0, END)

def unhash():
    hash = entry1.get()
    f = open('Common Passwords','r')
    for lines in f:
        commonPass = lines.strip()
        commonPass = commonPass.encode('utf-8')
        hashPass = hashlib.md5(commonPass).hexdigest()
        if hashPass == hash:
            commonPass = str(commonPass)
            #commonPass = re.sub('[^A-Za-z0-9]+', '', commonPass)
            pyperclip.copy(commonPass)
            print('Password is: '+commonPass)
            tkinter.messagebox.showinfo("Results Copied", "Password was copy to clip-Board")
            tkinter.messagebox.showinfo("Decrypted Result", commonPass)
            entry1.delete(0, END)
            break
        else:
            print('Hash match not found')

def closeApp():
    root.destroy()



#Home Screen
root = tkinter.Tk()
root.geometry("550x175")
root.title("Hash in a Dash")

#Label Frame
Label1 = LabelFrame(root, text="Users Information")
Label1.pack(fill="both", expand="yes")

#User input fields
header1 = Label(Label1, text='Enter Password or Hash', bg='green', fg='white')
header1.place(x=0, y=5)
entry1 = Entry(Label1, bd=4)
entry1.place(x=0, y=55, width=500)

Button1 = Button(Label1, text='Encrypt Password', bg='green', fg='white', bd=3, command=hash1)
Button1.place(x=0, y=100,  width=110)
Button2 = Button(Label1, text='Decrypt Password', bg='green', fg='white', bd=3, command=unhash)
Button2.place(x=130, y=100, width=110)
Button3 = Button(Label1, text='Cancel', bg='green', fg='white', bd=3, command=closeApp)
Button3.place(x=400, y=100, width=100)





root.mainloop()