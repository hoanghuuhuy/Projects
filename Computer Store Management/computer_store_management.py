from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import mysql.connector
import os


global proid
global proname
global proprice
global proamount
global proinfor

global stid
global stname
global stdob
global stcontact
global stjob

global cusid
global cusname
global cusbought
global cusamount
global cuscontact
global cusdate


#Error and Success
def Successupdate():
    messagebox.showinfo("Success","Everything is updated")

def Error():
    messagebox.showinfo("information", "Something is wrong")


#add product
def ADDPRO():
    name = proname.get()
    price = proprice.get()
    amount = proamount.get()
    information = proinfor.get()


    if name == "":
        Error()
    elif price == "":
        Error()
    elif amount == "":
        Error()
    elif information == "":
        Error()
    elif name == proname.get():
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM product WHERE name = %s GROUP BY name",(name,))
        result = mycursor.fetchone()
        if result:
            messagebox.showinfo("Error", "Product already exists")
        else:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
            mycursor = connection.cursor()
            vals = (name, price, amount, information)
            mycursor.execute("INSERT INTO product (Name,Price,Amount,Information) VALUES(%s,%s,%s,%s)", vals)
            connection.commit()
            connection.close()
            Successupdate()


#edit product
def EDITPRO():

    name = proname.get()
    price = proprice.get()
    amount = proamount.get()
    information = proinfor.get()

    if name == "":
        Error()
    elif price == "":
        Error()
    elif amount == "":
        Error()
    elif information == "":
        Error()
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()

        try:
            sql = "UPDATE product SET Price = %s , Amount = %s , Information = %s where Name = %s"
            vals = (price, amount, information, name)
            mycursor.execute(sql, vals)
            connection.commit()
            Successupdate()

        except EXCEPTION as e:
            print(e)
            connection.rollback()
        connection.close()


#delete product
def DELPRO():
    name = proname.get()
    if name == "":
        Error()
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        find = (name,)
        mycursor.execute("DELETE FROM product WHERE Name = %s ", find)
        mycursor.execute("ALTER TABLE product AUTO_INCREMENT = 1")
        connection.commit()
        connection.close()
        Successupdate()


#add staff
def ADDST():
    name = stname.get()
    dob = stdob.get()
    contact = stcontact.get()
    job = stjob.get()

    if name == "":
        Error()
    elif dob == "":
        Error()
    elif contact == "":
        Error()
    elif job == "":
        Error()
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        vals = (name, dob, contact, job)
        mycursor.execute("INSERT INTO staff (Name,DoB,Contact,Job) VALUES(%s,%s,%s,%s)", vals)
        connection.commit()
        connection.close()
        Successupdate()


#edit staff
def EDITST():
    name = stname.get()
    dob = stdob.get()
    contact = stcontact.get()
    job = stjob.get()

    if name == "":
        Error()
    elif dob == "":
        Error()
    elif contact == "":
        Error()
    elif job == "":
        Error()
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()

        try:
            sql = "UPDATE staff SET DoB = %s , Contact = %s , Job = %s  where Name = %s"
            vals = (dob, contact, job, name)
            mycursor.execute(sql, vals)
            connection.commit()
            Successupdate()

        except EXCEPTION as e:
            print(e)
            connection.rollback()
        connection.close()


#delete staff
def DELST():
    name = stname.get()
    if name == "":
        Error()
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        find = (name,)
        mycursor.execute("DELETE FROM staff WHERE Name=%s", find)
        mycursor.execute("ALTER TABLE staff AUTO_INCREMENT = 1")
        connection.commit()
        connection.close()
        Successupdate()


#add customer
def ADDCUS():
    name = cusname.get()
    bought = cusbought.get()
    amount = cusamount.get()
    contact = cuscontact.get()
    date = cusdate.get()

    if name == "":
        Error()
    elif bought == "":
        Error()
    elif amount == "":
        Error()
    elif contact == "":
        Error()
    elif date == "":
        Error()
    elif bought == cusbought.get():
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM product WHERE name = %s GROUP BY name",(bought,))
        result = mycursor.fetchone()
        if not result:
            messagebox.showinfo("Error", "Product doesn't exist")
        else:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
            mycursor = connection.cursor()
            vals = (name, bought, amount, contact, date)
            mycursor.execute("INSERT INTO customer (Name,Bought,Amount,Contact,Date) VALUES(%s,%s,%s,%s,%s)", vals)
            connection.commit()
            connection.close()
            Successupdate()


