from tkinter import *
from tkinter.ttk import *
from tkinter import Text,Canvas
#import time
#import keyboard
#import os

#import random
root = Tk()
width,height = root.winfo_screenwidth(),root.winfo_screenheight()
canvasSize = root.geometry('%dx%d+0+0'%(width,height))
root.title('WDocProj')
root.config(background="#E4DCCF")#hex colors must have the hashtag in specifying
#root.resizable(False,False)
#root.attributes('-fullscreen',True)
frm = Frame(root,padding=10)
frm.place()

#initializing frames for each button trigger signals
s = Style()
s.configure("My.TFrame",background="red")


'''
test out core features. then move it on a separate library later
'''
#functionalities
class liner:
    linecounter = 0#linecounted should be part of the method
    def addCodeLine(event):
    
        linecounter+=1
        #print("beep")
        #a =  str(linecounter) + '\t\n'
        a = "something \n"
        textpad.insert(END,a)
        
        #time.sleep(5)

class TopWidgets:
    def show():
        edit.place(x= 100,y=26,width=50,height=100)#reseting the plcement
        hidden = False
        navFile2.config(command=TopWidgets.hide)
    def hide():
        edit.place_forget()
        navFile2.config(command=TopWidgets.show)

        

def maincommand(a):
    liner.addCodeLine(a)

#other window aspect
canvas = Canvas(root,width=10000,height=45,background="#576F72",highlightthickness=0,bd=0,relief="ridge")
canvas.place(x=0,y=0)
canvas2 = Canvas(root,width=10000,height=45,background="#3D8361",highlightthickness=0,bd=0,relief="ridge")
canvas2.place(x=0,y=45)


paperplace = Canvas(root,width=1000,height=2000,background="#FFFFFF",highlightthickness=0,bd=0,relief="ridge")
paperplace.place(x=250,y=150)


#widgets goes here
style1 = Style()
style1.configure('Custom.TButton',font=("calibri",11),background="#7D9D9C")

#very top nav bar goes here
navFile1 = Button(text="File",style='Custom.TButton')
navFile1.config()
navFile1.place(width=75,height=23,x=10,y=6)

navFile2 = Button(text="Edit",style='Custom.TButton')
navFile2.config (command=TopWidgets.show)
navFile2.place(width=75,height=23,x=100,y=6)
#navFile2.bind('<Button-1>',TopWidgets.openFileBtn)
#word editing utilities goes here.


#pop widgets goes here 
edit = Frame(root,padding=10,style="My.TFrame")
edit.config()#make it so the the widget frame display is hidden
#edit.place(x= 10,y=20,width=50,height=100)
edit.place_forget()

#Add the content tools bar(below the nav bars)

#1. the font alignment buttons (left,centered, right)
L_allignment = Button(text='Left') #maybe replace it with icons later on
L_allignment.place(x=800,y=50,width=50,height=20)

C_allignment = Button(text='Cntr') #maybe replace it with icons later on
C_allignment.place(x=850,y=50,width=50,height=20)

R_allignment = Button(text='Rght') #maybe replace it with icons later on
R_allignment.place(x=900,y=50,width=50,height=20)


#2. the font Size field and fixed size buttons
Label2 = Label(text="Font Size:").place(x=445,y=55,width=55,height=20)

Fz_Field = Entry()
Fz_Field.insert(0,"fsz: ")
Fz_Field.place(x=500,y=55,width=50,height=20)

Fz_FixedSize = Button(text="v")
Fz_FixedSize.place(x=550,y=55,width=20,height=20)

def deletePlaceholderText(event):#functions that deletes the placeholder text(WORKS NOW)
    a = textpad.get("1.0","1.21")
    if event and a == placeholderText1:
        textpad.delete("1.0","1.21")
        print("pingpong")
        '''
        Tkinter text indexing guide:
        text widget has index pointer system.
        "1.0" means line 1 and the 0 index character or first character
        "1.21" means line 1 character 21
        '''
        
        

#text field goes here
placeholderText1 = "/Type something here/"
textpad = Text(bd=0)
#textpad.insert(END,"0\t")
textpad.config(font=("calibri",12))
textpad.place(x=350,y=200,width=800,height=1500)
textpad.insert(END,placeholderText1)
textpad.tag_add("plc","1.0","1.10") #marker

textpad.bind('<FocusIn>',deletePlaceholderText)
#textpad.bind('<Return>',maincommand)

root.mainloop()
