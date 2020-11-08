# single window application

from tkinter import *
from tkinter import messagebox
import json

def loadJsonData():
    mcqs = json.loads(open("quizApp/data.json","r").read())
    q_dict = mcqs[0]
    option_dict = mcqs[1]
    return (q_dict,option_dict)

def setMcqs():
    
    # get quetion list
    q_dict,option_dict = loadJsonData()

    # default intialization
    r = IntVar()
    key = 1

    # set quetion
    text = q_dict.get(str(key),"")
    lblText = Label(root,text=text,justify="center",wraplength=400,width=500,font=(18))
    lblText.pack(pady=(20,10))

    # set options
    Optionvalue = option_dict.get(str(key),[])
    val = 1
    r = IntVar()
    for option in Optionvalue:
        Radiobutton(root,text=option,variable=r,value=val,width=30,font=("Sans",15),relief=GROOVE).pack(pady=(10,0))
        val += 1
    

def startQuiz():
    label_img1.destroy()
    label_text.destroy()
    button_start.destroy()
    instr_label.destroy()
    lblRules.destroy()
    setMcqs()


# create windows screen
root = Tk()
root.title("QuizStar")
root.geometry("650x500")
root.config(background="white")
root.resizable(0,0)

# create image(logo) for label
logo = PhotoImage(file="quizApp/exam.png")
logo = logo.subsample(5, 5)  # divide height and width by 4
# logo configration
label_img1 = Label(root, image=logo, background="#ffffff")
label_img1.pack()

# set main label 
label_text = Label(root,text="QuizStar",font=("ComicSansMS",24,"bold"),background="#ffffff")
label_text.pack()

# image button and configration
btnImg = PhotoImage(file="quizApp/Frame.png")
button_start = Button(root,image=btnImg,relief=FLAT,border=0,background="#ffffff",command=startQuiz)
button_start.pack(pady=(15,0)) # padding by top

# instruction label
instr_label = Label(root,text="Before the Click on Start button\nread below instruction",background="#ffffff",font=("Consolas",14),justify="center")
instr_label.pack()

# rules
lblRules = Label(root,text="This quiz contains 10 quetions\nYou will get 20 seconds to solve a quetion\nOnce you select a radio that will be a final choice\nhence think before you select",width=100,background="#000000",foreground="#ffffff",font=("Times",14))
lblRules.pack(pady=(60,0))

# change frame using loop
root.mainloop()
