from tkinter import *

root=Tk()
root.title("Login App")
root.geometry("400x400")

frame=Frame(master=root,height=200,width=360,bg="#A00000")
root=Tk()
root.title("Info")
#Size of the screen
root.geometry("250x300")
lbl2=Label(frame, text="Name",bg="#3895D3",fg="white",width=12)
lbl3=Label(frame, text="Age",bg="#3895D3",fg="white",width=12)
lbl4=Label(frame, text="Gender",bg="#3895D3",fg="white",width=12)

name_entry=Entry(frame)
age_entry=Entry(frame)
gender_entry=Entry(frame)


def display():
    name=name_entry.get()
    greet="Hey "+name
    message1="\nCongratulations for entering your details!"
    message2="\nYou are {age_entry} years old!"

    textbox.insert(END,greet)
    textbox.insert(END,message1)
    textbox.insert(END,message2)

textbox=Text(bg="#BEBEBE",fg="black")
btn=Button(text="Create Account",command=display, bg="red")


frame.place(x=20,y=0)
lbl2.place(x=20,y=20)
lbl3.place(x=20,y=80)
lbl4.place(x=20,y=140)

name_entry.place(x=150,y=20)
age_entry.place(x=150,y=80)
gender_entry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)






root.mainloop()