#edit customer
def EDITCUS():

    name = cusname.get()
    bought = cusbought.get()
    amount = cusamount.get()
    contact = cuscontact.get()
    date = cusdate.get()

    if name == "":
        Error()
    elif bought == "":
        Error()
    elif amount == "":
        Error()
    elif contact == "":
        Error()
    elif date == "":
        Error()
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()

        try:
            sql = "UPDATE customer SET Bought = %s , Amount = %s , Contact = %s , Date = %s where Name = %s"
            vals = (bought, amount, contact, date, name)
            mycursor.execute(sql, vals)
            connection.commit()
            Successupdate()

        except EXCEPTION as e:
            print(e)
            connection.rollback()
            connection.close()


#delete customer
def DELCUS():
    name = cusname.get()

    if name == "":
        Error()
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        find = (name,)
        mycursor.execute("DELETE FROM customer WHERE Name=%s", find)
        mycursor.execute("ALTER TABLE customer AUTO_INCREMENT = 1")
        connection.commit()
        connection.close()
        Successupdate()


#search product
def search_pro_table():
    name = proname.get()

    if name == "":
        messagebox.showinfo("Error ", "Name is required")
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        try:
            val=(name,)
            mycursor.execute("SELECT * FROM product WHERE Name = %s",val)
            result = mycursor.fetchall()
            for x in result:
                print(x)
            proprice.delete(0,END)
            proprice.insert(END,x[3])
            proamount.delete(0,END)
            proamount.insert(END,x[2])
            proinfor.delete(0,END)
            proinfor.insert(END,x[4])
        except EXCEPTION as e:
            print(e)
            connection.rollback()
            connection.close


#search staff
def search_st_table():
    name = stname.get()

    if name == "":
        messagebox.showinfo("Error ", "Name is required")
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        try:
            val = (name,)
            mycursor.execute("SELECT * FROM staff WHERE Name = %s", val)
            result = mycursor.fetchall()
            for x in result:
                print(x)
            stdob.delete(0, END)
            stdob.insert(END, x[2])
            stcontact.delete(0, END)
            stcontact.insert(END, x[3])
            stjob.delete(0, END)
            stjob.insert(END, x[4])
        except EXCEPTION as e:
            print(e)
            connection.rollback()
            connection.close

#search customer
def search_cus_table():
    name = cusname.get()

    if name == "":
        messagebox.showinfo("Error ", "Name is required")
    else:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
        mycursor = connection.cursor()
        try:
            val = (name,)
            mycursor.execute("SELECT * FROM customer WHERE Name = %s", val)
            result = mycursor.fetchall()
            for x in result:
                print(x)
            cusbought.delete(0, END)
            cusbought.insert(END, x[2])
            cusamount.delete(0, END)
            cusamount.insert(END, x[3])
            cuscontact.delete(0, END)
            cuscontact.insert(END, x[5])
            cusdate.delete(0, END)
            cusdate.insert(END, x[4])
        except EXCEPTION as e:
            print(e)
            connection.rollback()
            connection.close


#show value of product
def show_pro_infor():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
    mycursor = connection.cursor()
    mycursor.execute("SELECT Id, Name, Price, Amount, Information FROM product ")
    product = mycursor.fetchall()
    print(product)

    for i in Table_product.get_children():
        print(i)

    for i in Table_product.get_children():
        Table_product.delete(i)

    for i, (id, name, price, amount, information) in enumerate(product, start=1):
        Table_product.insert("", "end", values=(id, name, price, amount, information))
    connection.close()

#show value of staff
def show_st_infor():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
    mycursor = connection.cursor()
    mycursor.execute("SELECT Id ,Name, Dob, Contact, Job FROM staff ")
    staff = mycursor.fetchall()
    print(staff)

    for i in Table_staff.get_children():
        print(i)

    for i in Table_staff.get_children():
        Table_staff.delete(i)

    for i, (id, name, dob, contact, job) in enumerate(staff, start=1):
        Table_staff.insert("", "end", values=(id, name, dob, contact, job))
    connection.close()

#show value of customer
def show_cus_infor():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
    mycursor = connection.cursor()
    mycursor.execute("SELECT Id, Name, Bought, Amount, Contact, Date FROM customer ")
    customer = mycursor.fetchall()
    print(customer)

    for i in Table_customer.get_children():
        print(i)

    for i in Table_customer.get_children():
        Table_customer.delete(i)

    for i, (id, name, bought, amount, contact, date) in enumerate(customer, start=1):
        Table_customer.insert("", "end", values=(id, name, bought, amount, contact, date))
    connection.close()

