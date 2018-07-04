# Project by Juhi,Vivek and Mohith.
# Name of the project: Dictation.
# Concepts used: Classes,Functions,Decorators,Modules,GUI.
from Tkinter import*
import random
import time
import os
import subprocess
#from PIL import ImageTk,Image
root= Tk()
root.title("DICTATION")		# Title on top of the window.
root.configure(background='light blue')	# Background colour of the window.
root.resizable(width=FALSE, height=FALSE) # Cannot resize the window.
root.geometry('600x800')
flag=0

class Layout:		# Making the layout of the window.
   count=0
   count3=0
   level=0
   data=""
   count2=0
   def __init__(self):
      self.f1=Frame(root,bg="white")
      self.f1.pack()
      self.label=Label(self.f1,text="Welcome",bg=
"khaki",fg="dodger blue",font=("Times",75,"bold italic"))	# Making the label "welcome" at the top.
      self.label.pack(padx=25,pady=25)
      # Creating the button for starting the new game.
      self.button= Button(self.f1,text="New Game",fg="firebrick",bg="snow",font=("Times",45,"bold italic"))
      self.button.config(height=2,width=10)	# Fixing the height and width of the window.
      # Creating the button to exit the game.
      self.button1= Button(self.f1,text="Exit",bg="violet red",font=("Times",45,"bold italic"),fg="snow") 
      self.button.bind("<Button-1>",lambda event:self.page1(event,self.f1))
      self.button.pack(pady=25,padx=25)
      self.rules=Button(self.f1,text="Rules",height=2,width=10,bg="snow",font=("Times",45,"bold italic"),fg="forest green",padx=10)
      self.rules.bind("<Button-1>",lambda event:self.Rules(event,self.f1))
      self.rules.pack(padx=25,pady=25)
      self.button1.bind("<Button-1>",quit)	# Button to quit the window.
      self.button1.pack(padx=25,pady=25)
   
   def Rules(self,event,frame):		# Giving the rules of the game.
       frame.pack_forget()
       self.f2=Frame(root)
       self.f2.pack()
       self.next=Button(self.f2,text="Next",bg="snow",fg="firebrick",font=("Times",25,"bold italic"))
       self.next.bind("<Button-1>",lambda event:self.page1(event,self.f2))
       self.next.pack(side=BOTTOM)
       #self.background_image=self.f2.PhotoImage(rules.png)
       #self.background_label = self.f2.Label(parent, image=background_image)
       #self.background_label.place(x=0, y=0, relwidth=500, relheight=500)
       self.txt=Text(self.f2,font=("Times",20),fg="red3",bg="khaki")
       self.txt.pack()
       rules="""1)There are 3 levels in the game!
           
2)Each level contains five words of increasing difficulty

3)You are only given 40 seconds per level!

4)You can only proceed after you type in the correct word!

5)The game displays the correct spelling
    in case you type in the wrong word,for one second
    
                 So keep your eyes open!
                 
6)In the end of each level, press the submit button
    to move to the end screen to know your score!
    
7) The timer starts as soon as you choose the level!

                 So Ready Set Go!"""
       self.txt.insert(END,rules)
   
   def page1(self,event,frame):		# Making page 1.
      frame.pack_forget()
      self.f2=Frame(root,bg="white")
      self.f2.pack()
      # Creating the level-1 button.
      self.level1=Button(self.f2,text="Level 1",bg="light sky blue",fg="black",font=("Times",25,"bold italic"))
      # Creating the level-2 button.
      self.level2=Button(self.f2,text="Level 2",bg="sky blue",fg="black",font=("Times",25,"bold italic"))
      # Creating the level-3 button.
      self.level3=Button(self.f2,text="Level 3",bg="dodgerblue2",fg="black",font=("Times",25,"bold italic"))
      self.level1.bind("<Button-1>",lambda event:self.page_level1(event,self.f2))
      self.level1.pack(pady=80)
      self.level2.pack(pady=80)
      self.level2.bind("<Button-1>",lambda event:self.page_level2(event,self.f2))
      self.level3.pack(pady=80)
      self.level3.bind("<Button-1>",lambda event:self.page_level3(event,self.f2))
      
   @staticmethod
   def quit():
      root.quit()
      
   def page_level1(self,event,f2):      	# Making level-1 page.
       Layout.level=1
       f2.pack_forget()
       self.f3=Frame(root,bg="white")
       self.f3.pack()      
       self.label=Label(self.f3,text="LEVEL-1",bg="cyan",font=("Times",45,"bold italic"),fg="turquoise")
       self.label.pack(side=TOP)		# Writing the level-1 label at the top.
       self.listen=Button(self.f3,text="Listen Again",command=speak,font=("Times",25,"bold italic"),bg="white",fg="turquoise")
       # Making the button named listen at the bottom when we click on that we can hear the sound.
       self.listen.pack(side=BOTTOM,padx=25,pady=25) 
       self.answer=Entry(self.f3,width=25)	# Creating text to write the answer.
       self.answer.pack(padx=25,pady=25)
       generate_word()
       self.f3.after(500,speak)
       timer(o.f3,40)
       #global label_time
       #label_time=timer(o.f3,10)

       self.submit=Layout.submit_button(self.f3)	# Making the layout of the submit button.
       self.submit_action(self.submit,self.f3)		# After writing the answer we can submit the answer by clicking on it.
   
   
   @staticmethod
   def submit_button(f3):
       submit=Button(f3,text="Submit",font=("Times",25,"bold italic"),bg="white",fg="black")
       submit.pack(side=BOTTOM)		# Creating the submit button, when we click on it you can hear next word.
       return submit

   @staticmethod
   def submit_action(submit,f3):
       # print Layout.count
       global flag
       if (Layout.count<5 and flag==0):
            submit.bind("<Button-1>",check)
       else:
            submit.bind("<Button-1>",lambda event:o.end(event,f3))



   def page_level2(self,event,f2):		# Making level-2 page.
       Layout.level=2
       f2.pack_forget()
       self.f3=Frame(root,bg="white")
       self.f3.pack()
       self.label=Label(self.f3,text="LEVEL-2",bg="gold",font=("Times",45,"bold italic"),fg="indian red")
       self.label.pack(side=TOP)		# Writing the level-2 label.
       self.listen=Button(self.f3,text="Listen Again",command=speak,font=("Times",25,"bold italic"),bg="khaki",fg="black")
       # Making the button named listen at the bottom when we click on that we can hear the sound.
       self.listen.pack(side=BOTTOM,padx=25,pady=25) 
       self.answer=Entry(self.f3,width=25)	# Creating text to write the answer.
       self.answer.pack(padx=25,pady=25)
       generate_word()
       self.f3.after(500,speak)
       timer(o.f3,40)
       self.submit=Layout.submit_button(self.f3)	# Making the layout of the submit button.
       self.submit_action(self.submit,self.f3)		# After writing the answer we can submit the answer by clicking on it.
   
   
   def page_level3(self,event,f2):		# Making level-3 page.
      
       Layout.level=3
       f2.pack_forget()
       self.f3=Frame(root,bg="white")
       self.f3.pack()
       self.label=Label(self.f3,text="LEVEL-3",bg="chartreuse",font=("Times",45,"bold italic"),fg="dark green")
       self.label.pack(side=TOP)			# Writing the level-3 label.
       self.listen=Button(self.f3,text="Listen Again",command=speak,font=("Times",25,"bold italic"),bg="white",fg="OliveDrab1")
       # Making the button named listen at the bottom when we click on that we can hear the sound.
       self.listen.pack(side=BOTTOM,padx=25,pady=25)	
       self.answer=Entry(self.f3,width=25)		# Creating text to write the answer.
       self.answer.pack(padx=25,pady=25)
       generate_word()
       self.f3.after(500,speak)
       timer(o.f3,40)
       self.submit=Layout.submit_button(self.f3)	# Making the layout of the submit button.
       self.submit_action(self.submit,self.f3)		# After writing the answer we can submit the answer by clicking on it.
   
   
   def end(self,event,f3):
       f3.pack_forget()
       self.f4=Frame(root,bg="white")
       self.f4.pack()
       if(flag==0):
        self.correct=Label(self.f4,text="Congratulations!Level Passed!",font=("Times",35,"italic"),fg="violet red")
        self.correct.pack(side=TOP)
        self.back=Button(self.f4,text="Go back",height=5,width=15)	# Creating back button to go to the back page.
        self.back.bind("<Button-1>",lambda event:self.page1(event,self.f4))
        self.back.pack(side=BOTTOM)
        Layout.count=0
	# Giving the no of questions answered correct.
        self.label1=Label(self.f4,text="correct: "+str(5-Layout.count2),font=("Times",25,"bold"),fg="lawn green")
        self.label1.pack(side=LEFT)
	# Giving the no of questions answered wrong.
        self.label2=Label(self.f4,text="wrong: "+str(Layout.count2),font=("Times",25,"bold"),fg="red")
        self.label2.pack(side=LEFT)
       else:
        self.correct=Label(self.f4,text="Times Up!Try again!",font=("Times",45,"italic"),fg="violet red")
        self.correct.pack(side=TOP)

