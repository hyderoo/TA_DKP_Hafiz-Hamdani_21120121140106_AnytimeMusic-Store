from tkinter import *
from tkinter import messagebox

#Function untuk button login
def login():
    email = email0.get()
    password = password0.get()

    if(email == "" and password == "" ):
        messagebox.showerror("ERROR", "Blank Not Allowed")

    elif(email == "hafizhamdani@rocketmail.com" and password == "admin"):
        msboexit = messagebox.askyesno('AnytimeMusic', 'Login Success!, Do you want continue?')
        if msboexit == True:
            window.destroy()
        elif msboexit == False:
            pass
    else :
        messagebox.showerror("ERROR", "Incorrect Username and Password")

window = Tk()
window.geometry("1000x600")
window.title("AnytimeMusic")
global email0
global password0
window.configure(bg = "#ffffff")
canvas = Canvas(window,bg = "#ffffff",height = 600,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#Label
email_img = PhotoImage(file = f"Media/img_textBoxemail.png")
email_bg = canvas.create_image(723.5, 330.0,image = email_img)
email0 = Entry(bd = 0,bg = "#f6f2f2",highlightthickness = 0)
email0.place(x = 594.0, y = 318,width = 259.0,height = 22)

password_img = PhotoImage(file = f"Media/img_textBoxpass.png")
password_bg = canvas.create_image(723.5, 380.0,image = password_img)
password0 = Entry(bd = 0,bg = "#f4f1f1",highlightthickness = 0, show = "*")
password0.place(x = 594.0, y = 368,width = 259.0,height = 22)

#Button login
imgbutton = PhotoImage(file = f"Media/imglogin.png")
buttonlogin = Button(image = imgbutton,borderwidth = 0,highlightthickness = 0,command = login,relief = "flat")
buttonlogin.place(x = 701, y = 423,width = 56,height = 23)

#Background
background_img = PhotoImage(file = f"Media/oasis.png")
background = canvas.create_image(467.0, 236.0,image=background_img)

window.resizable(True, True)
window.mainloop()