#place value of product
def place_pro_infor(self):
    proname.delete(0, END)
    proprice.delete(0, END)
    proinfor.delete(0, END)
    proamount.delete(0, END)
    row_name = Table_product.selection()[0]
    select = Table_product.set(row_name)

    proname.insert(0, select['Name'])
    proprice.insert(0, select['Price'])
    proamount.insert(0, select['Amount'])
    proinfor.insert(0, select['Information'])


#place value of staff
def place_st_infor(self):
    stname.delete(0, END)
    stdob.delete(0, END)
    stcontact.delete(0, END)
    stjob.delete(0, END)
    row_name = Table_staff.selection()[0]
    select = Table_staff.set(row_name)

    stname.insert(0, select['Name'])
    stdob.insert(0, select['DoB'])
    stcontact.insert(0, select['Contact'])
    stjob.insert(0, select['Job'])

#place value of customer
def place_cus_infor(self):
    cusname.delete(0, END)
    cusamount.delete(0, END)
    cusbought.delete(0, END)
    cuscontact.delete(0, END)
    cusdate.delete(0, END)
    row_name = Table_customer.selection()[0]
    select = Table_customer.set(row_name)

    cusname.insert(0, select['Name'])
    cusamount.insert(0, select['Amount'])
    cusbought.insert(0, select['Bought'])
    cuscontact.insert(0, select['Contact'])
    cusdate.insert(0, select['Date'])

#return to main window
def Return():
    root.destroy()
    os.startfile("Main_window.py")

#clear all entries
def Clear():
    cusname.delete(0, END)
    cusamount.delete(0, END)
    cusbought.delete(0, END)
    cuscontact.delete(0, END)
    cusdate.delete(0, END)
    stname.delete(0, END)
    stdob.delete(0, END)
    stcontact.delete(0, END)
    stjob.delete(0, END)
    proname.delete(0, END)
    proprice.delete(0, END)
    proinfor.delete(0, END)
    proamount.delete(0, END)
    search_box.delete(0, END)

#search for word have in name
def search_name():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="mid_python")
    mycursor = connection.cursor()

    selected = drop.get()
    sql = ""
    if selected == "Search In ...":
        messagebox.showinfo("Error", "What table do you like to search in ?")

    if selected == "Product":
        if search_box.get() == "":
            messagebox.showinfo("Error", "What do you like to search?")
        else:
            sql = 'SELECT * FROM product WHERE name LIKE %s'
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
    if selected == "Staff":
        if search_box.get() == "":
            messagebox.showinfo("Error", "What do you like to search?")
        else:
            sql = 'SELECT * FROM staff WHERE name LIKE %s'
            args = ['%' + search_box.get() + '%']
            result = mycursor.execute(sql, args)
            result = mycursor.fetchall()

            for i in Table_staff.get_children():
                print(i)
            for i in Table_staff.get_children():
                Table_staff.delete(i)
            for i, (id, name, birth, contact, job) in enumerate(result, start=1):
                Table_staff.insert("", "end", values=(id, name, birth, contact, job))
            connection.close()
    if selected == "Customer":
        if search_box.get() == "":
            messagebox.showinfo("Error", "What do you like to search?")
        else:
            sql = 'SELECT * FROM customer WHERE name LIKE %s'
            args = ['%' + search_box.get() + '%']
            result = mycursor.execute(sql, args)
            result = mycursor.fetchall()

            for i in Table_customer.get_children():
                print(i)
            for i in Table_customer.get_children():
                Table_customer.delete(i)
            for i, (id, name, bought, amount, contact, date) in enumerate(result, start=1):
                Table_customer.insert("", "end", values=(id, name, bought, amount, contact, date))
            connection.close()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Computer store management")
    root.geometry("1500x1000")


# styke treeview
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", rowheight=20)

#scroll product
    tree_framepro = tk.Frame(root)
    tree_framepro.pack(pady=20)
    tree_scrollpro = tk.Scrollbar(tree_framepro)
    tree_scrollpro.pack(side=tk.RIGHT,fill=tk.Y)

#scroll staff
    tree_framest = tk.Frame(root)
    tree_framest.pack(pady=20)
    tree_scrollst = tk.Scrollbar(tree_framest)
    tree_scrollst.pack(side=tk.RIGHT,fill=tk.Y)

#scroll customer
    tree_framecus = tk.Frame(root)
    tree_framecus.pack(pady=20)
    tree_scrollcus = tk.Scrollbar(tree_framecus)
    tree_scrollcus.pack(side=tk.RIGHT,fill=tk.Y)

