from doctest import master      #
import tkinter as tk
from tkinter import *
import os
from turtle import color
import pandas as pd
import numpy as np
import random

GREEN="#18732a"
GREY="#666e68"
YELLOW="#d1bb2a"
global usedWords
global usedColors
global highlighted
global highlightedPos
highlightedPos=0
highlighted=[]
usedWords=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
usedColors=['grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey']
 

def escp():
    gui.destroy()

gui = tk.Tk(className="Olg's Wordle :)")
gui.geometry("1080x720")
gui.minsize(1080, 720)
gui.maxsize(1080, 720)
#gui.configure(background = 'black')
bg = PhotoImage(file = "landing.png")
# Show image using label
background = Label( gui, image =bg,width=1080, height=760,background='#964B00').place(x = 0, y = 0)



#label = Label(gui, text = 'Olg\'s Wordle!', fg = 'yellow',bg = 'black', font = ("Arial", 30,'bold'), height = 1)
#label.pack(side = TOP,pady=70)
for i in range(3):
    gui.columnconfigure(i, weight=1)

gui.rowconfigure(1, weight=1)

def redirect(): 
    global usedColors
    usedColors=['grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey']
    global highlighted
    global highlightedPos
    global yellowLetters
    yellowLetters=[]
    highlightedPos=0
    highlighted=[]
    global totalclicks
    totalclicks=0
    def character_limit(guess):
        if len(guess.get()) > 0:
            guess.set(guess.get()[:5])

    
    mover=0
    movy=0
        #print(usedWords)
  
    
    
    
    def restart():
        wordle.withdraw()
        redirect()
    def retr():
        gui.deiconify()
        wordle.withdraw()
        
        
    def chck():
        guessedLetters=np.zeros(5,dtype=str)
        global totalclicks
        global guessString
        
        guessString=guess.get().lower()
        
        if not(guessString in words.values):
            tempLabel=Label(wordle,text='That word isn\'t in the game',fg='#FFE55A',bg='black',font=("Arial",15) )
            tempLabel.place(rely=0.0, relx=0.5, x=0, y=0, anchor=N)
            wordle.after(2000, tempLabel.destroy)
            return 
        inputs=np.zeros(5,dtype=str)

        i=0
        for character in guessString:
           inputs[i]=character
           i+=1
           

  
                
        
        #Label(wordle,text=guessString,fg='yellow',bg='black').grid(row=2, column=3)
        global tempWord
        tempWord=word
        def checkIfCorrect(letter,pos):
            global guessString
            global tempWord
            global highlighted
            global highlightedPos
            if letter==word[pos]:
                highlighted.append(letter)
                #guessString=guessString.replace(letter, "")# prvo nadji sve tacne pa onda na pogresnim pozicijama
                guessString = guessString[:pos] + "-" + guessString[pos+1:]
                tempWord=tempWord[:pos] + "-" + tempWord[pos+1:]
                highlightedPos+=1
                return GREEN
            #for element in word:            #dodaj da se samo jednom karakter uporedjuje tipa da moze da se izbaci ako je vec green
                #if letter==element:
                    #return YELLOW
            return GREY
        
        def checkIfPos(letter,pos):
            global guessString
            global yellowLetters
                        #dodaj za zuta slova
            global tempWord
            for i in range(len(tempWord)):
                if letter==tempWord[i]:
                    tempWord=tempWord[:i] + "-" + tempWord[i+1:]            #OVO OVDE DA POPRAVI TO STO SE PRIKAZUJU DVA ISTA SLOVA UMESTO JEDNOG 
                    yellowLetters.append(letter)
                    return YELLOW           #brisi pogodjene reci iz word
            return GREY
        cnt=0
        pos=0
        totalclicks+=1
        
        colorL=np.full(5,GREY)
        colorL.fill
        colorc=0
        for element in guessString: 
            colorL[colorc]=checkIfCorrect(element,pos)
            pos+=1
            colorc+=1
        colorc=0
        pos=0
        for element in guessString:
            if colorL[colorc]==GREY:
                colorL[colorc]=checkIfPos(element,pos)
            pos+=1
            colorc+=1
        position=0
        for element in inputs:
            #colorL=checkIfCorrect(element,pos)
            cnt+=20
            Label(wordle,text=element,fg='white',bg=colorL[position],wraplength=1,font=("Arial", 25)).place(x = cnt+400,y = 30+totalclicks*60)       #.place(x = cnt+520,y = 20+totalclicks*4)
            cnt+=20
            position+=1
            #Label(wordle,text=element,fg='yellow',bg='black',wraplength=1).pack(side=LEFT, anchor=NW)
        guessed=False
        if np.all(colorL==GREEN):
            cnt=0
            Label(wordle,text="Correct!",fg='white',bg=GREEN,font=("Arial", 25)).place(x = cnt+440,y = 30+(totalclicks+1)*60)
            wordInput.config(state='disabled')   
            Label(wordle,text="BLOCK",fg='#964B00',bg='#964B00',font=("Arial", 25)).grid(row=0,column=4,sticky=N,pady=30,padx=25)
            guessed=True
        if totalclicks==6 and guessed==False:
            #totalclicks+=1
            cnt=0
            Label(wordle,text="Incorrect!",fg='white',bg='red',font=("Arial", 25)).place(x =440,y = 30+(totalclicks+1)*60)
            for element in word:
                cnt+=20
                Label(wordle,text=element,fg='white',bg=GREEN,wraplength=1,font=("Arial", 25)).place(x = cnt+400,y = 30+(totalclicks+2)*60)
                cnt+=20
            wordInput.config(state='disabled')   
            Label(wordle,text="BLOCK",fg='#964B00',bg='#964B00',font=("Arial", 25)).grid(row=0,column=4,sticky=N,pady=30,padx=25)
                
                
            mover=0
            movy=0
        global usedWords
        global usedColors
        global yellowLetters
        #print(usedWords)
        #print(inputs)
        for i in range(len(usedWords)):
            for j in range(len(inputs)):
                if usedWords[i].lower()==inputs[j].lower():     #dodaj da se pokazuju i zuta slova
                    usedColors[i]='grey9'
                    
        #for i in range(len(inputs)):            #input & word ->mark usedw
            #if()
        for i in range(len(usedWords)):
            for j in range(len(yellowLetters)):
                if usedWords[i].lower()==yellowLetters[j].lower():
                    usedColors[i]=YELLOW
        for i in range(len(usedWords)):
            for j in range(len(highlighted)):
                 if usedWords[i].lower()==highlighted[j].lower():
                        usedColors[i]=GREEN
        #print(usedColors)
        mover=0
        movy=0
        #print(usedWords)
        for i in range(len(usedWords)):
            mover+=20
            Label(wordle,text=usedWords[i],bg=usedColors[i],wraplength=150,fg='white',font=("Arial", 20)).place(x = mover+700,y = 30+(movy+2)*60)
            mover+=20
            if mover%200==0:            #dodaje kao da postoja dva ista slova ispravi!!!!!
                movy+=1
                mover=0   
  #usedWords=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','grey']

                
                
                
    wordle=Toplevel(gui)
    for i in range(7):
        wordle.columnconfigure(i, weight=1)



    wordle.rowconfigure(1, weight=1)
    guessHolder = Frame(wordle, bg='black')
    wordle.title("Ogl's Wordle!!!!")
    wordle.geometry("1080x720")
    wordle.minsize(1080, 720)
    wordle.maxsize(1080, 720)
    wordle.configure(background="#964B00")
    gui.withdraw()
    
    

        
        
    words = pd.read_csv('words.txt', header = None)
    words=words.T
    which=random.randint(0,len(words[0]))
    word=words.loc[words.index==which]
    word=word[0].to_string(index=False)
    #Label(wordle,text=word,fg='yellow',bg='black').grid(row=0,column=1,sticky=N,pady=30,padx=25)
    guess = tk.StringVar() 
    guess.trace("w", lambda *args: character_limit(guess))
    wordInput=Entry(wordle,width='6',textvariable=guess,font=("Arial", 25),bg=GREY,fg='#FFE55A')
    wordInput.grid(row=0,column=3,sticky=N,pady=25,padx=25,ipady=0)
    
    check=tk.Button(wordle, text ="Check",activeforeground='#FFE55A',activebackground='#964B00',background='#FFE55A',command=chck,width=10,height=2,borderwidth=0).grid(row=0,column=4,sticky=N,pady=30,padx=25)
    
    check=tk.Button(wordle, text ="Restart",activeforeground='red',activebackground='#964B00',background='#FFE55A',width=10,height=2,command=restart,borderwidth=0).grid(row=0,column=5,sticky=N,pady=30,padx=25)
    
    ret=tk.Button(wordle, text ="Return",activeforeground='#FFE55A',activebackground='#964B00',background='#FFE55A',command=retr,width=10,height=2,borderwidth=0)
    ret.place(rely=0.97, relx=0.97, x=0, y=0, anchor=SE)
    
gridFrame = Frame(gui,background='#964B00')
btn = tk.Button(gridFrame, text ="Start solving",activeforeground='#FFE55A',activebackground='#964B00',background='#FFE55A',fg='black',command=redirect,width=10,height=2,borderwidth=0)
btn.grid(row=0, column=1, pady = 110, padx = 25, sticky=N) 
esc=tk.Button(gridFrame, text ="Exit",activeforeground='#FFE55A',activebackground='#964B00',background='#FFE55A',fg='black',command=escp,width=10,height=2,borderwidth=0)
esc.grid(row=2,column=1,sticky=N,pady=30,padx=25)
gridFrame.pack(side='bottom') 
gui.mainloop()

