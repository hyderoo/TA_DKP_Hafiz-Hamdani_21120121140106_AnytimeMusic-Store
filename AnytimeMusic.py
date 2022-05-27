from tkinter import *
from Login import *
import random
from datetime import datetime
import time
from tkinter import messagebox

window = Tk()
window.geometry("1000x600")
window.title("AnytimeMusic")
window.configure(bg = "#ffffff")
canvas = Canvas(window, bg = "#ffffff", height = 600, width = 1000, bd = 0,  highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

Bill = StringVar()
Total = StringVar()
Date = StringVar()
Gitar = StringVar()
Drum = StringVar()
Keyboard = StringVar()
Bass = StringVar()
Harp = StringVar()
Piano = StringVar()
Viola = StringVar()
Saxophone = StringVar()

#Label
gitar_img = PhotoImage(file = f"Media/img_textBox0.png")
gitar_bg = canvas.create_image(120.5, 240.5, image = gitar_img)
gitartext = Entry( bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Gitar, justify=CENTER)
gitartext.place(x = 107.5, y = 234, width = 26.0, height = 11)

piano_img = PhotoImage(file = f"Media/img_textBox1.png")
piano_bg = canvas.create_image(120.5, 439.5, image = piano_img)
pianotext = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Piano, justify=CENTER)
pianotext.place(x = 107.5, y = 433, width = 26.0, height = 11)

viola_img = PhotoImage(file = f"Media/img_textBox2.png")
viola_bg = canvas.create_image(340.5, 439.5, image = viola_img)
violatext = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Viola, justify=CENTER)
violatext.place(x = 327.5, y = 433, width = 26.0, height = 11)

saxophone_img = PhotoImage(file = f"Media/img_textBox3.png")
saxophone_bg = canvas.create_image(546.5, 445.5, image = saxophone_img)
saxophonetext = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Saxophone, justify=CENTER)
saxophonetext.place(x = 533.5, y = 439, width = 26.0, height = 11)

drum_img = PhotoImage(file = f"Media/img_textBox4.png")
drum_bg = canvas.create_image(340.5, 240.5, image = drum_img)
drumtext = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Drum, justify=CENTER)
drumtext.place(x = 327.5, y = 234, width = 26.0, height = 11)

keyboard_img = PhotoImage(file = f"Media/img_textBox5.png")
keyboard_bg = canvas.create_image(546.5, 240.5, image = keyboard_img)
keyboardtext = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Keyboard, justify=CENTER)
keyboardtext.place(x = 533.5, y = 234, width = 26.0, height = 11)

bass_img = PhotoImage(file = f"Media/img_textBox6.png")
bass_bg = canvas.create_image(726.5, 240.5, image = bass_img)
basstext = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Bass, justify=CENTER)
basstext.place(x = 713.5, y = 234, width = 26.0, height = 11)

harp_img = PhotoImage(file = f"Media/img_textBox7.png")
harp_bg = canvas.create_image(898.5, 240.5, image = harp_img)
harptext = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Harp, justify=CENTER)
harptext.place(x = 885.5, y = 234, width = 26.0, height = 11)

#Function untuk command button total
def generate_bill():
    confirm = messagebox.askyesno('Confirmation', 'Do you want to proceed?')
    if confirm == True:
        bill_no = str(random.randint(10000, 30000))
        Bill.set(bill_no)
        Date.set(localtime)
        #Pengkondisian Try-Except
        try: xgitar = int(Gitar.get())
        except: xgitar = 0
        try: xdrum = int(Drum.get())
        except: xdrum = 0
        try: xkeyboard = int(Keyboard.get())
        except:xkeyboard = 0
        try: xbass = int(Bass.get())
        except:xbass = 0
        try: xharp = int(Harp.get())
        except:xharp = 0
        try: xpiano = int(Piano.get())
        except: xpiano = 0
        try: xviola = int(Viola.get())
        except:xviola = 0
        try: xsaxophone = int(Saxophone.get())                   
        except: xsaxophone = 0

        #Perhitungan Harga satuan alat musik
        HargaGitar = xgitar * 380
        HargaDrum = xdrum * 900
        HargaKeyboard =  xkeyboard * 700
        HargaBass = xbass * 400
        HargaHarp = xharp * 580
        HargaPiano = xpiano * 3700
        HargaViola = xviola * 150
        HargaSaxophone = xsaxophone * 190

        #Perhitungan Total pembayaran
        Totalcost= HargaGitar + HargaDrum + HargaKeyboard + HargaBass + HargaHarp + HargaPiano + HargaViola + HargaSaxophone
        Totalcost= '$', str('%g' % Totalcost)
        Total.set(Totalcost)

    elif confirm == False:
        pass

#Label
lbl_no_bill_img = PhotoImage(file = f"Media/img_textBox8.png")
lbl_no_bill_bg = canvas.create_image(825.0, 312.0, image = lbl_no_bill_img)
text_no_bill = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Bill, justify=CENTER)
text_no_bill.place(x = 751.0, y = 300, width = 148.0, height = 22)

lbl_date_img = PhotoImage(file = f"Media/img_textBox9.png")
lbl_date_bg = canvas.create_image(824.5, 346.0, image = lbl_date_img)
text_date = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Date, justify=CENTER)
text_date.place(x = 751.0, y = 334, width = 147.0, height = 22)

lbl_total_img = PhotoImage(file = f"Media/img_textBox10.png")
lbl_total_bg = canvas.create_image(824.5, 379.0, image = lbl_total_img)
text_total = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0, textvariable=Total, justify=CENTER)
text_total.place(x = 751.0, y = 367, width = 147.0, height = 22)

#Background
background_img = PhotoImage(file = f"Media/background.png")
background = canvas.create_image(514.5, 214.5, image=background_img)

#Button total
button_total = PhotoImage(file = f"Media/img0.png")
btotal = Button(image = button_total, borderwidth = 0, highlightthickness = 0, command = generate_bill, relief = "flat")
btotal.place(x = 653, y = 426, width = 64, height = 26)

#Function untuk button reset
def reset():
    Gitar.set('')
    Drum.set('')
    Keyboard.set('')
    Bass.set('')
    Harp.set('')
    Piano.set('')
    Viola.set('')
    Saxophone.set('')
    Bill.set('')
    Total.set('')
    Date.set('')

#Button reset
button_reset = PhotoImage(file = f"Media/img1.png")
breset = Button(image = button_reset, borderwidth = 0, highlightthickness = 0, command = reset, relief = "flat")
breset.place(x = 749, y = 426, width = 65, height = 28)

#Function untuk button exit
def exit():
    msboexit = messagebox.askyesno('AnytimeMusic', 'Are you sure you want to exit?')
    if msboexit == True:
        messagebox.showinfo('Countdown', 'Killing window in 3 seconds')
        time.sleep(3)
        window.destroy()
    elif msboexit == False:
        pass

#Button exit
button_exit = PhotoImage(file = f"Media/img2.png")
bexit = Button(image = button_exit, borderwidth = 0, highlightthickness = 0, command = exit, relief = "flat")
bexit.place(x = 846, y = 424, width = 64, height = 28)

window.resizable(True, True)
window.mainloop()