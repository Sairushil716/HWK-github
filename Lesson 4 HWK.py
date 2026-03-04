from tkinter import *

root=Tk()
root.title("Number Pad")
root.geometry("400x300")






lbl2=Label(root, text="Enter the principle amount",bg="#3895D3",fg="white")
lbl2.pack()

textbox1=Entry(bg="#BEBEBE",fg="black")
textbox1.pack()
a=" "
textbox1.insert(END,a)



lbl3=Label(root, text="Enter the rate of interest",bg="#3895D3",fg="white")
lbl3.pack()

textbox2=Entry(bg="#BEBEBE",fg="black")
textbox2.pack()
a=" "
textbox2.insert(END,a)

lbl4=Label(root, text="Enter the time in years",bg="#3895D3",fg="white")
lbl4.pack()

textbox3=Entry(bg="#BEBEBE",fg="black")
textbox3.pack()
a=" "
textbox3.insert(END,a)


def display():
    x=int(textbox1.get())+(int(textbox2.get())*int(textbox3.get()))
    lbl4=Label(root, text=x,bg="#3895D3",fg="white")
    lbl4.pack()
btn1=Button(text="Click",command=display, bg="red")
btn1.pack()



root.mainloop()