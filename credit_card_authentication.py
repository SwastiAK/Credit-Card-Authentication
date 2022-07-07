from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")

root.configure(background="gold")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

img=ImageTk.PhotoImage(Image.open ("C:/Users/Swasti/Desktop/Python Projects/ADV-Project-C158/credit.jpg"))
label = Label(root, image=img)


def authentication():
    try :
        input_value = int(input_box.get())
        messagebox.showinfo("Alert","Credit card accepted.")
    except (ValueError) :
        messagebox.showinfo("Alert", "Credit Card Not Accepted. Please Enter Valid Pin Code")    


btn = Button(root, text = "check credit card", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()