
from tkinter import *
import pyautogui
import time
import webbrowser
#=====================design============================================================================
ib=Tk()
ib.geometry("500x500")
ib.title("INSTAGRAM BOT")
#==============string var=======================================================================================
chat=StringVar()
Name=StringVar()
#==================functions=======================================================================================
def send():

    webbrowser.open("www.google.com")
    time.sleep(4)


    fail=pyautogui.FAILSAFE=False
    pyautogui.moveTo(1700, 40)
    time.sleep(2)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.moveTo(1200,120)
    pyautogui.leftClick()
    pyautogui.write("instagram.com")

    pyautogui.press("Enter")
    time.sleep(15)
    pyautogui.moveTo(790, 260)
    time.sleep(5)
    pyautogui.leftClick()
    pyautogui.write("instagram username")
    time.sleep(3)
    pyautogui.moveTo(1290, 310)
    pyautogui.leftClick()
    time.sleep(3)
    pyautogui.moveTo(755, 330)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.write("instagram password")
    pyautogui.press("Enter")
    time.sleep(5)
    pyautogui.moveTo(1000, 100)
    time.sleep(3)
    pyautogui.leftClick()
    time.sleep(5)
    pyautogui.moveTo(895, 500)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.write(Name.get())
    time.sleep(3)
    pyautogui.moveTo(845, 350)
    pyautogui.leftClick()
    pyautogui.moveTo(865, 250)
    pyautogui.leftClick()
    time.sleep(3)
    pyautogui.write(chat.get())
    pyautogui.press("Enter")


#=================title===================================================================================
title=Label(ib, text="Instagram Bot", bg="white", fg="black", bd=7, font=("halvetica", 15, "bold"))
title.pack(fill=X)
#=================what to send==============================================================================
to_send=LabelFrame(ib, text="Type what to send", bg="white")
to_send.place(x=0, y=50, relwidth=1)
text=Entry(to_send, width="100", bg="grey", fg="black", font=("halvetica", 10), textvariable=chat)
text.grid(row=0, column=0)
#=====================whom to send===========================================================================
whom_to_send=LabelFrame(ib ,text="Whom to send", bg="white")
whom_to_send.place(x=0, y=90, relwidth=1)
name=Entry(whom_to_send, width="100", bg="grey", fg="black", font=("halvetica", 10), textvariable=Name)
name.grid(row=0, column=0)
confirm=Button(whom_to_send, width="20", text="send", fg="black", bg="white", font=("halvetica", 15), command=send)
confirm.grid(row=1, column=0)
#===========================================================================================================





ib.mainloop()
