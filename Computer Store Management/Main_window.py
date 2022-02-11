from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import mysql.connector
import os


def Company():
    root.destroy()
    os.startfile("computer_store_management.py")

def Customer():
    root.destroy()
    os.startfile("computer_store.py")

def resizer(e):
    global resized_bg
    global new_bg
    bg1=Image.open("C:\\Users\\HoangHuy\\Desktop\\Mid_python\\mid.jpg")
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    new_bg =  ImageTk.PhotoImage(resized_bg)
    my_canvas.create_image(0, 0, image=new_bg, anchor="nw")

if __name__== "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("1500x1000")

    bg = ImageTk.PhotoImage(file="C:\\Users\\HoangHuy\\Desktop\\Mid_python\\mid.jpg")

    my_canvas = Canvas(root, width=800, height=500)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bg, anchor="nw")

    textsize = font.Font(size=36)

    Company_button = tk.Button(root,text = "For Staff",command=lambda:Company(), bg="ghost white", height=15, width=35).place(x=800, y=220)

    Customer_button = tk.Button(root,text = "For Customer",command=lambda:Customer(), bg="sky blue", height=15, width=35).place(x=210, y=220)

    exitButton = tk.Button(root, text="Exit", command=root.destroy, fg="white", bg="firebrick1", height=3, width=15).place(x=1140, y=580)

root.bind('<Configure>', resizer)

root.mainloop()