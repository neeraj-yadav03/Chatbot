from tkinter import *
from tkinter import messagebox
import webbrowser
import random
import datetime
import pyttsx3
# GUI
root = Tk()
root.title("BeBot")
frame = Frame(root)
frame.pack()

BG_GRAY = "#17202A"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if (user == "hello" or user == "hi" or user == "hii" or user == "hiiii"): 
        list=['hello','hi','namaste','vanakam']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )
    
    # To open browser
        
    elif (user == "open google" or user == "google" or user == "search something"):
        txt.insert(END, "\n" + "BeBot -> Opening Google..")
        engine = pyttsx3.init()
        engine.say("Opening Google..")
        engine.runAndWait()
        webbrowser.open("https://www.google.com")
     
    # Calculator
    elif (user == "can you do math" or user == "calculator" or user == "open calculator"):
        txt.insert(END, "\n" + "BeBot -> Sure! Opening Calculator...")
        engine = pyttsx3.init()
        engine.say("Sure! Opening Calculator...")
        engine.runAndWait()
        import Cal
     
     # Date and Time   
    elif (user == "what time is it" or user == "time" or user == "date"):
        now = datetime.datetime.now()
        t=now.strftime("%Y-%m-%d %H:%M:%S")
        txt.insert(END, "\n" + "BeBot -> *tick* *tick*\n" + t)
       
    # responses
    elif (user == "how are you"):
        list=['Im fine','Good','Im doing great!']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )
        
        
    elif (user == "what can you do?" or user == "what can you do"):
        list=['I can say something funny','I can sing!',"I'm good at Math",'You tell me..']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )

    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        list=['That is great','Good to hear that!','Hmmmmmm','Nice']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )
        
    elif (user == "what do you eat?" or user == "do you eat?" or user == "you like food?"):
        list=["Well i'm a bot so I don't eat",'I like Waffles!','I do! I take big *Bytes*','Seriously?']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )
        
    elif (user == "who are you" or user == "who are you?" or user == "what is your name?" or user == "what do i call you?"):
         list=['Yes I do! I am Bebop..','You can call me Bebop',"I'm Bebop, your Chatbot",'My name is Bebop, your Chatbot']
         r= random.choice(list)
         txt.insert(END, "\n" + "BeBot -> " + r )

    elif (user == "thanks" or user == "thank you" or user == "thanks bebop"):
        list=['Your welcome','welcome','My pleasure','Any time']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )

    elif (user == "your fav song?" or user == "suggest me a song" or user == "do you listen to music?" or user == "sing me a song"):
        list=['Yes,*clears throat* Konisthane coka...coka..coka..',
              'Listen to this song, *Jagamanta kutaumbam naadhi \n aaekaki jeevitam naadhi*',
              'Listen to liger theme song...']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )
        
    elif (user == "tell me a joke" or user == "tell me something funny" or user == "can you tell me a joke?"):
        list=["Do you know about the pc monster? It's taking big bytes",
              'how does our solar system keep its pants up?\n With an asteroid belt',
              'I like to think I am prety down to Earth because well...GRAVITY'
              ,'What do you call a bee that lives in America? \n U S B']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )
     
     # Exit 
    elif (user == "goodbye" or user == "see you later" or user == "see yaa" or user == "bye"):
        list=['Thanks for using BEBOP','bye','see ya!','malli ra vro']
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )
        engine = pyttsx3.init()
        engine.say("Thanks for using BEBOP")
        engine.runAndWait()
        messagebox.showinfo("Exit", "Thanks for using BEBOP ")
        root.destroy()
        

    else:
        list=["Could you please re-phrase that? ",
                    "...",
                    "Sounds about right.",
                    "What does that mean?"]
        r= random.choice(list)
        txt.insert(END, "\n" + "BeBot -> " + r )

    e.delete(0, END)


lable1 = Label(frame,bg=BG_COLOR, fg=TEXT_COLOR ,text="Welcome User", font=FONT, pady=10, width=20, height=1).grid(row=0)

txt = Text(frame, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(frame, bg=BG_GRAY, fg='white', font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(frame, text="Send", font=FONT_BOLD,fg="white" ,bg=BG_GRAY,
            command=send).grid(row=2, column=1)

root.mainloop()