#edit product
    tk.Label(root, text="Product name").place(x=5, y=10)
    tk.Label(root, text="Product price").place(x=5, y=60)
    tk.Label(root, text="Product amount").place(x=5, y=110)
    tk.Label(root, text="Product information").place(x=5, y=160)


    proname = tk.Entry(root)
    proname.place(x=150, y=10)

    proprice = tk.Entry(root)
    proprice.place(x=150, y=60)

    proamount = tk.Entry(root)
    proamount.place(x=150, y=110)

    proinfor = tk.Entry(root)
    proinfor.place(x=150, y=160)

#edit button product
    tk.Button(root, text="Add Product", command=lambda:[ADDPRO(),show_pro_infor()],bg="white", height=2, width=15).place(x=20, y=190)
    tk.Button(root, text="Delete Product", command=lambda:[DELPRO(),show_pro_infor()],fg="white" ,bg="black", height=2, width=15).place(x=150, y=190)
    tk.Button(root, text="Edit Product", command=lambda:[EDITPRO(),show_pro_infor()],bg="skyblue1", height=2, width=15).place(x=20, y=240)


#show table product
    Table_product = ttk.Treeview(tree_framepro, yscrollcommand=tree_scrollpro.set, columns=('ID','Name','Price','Amount','Information'), show='headings', height=4)
    Table_product.column("ID", anchor=tk.CENTER, width=50)
    Table_product.column("Name", anchor=tk.W, width=330)
    Table_product.column("Price", anchor=tk.CENTER, width=80)
    Table_product.column("Amount", anchor=tk.CENTER, width=80)
    Table_product.column("Information", anchor=tk.W, width=545)

    Table_product.heading("ID", text="ID", anchor=tk.CENTER)
    Table_product.heading("Name", text="Name", anchor=tk.CENTER)
    Table_product.heading("Price", text="Price", anchor=tk.CENTER)
    Table_product.heading("Amount", text="Amount", anchor=tk.CENTER)
    Table_product.heading("Information", text="Information", anchor=tk.CENTER)
    Table_product.pack()
    tree_scrollpro.config(command=Table_product.yview)
    tree_framepro.place(x=10, y=315)

#edit staff
    tk.Label(root, text="Staff name").place(x=430, y=10)
    tk.Label(root, text="Staff birth").place(x=430, y =60)
    tk.Label(root, text="Staff contact").place(x=430, y=110)
    tk.Label(root, text="Staff job").place(x=430, y=160)


    stname = tk.Entry(root)
    stname.place(x=555, y=10)

    stdob = tk.Entry(root)
    stdob.place(x=555, y=60)

    stcontact = tk.Entry(root)
    stcontact.place(x=555, y=110)

    stjob = tk.Entry(root)
    stjob.place(x=555, y=160)

#edit button staff
    tk.Button(root, text="Add Staff", command=lambda:[ADDST(),show_st_infor()],bg="white", height=2, width=15).place(x=445, y=190)
    tk.Button(root, text="Delete Staff", command=lambda:[DELST(),show_st_infor()],fg="white" ,bg="black", height=2, width=15).place(x=575, y=190)
    tk.Button(root, text="Edit Staff", command=lambda:[EDITST(),show_st_infor()],bg="skyblue1", height=2, width=15).place(x=445, y=240)

#show table staff
    Table_staff = ttk.Treeview(tree_framest, yscrollcommand=tree_scrollst.set, columns=('ID','Name','DoB','Contact','Job'), show='headings', height=4)
    Table_staff.column("ID", anchor=tk.CENTER, width=80)
    Table_staff.column("Name", anchor=tk.W, width=330)
    Table_staff.column("DoB", anchor=tk.CENTER, width=200)
    Table_staff.column("Contact", anchor=tk.CENTER, width=200)
    Table_staff.column("Job", anchor=tk.W, width=275)

    Table_staff.heading("ID", text="ID", anchor=tk.CENTER)
    Table_staff.heading("Name", text="Name", anchor=tk.CENTER)
    Table_staff.heading("DoB", text="Birth", anchor=tk.CENTER)
    Table_staff.heading("Contact", text="Contact", anchor=tk.CENTER)
    Table_staff.heading("Job", text="Job", anchor=tk.CENTER)
    Table_staff.pack()
    tree_scrollst.config(command=Table_staff.yview)
    tree_framest.place(x=10, y=425)


