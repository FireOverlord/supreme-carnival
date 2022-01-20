from tkinter import *
import random
root=Tk()

root.title("Sneakipedia")
root.geometry("400x400")

no1= Label(root)
no2= Label(root)
no3= Label(root)

colours=["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]

dictionary={'Maroon':colours.get[0],'Lawn Green':colours.get[1],"magenta":colours.get[2],
            "purple":colours.get[3],"Spring Green":colours.get[4],"Chocolate":colours.get[5],
            "Deep Pink":colours.get[6],"cyan":colours.get[7]}

def Mro():
    no1["text"]=""
    no1["text"]= dictionary["Maroon"]
    root.configure(background=colours.get[0])


def LwG():
     no1["text"]=""
     no1["text"]= dictionary["Lawn Green"]
     root.configure(background=colours.get[1]
                    
def MgT():
     no1["text"]=""
     no1["text"]= dictionary["Magenta"]
     root.configure(background=colours.get[2]

def Ppl():
     no1["text"]=""
     no1["text"]= dictionary["Maroon"]
     root.configure(background=colours.get[3]

def SpG():
     no1["text"]=""
     no1["text"]= dictionary["Spring Green"]
     root.configure(background=colours.get[4]

def Chl():
     no1["text"]=""
     no1["text"]= dictionary["Chocolate"]
     root.configure(background=colours.get[5]

def DeP():
     no1["text"]=""
     no1["text"]= dictionary["Maroon"]
     root.configure(background=colours.get[6]

def Cyn():
     no1["text"]=""
     no1["text"]= dictionary["Lawn Green"]
     root.configure(background=colours.get[7]

no1.place(relx=0.5,rely=0.5,anchor=CENTER)                    

bmro= Button(root,text="Maroon",command=Mro)
bmro.place(relx=0.9,rely=0.1,anchor=CENTER)

bMgt= Button(root,text="Magenta",command=Mgt)
bMgt.place(relx=0.9,rely=0.2,anchor=CENTER)

bLwG= Button(root,text="Lawn Green",command=LwG)
bLwG.place(relx=0.9,rely=0.3,anchor=CENTER)

bPpl= Button(root,text="Purple",command=Ppl)
bPpl.place(relx=0.9,rely=0.4,anchor=CENTER)

bSpG= Button(root,text="Spring Green",command=SpG)
bSpG.place(relx=0.9,rely=0.5,anchor=CENTER)

bChl= Button(root,text="Chocolate",command=Chl)
bChl.place(relx=0.9,rely=0.6,anchor=CENTER)

bDep= Button(root,text="Deep Pink",command=DeP)
bDep.place(relx=0.9,rely=0.7,anchor=CENTER)

bCya= Button(root,text="Cyan",command=Cyn)
bmro.place(relx=0.9,rely=0.8,anchor=CENTER)


root.mainloop()