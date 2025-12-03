import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
def say_Hellow():
    txt=entry1.get()
    txt2=entry2.get()
    result1=txt.split("/")
    num1=int(result1[0])
    de1=int(result1[1])
    print("num1",num1)
    result2=txt2.split("/")
    num2=int(result2[0])
    de2=int(result2[1])
    D=str(de1*de2)
    N1=num1*de2
    N2=num2*de1
    N=str(N1+N2)
    messagebox.showinfo("entry",txt+"+"+txt2+"="+N+"/"+D)
    #messagebox.showinfo("Wife","Jeee")

root.geometry("300x200")

label=tk.Label(root,text="Welcome to my Calculator")
label.pack()

entry1=tk.Entry(root)
entry1.pack()

entry2=tk.Entry(root)
entry2.pack()

button=tk.Button(root, text="add", command=say_Hellow)
button.pack()

root.mainloop()