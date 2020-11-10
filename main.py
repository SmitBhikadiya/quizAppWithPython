# single window application

from tkinter import *
from tkinter import messagebox
import json
import random
import threading
import time


user_answer = []
set_answer = []
right = 0
starting_time = 0
ending_time = 0
footer = None

def check_correct(que_number, selected):
    global right

    if str(que_number) in set_answer:
        if int(selected) == set_answer.get(str(que_number),0):
            print("True")
            right += 1 
        else:
            print("False")

def gen():
    global rand_list
    rand_list = []
    while True:
        rand = random.randint(1,10)
        if len(rand_list) == 10:
            break
        if rand in rand_list:
            pass
        else:
            rand_list.append(rand)

def loadJsonData():
    global set_answer
    mcqs = json.loads(open("quizApp/data.json", "r").read())
    q_dict = mcqs[0]
    option_dict = mcqs[1]
    set_answer = mcqs[2]
    return (q_dict, option_dict)

def getFormatedTime(t):
    t = int(t)
    if t>60:
        min_ = t//60
        sec_ = t%60
    else:
        min_ = 0
        sec_ = t
    if min_ < 10:
        if min_ == 0:min_ = int("00"+str(min_))
        else:min_ = int("0"+str(min_))
    if sec_ < 10:
        sec_ = int("0"+str(sec_))
    return str(min_)+" min "+str(sec_)+" sec"

def selectAns(index,c):
    global starting_time
    user_answer.append([rand_list[c-1],r.get()])
    check_correct(rand_list[c-1],r.get())
    lblText.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    index += 1
    c += 1
    if index > 10:
        ending_time = time.time()
        print(ending_time)
        taken_time = ending_time - starting_time
        taken_time = getFormatedTime(taken_time) 
        footer.destroy()
        root.quit()
        messagebox.showinfo("ScoreBoard","## Congrats ##\nScore : "+str(right)+"/10\nTime : "+str(taken_time))
    else:
        setMcqs(index,c)

def setMcqs(index,c):

    root.config(bg="#004455")

    global r
    global lblText
    global r1,r2,r3,r4

    # get quetion list
    q_dict, option_dict = loadJsonData()

    # default intialization
    r = IntVar()
    key = rand_list[index-1]

    # set quetion
    text = q_dict.get(str(key), "")
    lblText = Label(root, text="("+str(index)+") "+text, justify="center",wraplength=400, width=500, font=(18))
    lblText.pack(pady=(20, 10))

    options = option_dict.get(str(key),[])
    print(options)

    # set Mcqs
    r1 = Radiobutton(root,text=options[0],variable=r,value=1,font=("Sans",14),width=30,anchor=W,command=lambda : selectAns(index,c))
    r1.pack(pady=(10,0))
    r2 = Radiobutton(root,text=options[1],variable=r,value=2,font=("Sans",14),width=30,anchor=W,command=lambda : selectAns(index,c))
    r2.pack(pady=(10,0))
    r3 = Radiobutton(root,text=options[2],variable=r,value=3,font=("Sans",14),width=30,anchor=W,command=lambda : selectAns(index,c))
    r3.pack(pady=(10,0))
    r4 = Radiobutton(root,text=options[3],variable=r,value=4,font=("Sans",14),width=30,anchor=W,command=lambda : selectAns(index,c))
    r4.pack(pady=(10,0))

    if footer == None:
        setFooter()
    else:
        footer.destroy()
        setFooter()
        footer.config(text=str(index)+"/10")

def setFooter():
    global footer
    # set footer
    footer = Label(root,text="1/10",width=100,bg="#ffffff",fg="#000000",font=("Sans",20))
    footer.pack(pady=(40,0))

def startQuiz():
    global c
    global starting_time

    starting_time = time.time()

    label_img1.destroy()
    label_text.destroy()
    button_start.destroy()
    instr_label.destroy()
    lblRules.destroy()

    gen()
    index = 1
    c = 1
    print(rand_list)
    setMcqs(index,c)


# create windows screen
root = Tk()
root.title("QuizStar")
root.geometry("650x500")
root.config(background="white")
root.resizable(0, 0)

# create image(logo) for label
logo = PhotoImage(file="quizApp/exam.png")
logo = logo.subsample(5, 5)  # divide height and width by 4
# logo configration
label_img1 = Label(root, image=logo, background="#ffffff")
label_img1.pack()

# set main label
label_text = Label(root, text="QuizStar", font=(
    "ComicSansMS", 24, "bold"), background="#ffffff")
label_text.pack()

# image button and configration
btnImg = PhotoImage(file="quizApp/Frame.png")
button_start = Button(root, image=btnImg, relief=FLAT,
                      border=0, background="#ffffff", command=startQuiz)
button_start.pack(pady=(15, 0))  # padding by top

# instruction label
instr_label = Label(root, text="Before the Click on Start button\nread below instruction",
                    background="#ffffff", font=("Consolas", 14), justify="center")
instr_label.pack()

# rules
lblRules = Label(root, text="This quiz contains 10 quetions\nYou will get 20 seconds to solve a quetion\nOnce you select a radio that will be a final choice\nhence think before you select",
                 width=100, background="#000055", foreground="#ffffff", font=("Times", 14))
lblRules.pack(pady=(60, 0))

# change frame using loop
root.mainloop()
