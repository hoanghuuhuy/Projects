from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector
import os


# searching product
def search_pro_table():
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()

        selected = drop.get()
        sql = ""
        if selected == "Search By ...":
            messagebox.showinfo("Error","What do you like to search by ?")

        if selected == "Name":
            if search_box.get() == "":
                messagebox.showinfo("Error", "What do you like to search?")
            else:
                sql='SELECT * FROM product WHERE name LIKE %s'
                args = ['%' + search_box.get() + '%']
                result = mycursor.execute(sql, args)
                result = mycursor.fetchall()

                for i in Table_product.get_children():
                    print(i)
                for i in Table_product.get_children():
                    Table_product.delete(i)
                for i, (id, name, price, amount, information) in enumerate(result, start=1):
                    Table_product.insert("", "end", values=(id, name, price, amount, information))
                connection.close()
        if selected == "Price":
            sql = "Select * from product where price = %s"
            if search_box.get() == "":
                messagebox.showinfo("Error", "What do you like to search?")
            else:
                result = mycursor.execute(sql, (search_box.get(),))
                result = mycursor.fetchall()

                for i in Table_product.get_children():
                    print(i)
                for i in Table_product.get_children():
                    Table_product.delete(i)
                for i, (id, name, price, amount, information) in enumerate(result, start=1):
                    Table_product.insert("", "end", values=(id, name, price, amount, information))
                connection.close()
        if selected == "Amount":
            sql = "Select * from product where amount = %s"

            if search_box.get() == "":
                messagebox.showinfo("Error", "What do you like to search?")
            else:
                result = mycursor.execute(sql, (search_box.get(),))
                result = mycursor.fetchall()

                for i in Table_product.get_children():
                    print(i)
                for i in Table_product.get_children():
                    Table_product.delete(i)
                for i, (id, name, price, amount, information) in enumerate(result, start=1):
                    Table_product.insert("", "end", values=(id, name, price, amount, information))
                connection.close()


        if selected == "Information":
            if search_box.get() == "":
                messagebox.showinfo("Error", "What do you like to search?")
            else:
                sql = 'SELECT * FROM product WHERE information LIKE %s'
                args = ['%' + search_box.get() + '%']
                result = mycursor.execute(sql, args)
                result = mycursor.fetchall()

                for i in Table_product.get_children():
                    print(i)
                for i in Table_product.get_children():
                    Table_product.delete(i)
                for i, (id, name, price, amount, information) in enumerate(result, start=1):
                    Table_product.insert("", "end", values=(id, name, price, amount, information))
                connection.close()


#show product value
def show_pro_infor():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
    mycursor = connection.cursor()
    mycursor.execute("SELECT Id, Name, Amount, Price, Information FROM product ")
    product = mycursor.fetchall()
    print(product)

    for i in Table_product.get_children():
        print(i)

    for i in Table_product.get_children():
        Table_product.delete(i)

    for i, (id, name, price, amount, information) in enumerate(product, start=1):
        Table_product.insert("", "end", values=(id, name, price, amount, information))
    connection.close()

#change the size of background
def resizer(e):
    global bg1
    global resized_bg
    global new_bg
    bg1=Image.open("C:\\Users\\HoangHuy\\Desktop\\Mid_python\\mid.jpg")
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    new_bg =  ImageTk.PhotoImage(resized_bg)
    my_canvas.create_image(0, 0, image=new_bg, anchor="nw")

#return to main window
def Return():
    root.destroy()
    os.startfile("Main_window.py")

#clear entry
def Clear():
    search_box.delete()


if __name__== "__main__":
    root = tk.Tk()
    root.title("Computer store")
    root.geometry("1500x1000")

#back ground
    bg = ImageTk.PhotoImage(file="C:\\Users\\HoangHuy\\Desktop\\Mid_python\\mid.jpg")

    my_canvas = Canvas(root,width = 800, height=500)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0,0, image=bg, anchor="nw")

# styke treeview
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", rowheight=20)

# scroll product
    tree_framepro = tk.Frame(root)
    tree_framepro.pack(pady=20)
    tree_scrollpro = tk.Scrollbar(tree_framepro)
    tree_scrollpro.pack(side=tk.RIGHT, fill=tk.Y)

# return button
    returnButton = tk.Button(root, text="Return to main", command=lambda:Return(), bg = "hot pink", height = 3, width = 20).place(x=1100, y=40)

# exit button
    exitButton = tk.Button(root, text="Exit", command=root.destroy, fg="white", bg="firebrick1", height=3, width=15).place(x=1100, y=120)

# refresh button
    refresh_Button = tk.Button(root, text='Refresh',command=lambda: [show_pro_infor(),Clear()], bg="sky blue",height=3, width=15).place(x=900, y=40)

# entry
    search_box = tk.Entry(root)
    search_box.place(x=170, y=58, width=300)
    search_box_label = tk.Label(root, text="Search product ", fg="black")
    search_box_label.place(x=60, y=58)
    search_button = tk.Button(root, text="Search Product", command=lambda: search_pro_table(), bg="PaleGreen2",height=3, width=15)
    search_button.place(x=700, y=40)

# Search by bar
    drop = ttk.Combobox(root, value=["Search By ...", "Name", "Price", "Amount", "Information"])
    drop.current(0)
    drop.place(x=500, y=58)

# show table customer
    Table_product = ttk.Treeview(tree_framepro, yscrollcommand=tree_scrollpro.set,columns=('ID', 'Name', 'Amount', 'Price', 'Information'), show='headings', height=15)
    Table_product.column("ID", anchor=tk.CENTER, width=80)
    Table_product.column("Name", anchor=tk.W, width=330)
    Table_product.column("Price", anchor=tk.CENTER, width=110)
    Table_product.column("Amount", anchor=tk.CENTER, width=100)
    Table_product.column("Information", anchor=tk.W, width=550)

    Table_product.heading("ID", text="ID", anchor=tk.CENTER)
    Table_product.heading("Name", text="Name", anchor=tk.CENTER)
    Table_product.heading("Price", text="Price", anchor=tk.CENTER)
    Table_product.heading("Amount", text="Amount", anchor=tk.CENTER)
    Table_product.heading("Information", text="Information", anchor=tk.CENTER)
    Table_product.pack()
    tree_scrollpro.config(command=Table_product.yview)
    tree_framepro.place(x=45, y=200)

#show value of product
    show_pro_infor()

root.bind('<Configure>', resizer)

root.mainloop()