def output_right(frame):	# The output obtained for giving correct answer.
    right=Label(frame,text="Correct Spelling!")
    right.pack(side=TOP)
    right.after(1000,delete,right)

def output_wrong(frame):	# The output obtained for giving wrong answer.
    wrong=Label(frame,text="Wrong!")
    wrong.pack(side=TOP)
    wrong.after(1000,delete,wrong)

def delete(label):
     label.pack_forget()

def generate_word():	# To take a word.
    if(Layout.level==1):
        randomword = [line.strip() for line in open('level1.txt')]
        Layout.data=randomword[Layout.count]		# Taking the word one by one for level-1.
    if(Layout.level==2):
        randomword = [line.strip() for line in open('level2.txt')]
        Layout.data=randomword[Layout.count]		# Taking the word one by one for level-2.
    elif(Layout.level==3):
        randomword = [line.strip() for line in open('level3.txt')]
        Layout.data=randomword[Layout.count]		# Taking the word one by one for level-3.

def speak():	# It dictates the word to be written.
        #os.system("say "+Layout.data)
	text = Layout.data
	subprocess.call('espeak '+text, shell=True)

o=Layout()

def check(event):	# Checking the answer.
        new=""
        word=o.answer.get()
        o.answer.delete(0,'end')
        #global t
        #t.label.pack_forget()
        for i in range(len(word)):
            if (ord(word[i])>=65 and ord(word[i])<=90):
                new=new+str(chr(ord(word[i])+32))
            else: new=new+str((word[i]))
        if (word==""):
            warning=Label(o.f3,text="Type in something!",font=("Times",20),bg="white",fg="black")
            warning.pack(side=BOTTOM)
            warning.after(3000,delete,warning)
        else:
    
            if(flag==0):
                if Layout.data==new:
                    Layout.count=Layout.count+1		# Counting the score.
                    output_right(o.f3)
                    generate_word()
                    speak()
                    Layout.submit_action(o.submit,o.f3)
            
                else:
                    #Exceptions to be added:if left empty or if time expires
                    Layout.count2=Layout.count2+1
                    output_wrong(o.f3)
		    #Hint is given if you submit wrong answer.
                    correct=Label(o.f3,text="Hint: "+Layout.data,font=("Times",25),bg="white",fg="red") 
                    correct.pack(side=BOTTOM)
                    correct.after(2000,delete,correct)
		    # Warning will be given if you enter wrong spelling.
                    warning=Label(o.f3,text="Enter Correct spelling to continue to the next word!",font=("Times",20),bg="white",fg="black")
                    warning.pack(side=BOTTOM,padx=15,pady=15)
                    warning.after(2500,delete,warning)
            else: Layout.submit_action(o.submit,o.f3)

def timer(frame,time):		# Defining the timer function.
    label=Label(frame,text="Timer: "+str(time),font=("Times",30),bg="white",fg="red")
    label.pack()
    label.after(1000,delete,label)
    if(time>0):
        label.after(1000,timer,frame,(time-1))
    else:
        global flag
        flag=1
#print flag

root.mainloop()
