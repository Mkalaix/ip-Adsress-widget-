from tkinter import*
from  tkinter import messagebox
tranzend=Tk()
tranzend.title("Tran-sci")
lal=Label(tranzend,text="IP ADDRESS ")
def any():
    input_txt=float(user_input.get())
    print("IP ADDRESS :",input_txt)
    messagebox.showinfo("tranzend","succesful")
    




user_input=Entry(tranzend,bd=5)
btn=Button(tranzend,text="submit",command=any)
btn.pack(side="bottom")
lal.pack(side="left")
user_input.pack(side="right")
tranzend.mainloop()