#edit customer
    tk.Label(root, text="Customer name").place(x=820, y=10)
    tk.Label(root, text="Bought product").place(x=820, y=47)
    tk.Label(root, text="Amount").place(x=820, y=84)
    tk.Label(root, text="Customer Contact").place(x=820, y=121)
    tk.Label(root, text="Bought date").place(x=820, y=160)

    cusname = Entry(root)
    cusname.place(x=960, y=10)

    cusbought = Entry(root)
    cusbought.place(x=960, y=47)

    cusamount = Entry(root)
    cusamount.place(x=960, y=84)

    cuscontact = Entry(root)
    cuscontact.place(x=960, y=121)

    cusdate = Entry(root)
    cusdate.place(x=960, y=160)

#edit button customer
    Button(root, text="Add Customer", command=lambda:[ADDCUS(),show_cus_infor()],bg="white", height=2, width=15).place(x=835, y=190)
    Button(root, text="Delete Customer", command=lambda:[DELCUS(),show_cus_infor()],fg="white" ,bg="black", height=2, width=15).place(x=965, y=190)
    Button(root, text="Edit Customer", command=lambda:[EDITCUS(),show_cus_infor()],bg="skyblue1", height=2, width=15).place(x=835, y=240)

#show table customer
    Table_customer = ttk.Treeview(tree_framecus, yscrollcommand=tree_scrollcus.set, columns=('ID','Name','Bought','Amount','Contact','Date'), show='headings', height=4)
    Table_customer.column("ID", anchor=tk.CENTER, width=80)
    Table_customer.column("Name", anchor=tk.W, width=255)
    Table_customer.column("Bought", anchor=tk.W, width=350)
    Table_customer.column("Amount", anchor=tk.CENTER, width=80)
    Table_customer.column("Contact", anchor=tk.CENTER, width=160)
    Table_customer.column("Date", anchor=tk.CENTER, width=160)

    Table_customer.heading("ID", text="ID", anchor=tk.CENTER)
    Table_customer.heading("Name", text="Name", anchor=tk.CENTER)
    Table_customer.heading("Bought", text="Bought", anchor=tk.CENTER)
    Table_customer.heading("Amount", text="Amount", anchor=tk.CENTER)
    Table_customer.heading("Contact", text="Contact", anchor=tk.CENTER)
    Table_customer.heading("Date", text="Date", anchor=tk.CENTER)
    Table_customer.pack()
    tree_scrollcus.config(command=Table_customer.yview)
    tree_framecus.place(x=10, y=535)

#edit search button
    seacrch_product_button = tk.Button(root, text="Search Product", command=lambda:search_pro_table(),bg="spring green", height=2, width=15).place(x=150,y=240)
    seacrch_staff_button = tk.Button(root, text="Search Staff", command=lambda:search_st_table(),bg="spring green", height=2, width=15).place(x=575, y=240)
    seacrch_customer_button = tk.Button(root, text="Search Customer", command=lambda:search_cus_table(),bg="spring green", height=2, width=15).place(x=965, y=240)

#edit search name
    search_box_label = tk.Label(root, text="Search name ")
    search_box_label.place(x=30, y=290)
    search_box = tk.Entry(root)
    search_box.place(x=130, y=290, width=400)
    search_button = tk.Button(root, text="Search name", command=lambda: search_name(), bg="LightCyan3",height=1, width=16)
    search_button.place(x=705, y=285)

# dropmenuiproduct
    drop = ttk.Combobox(root, value=["Search In ...", "Product", "Staff", "Customer", ])
    drop.current(0)
    drop.place(x=550, y=290)

# exit button
    exitButton = tk.Button(root, text="Exit", command=root.destroy,fg="white",bg="firebrick1", height=10, width=15).place(x=1140, y=450)

# refresh button
    refresh_Button = tk.Button(root, text='Refresh',command=lambda:[show_pro_infor(), show_cus_infor(), show_st_infor(), Clear()],bg="DeepSkyBlue2", height=17, width=15).place(x=1140,y=10)

# return button
    returnButton = tk.Button(root, text="Return to main", command=lambda: Return(), bg="hot pink", height=9,width=15).place(x=1140, y=290)

# show and place value
    show_pro_infor()
    show_st_infor()
    show_cus_infor()

    Table_product.bind('<Double-Button-1>', place_pro_infor)
    Table_staff.bind('<Double-Button-1>', place_st_infor)
    Table_customer.bind('<Double-Button-1>', place_cus_infor)


    root.mainloop()
