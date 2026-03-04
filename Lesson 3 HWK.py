from tkinter import *

root=Tk()
root.title("Number Pad")
root.geometry("400x300")




lbl2=Label(root, text="Enter a number in cm",bg="#3895D3",fg="white")
lbl2.pack()

textbox1=Entry(bg="#BEBEBE",fg="black")
textbox1.pack()
a=" "
textbox1.insert(END,a)



def display():
    x=int(textbox1.get())/2.5
    lbl4=Label(root, text=x,bg="#3895D3",fg="white")
    lbl4.pack()
btn1=Button(text="Click",command=display, bg="red")
btn1.pack()



root.mainloop()