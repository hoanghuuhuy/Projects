import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import wave
import os
from PIL import ImageTk, Image
from tkinterdnd2 import DND_FILES, TkinterDnD


def Embedding():
        audio = wave.open(root.input, mode='rb')
        bytes_covert = bytearray(list(audio.readframes(audio.getnframes())))
        string = message.get("1.0",'end-1c')
        string = string + int((len(bytes_covert) - (len(string) * 8 * 8)) / 8) * '#'
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
        for i, bit in enumerate(bits):
            bytes_covert[i] = (bytes_covert[i] & 254) | bit
        frame_modified = bytes(bytes_covert)
        for i in range(0, 10):
            print(bytes_covert[i])
        name_output = os.path.join(root.output, outputname.get() + ".wav")
        output = wave.open(name_output, 'wb')
        output.setparams(audio.getparams())
        output.writeframes(frame_modified)

        output.close()
        audio.close()

def Extracting():
        Mess.delete('1.0', END)

        audio = wave.open(root.input, mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
        hidden_message = string.split("###")[0]
        Mess.insert(tkinter.END, hidden_message)
        audio.close()

def Export_message():
        name_output = os.path.join(root.text, text_name.get() + ".txt")
        file = open(name_output, 'w+')
        file.write(Mess.get('1.0', END))
        file.close()

def Input_file():
    root.input = tk.filedialog.askopenfilename(initialdir = "/", title = "select a file",filetype = [('Audio Files', '.wav')])
    label_input.config(text= root.input)

def Embedding_output():
    root.output = tk.filedialog.askdirectory(initialdir = "/", title = "select a file")
    label_output.config(text = root.output)

def Text_output():
    root.text = tk.filedialog.askdirectory(initialdir = "/", title = "select a file")
    label_text.config(text = root.text)

def Clear():
    outputname.delete(0, END)
    message.delete('1.0', END)
    Mess.delete('1.0', END)
    text_name.delete(0, END)
    label_input.config(text="Choose audio")
    label_output.config(text="Choose place to put")
    label_text.config(text="Choose place to put text")

def resizer(e):
    global resized_bg
    global new_bg
    bg1=Image.open("final.jpg")
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    new_bg =  ImageTk.PhotoImage(resized_bg)
    my_canvas.create_image(0, 0, image=new_bg, anchor="nw")

def drop_file(event):
    message.delete('1.0', "end")
    if event.data.endswith(".txt"):
        with open(event.data, "r") as file:
            for line in file:
                line = line.strip()
                message.insert("end", f"{line}\n")



root = TkinterDnD.Tk()
root.title("Audio steganography")
root.geometry("1060x620")

bg = ImageTk.PhotoImage(file="final.jpg")

my_canvas = Canvas(root, width=1060, height=620)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")


tk.Label(root, text="Input File:").place(x=20, y=30)
tk.Label(root, text="Output File:").place(x=20, y=110)
tk.Label(root, text="Name of audio:").place(x=20, y=190)
tk.Label(root, text="Message:").place(x=20, y=250)
tk.Label(root, text="Hidden Message:").place(x=770, y=30)

label_input = tk.Label(root,text="Choose audio",width=43, height=2,bg="white")
label_input.place(x= 30, y= 60)
label_output = tk.Label(root,text="Choose place to put",width=43, height=2,bg="white")
label_output.place(x= 30, y= 140)

outputname = tk.Entry(root,width=46)
outputname.place(x=30, y=220)

message = tk.Text(root,width=63,height=11)
message.place(x=30 ,y=280)
message.drop_target_register(DND_FILES)
message.dnd_bind("<<Drop>>", drop_file)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.place(x=538,y=281, height='180')
message.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=message.yview)

tk.Label(root, text="File name:").place(x=600,y=400)
text_name = tk.Entry(root,width=46)
text_name.place(x=625, y=430)
tk.Label(root, text="Output Text:").place(x=600, y=460)
label_text = tk.Label(root,text="Choose place to put text",width=43, height=2,bg="white")
label_text.place(x= 625, y= 490)

Mess = Text(root, height=20, width=50)
Mess.place(x=610, y=60)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.place(x=1014,y=61, height='323')
Mess.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Mess.yview)

tk.Button(root, text="Chosse File", command=lambda: Input_file() ).place(x=350, y=65)
tk.Button(root, text="Chosse Folder", command=lambda: Embedding_output() ).place(x=350, y=145)
tk.Button(root, text="Chosse Folder", command=lambda: Text_output() ).place(x=950, y=495)

tk.Button(root, text="Extract message", command=lambda: Export_message(),width=20, height=2).place(x=770, y=550)

tk.Button(root, text="Embedding", command=lambda: Embedding(),width=30, height=2).place(x=40, y=470)

tk.Button(root, text="Extracting",command=lambda: Extracting(),width=30, height=2).place(x=290, y=470)

tk.Button(root, text="Clear",command=lambda: Clear(), width=30, height=2).place(x=40, y=530)

tk.Button(root, text="Exit", command=root.destroy, width=30, height=2).place(x=290, y= 530)

root.bind('<Configure>', resizer)
root.mainloop()