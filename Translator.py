from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


from tkinter import *
from tkinter import ttk
from translate import Translator

def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    translator = Translator(from_lang=src1, to_lang=dest1)
    try:
        trans1 = translator.translate(text1)
        return trans1
    except Exception as e:
        print("Translation Error:", e)
        return "Translation Error"

def Data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)









root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(background="orange")


lab_txt=Label(root,text="Translator",foreground="green",font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)
  
frame=Frame(root).pack(side=BOTTOM)

sor_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="green",bg="orange")
sor_txt.place(x=100,y=100,height=20,width=300)

sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

 
comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("english")
  

bottom_change=Button(frame,text="Translate",relief=RAISED,command=Data)
bottom_change.place(x=170,y=300,height=40,width=100)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=100)
comb_dest.set("english")
  


lab_txt=Label(root,text="Dest Text",foreground="green",font=("Time New Roman",20,"bold"),bg="orange")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)



root.mainloop()









