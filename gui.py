from tkinter import *
from tkinter import messagebox
import pyttsx3
w=Tk()
w.title("BEBOP..")
w.geometry('250x150')
f="Verdana 10 bold"
l=Label(w,text='\U0001F916 BEBOP BOT \U0001F916',fg="black",font = f)
l.pack()
engine = pyttsx3.init()
engine.say("Starting Chatbot")
engine.runAndWait()

def call():
    a.configure(text='Initializing BEBOP Bot')
    e=pyttsx3.init()
    e.say("Initializing BEBOP")
    e.runAndWait()
    import Chatbot
    
def des():
    messagebox.showinfo("Exit", "Terminating Bebop")
    e = pyttsx3.init()
    e.say("Terminating BEBOP")
    e.runAndWait()
    w.destroy()
b=Button(w,text='Start',font=f, activeforeground="white",activebackground="grey",command=call)
b.pack()
a=Label(w,text='')
a.pack()
b1=Button(w,text='Exit',font=f, activeforeground="white",activebackground="grey",command=des)
b1.pack()
w.mainloop()