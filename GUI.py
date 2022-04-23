from datetime import datetime
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from functools import partial

now = datetime.now()

CREATE_GROCERIES = "CREATE TABLE IF NOT EXISTS groceries (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_HOUSEHOLD = "CREATE TABLE IF NOT EXISTS household (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_ENTERTAINMENT = "CREATE TABLE IF NOT EXISTS entertainment (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, " \
                       "date DATE);"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"

INSERT_GROCERIES = "INSERT INTO groceries (good, price, date) VALUES(?,?,?);"
INSERT_HOUSEHOLD = "INSERT INTO household (good, price, date) VALUES(?,?,?);"
INSERT_ENTERTAINMENT = "INSERT INTO entertainment (good, price, date) VALUES(?,?,?);"
INSERT_OTHER = "INSERT INTO other (good, price, date) VALUES(?,?,?);"

SELECT_ALL_GROCERIES = "SELECT * FROM groceries;"
SELECT_ALL_HOUSEHOLD = "SELECT * FROM household;"
SELECT_ALL_ENTERTAINMENT = "SELECT * FROM entertainment;"
SELECT_ALL_OTHER = "SELECT * FROM other;"

SELECT_GROCERIES = "SELECT * FROM groceries WHERE good = ?;"
SELECT_HOUSEHOLD = "SELECT * FROM household WHERE good = ?;"
SELECT_ENTERTAINMENT = "SELECT * FROM entertainment WHERE good = ?;"
SELECT_OTHER = "SELECT * FROM other WHERE good = ?;"

DELETE_GROCERIES = "DELETE FROM groceries WHERE good = ? AND price = ?;"
DELETE_HOUSEHOLD = "DELETE FROM household WHERE good = ? AND price = ?;"
DELETE_ENTERTAINMENT = "DELETE FROM entertainment WHERE good = ? AND price = ?;"
DELETE_OTHER = "DELETE FROM other WHERE good = ? AND price = ?;"


def create_grocery_table():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_GROCERIES)

def create_entertainment_table():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_ENTERTAINMENT)

def create_household_table():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_HOUSEHOLD)

def create_other_table():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_OTHER)


def insert_groceries(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_GROCERIES, (good, price, date))
        conn.commit()

def insert_entertainment(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_ENTERTAINMENT, (good, price, date))
        conn.commit()

def insert_household(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_HOUSEHOLD, (good, price, date))
        conn.commit()

def insert_other(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_OTHER, (good, price, date))
        conn.commit()


def select_all_groceries():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_GROCERIES)
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + '   ' + str(x[2]) + '   ' + '   ' + str(x[3]) + '\n'
        return output

def select_all_entertainment():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_ENTERTAINMENT)
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + '   ' + str(x[2]) + '   ' + '   ' + str(x[3]) + '\n'
        return output

def select_all_household():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_HOUSEHOLD)
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + '   ' + str(x[2]) + '   ' + '   ' + str(x[3]) + '\n'
        return output

def select_all_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_OTHER)
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + '   ' + str(x[2]) + '   ' + '   ' + str(x[3]) + '\n'
        return output


def delete_grocery(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_GROCERIES, (good, price))
        conn.commit()
        c.close()

def delete_entertainment(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ENTERTAINMENT, (good, price))
        conn.commit()
        c.close()

def delete_household(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_HOUSEHOLD, (good, price))
        conn.commit()
        c.close()

def delete_other(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_OTHER, (good, price))
        c.close()
        conn.commit()

# ------- GUI Code Begins ----------


def viewGrocery():
    grocery = tk.Toplevel(padx=100, pady=100)
    label = Label(grocery, text=select_all_groceries())
    label.grid(column=0, row=0)
    totalLabel = Label(grocery, text="Total")
    totalLabel.grid(column=0, row=1)

    def addGrocery():
        add = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(add, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(add, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(add, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(add, width=25)
        item.grid(column=0, row=2)
        price = Entry(add, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            insert_item = str(item.get())
            insert_price = float(price.get())
            totalGrocery = 0
            totalGrocery = totalGrocery + insert_price
            totalValue = Label(grocery, text=totalGrocery)
            totalValue.grid(column=0, row=2)
            insert_groceries(insert_item, insert_price, now)
            add.destroy()
            grocery.destroy()
            viewGrocery()

        def cancelClicked():
            add.destroy()

        ok_btn= Button(add, text= "Confirm", command=partial(okClicked))
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn=Button(add, text= 'Cancel', command=partial(cancelClicked))
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    def delGrocery():
        delete = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(delete, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(delete, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(delete, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(delete, width=25)
        item.grid(column=0, row=2)
        price = Entry(delete, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            delete_item = str(item.get())
            delete_price = float(price.get())
            delete_grocery(delete_item, delete_price)
            delete.destroy()
            grocery.destroy()
            viewGrocery()

        def cancelClicked():
            delete.destroy()

        ok_btn= Button(delete, text= "Confirm", command=okClicked)
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn=Button(delete, text= 'Cancel', command=cancelClicked)
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    add_btn= Button(grocery, text="Add Item", command=addGrocery)
    add_btn.grid(column=0, row=3, padx=10, pady=4, ipadx=20, ipady=15)
    delete_btn= Button(grocery, text="Delete Item", command=delGrocery)
    delete_btn.grid(column=0, row=4, padx=10, pady=4, ipadx=14, ipady=15)

def viewEntertainment():
    entertainment=tk.Toplevel(padx=100, pady=100)
    label = Label(entertainment, text=select_all_entertainment())
    label.grid(column=0, row=0)

    def addEntertainment():
        add = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(add, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(add, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(add, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(add, width=25)
        item.grid(column=0, row=2)
        price = Entry(add, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            insert_item = str(item.get())
            insert_price = float(price.get())
            totalEntertainment = 0
            totalEntertainment = totalEntertainment + insert_price
            totalValue = Label(entertainment, text=totalEntertainment)
            totalValue.grid(column=1, row=1)
            insert_entertainment(insert_item, insert_price, now)
            add.destroy()
            entertainment.destroy()
            viewEntertainment()

        def cancelClicked():
            add.destroy()

        ok_btn= Button(add, text= "Confirm", command=okClicked)
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn=Button(add, text= 'Cancel', command=cancelClicked)
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    def delEntertainment():
        delete = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(delete, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(delete, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(delete, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(delete, width=25)
        item.grid(column=0, row=2)
        price = Entry(delete, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            delete_item = str(item.get())
            delete_price = float(price.get())
            delete_entertainment(delete_item, delete_price)
            delete.destroy()
            entertainment.destroy()
            viewEntertainment()

        def cancelClicked():
            delete.destroy()

        ok_btn = Button(delete, text="Confirm", command=okClicked)
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn = Button(delete, text='Cancel', command=cancelClicked)
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    add_btn= Button(entertainment, text="Add Item", command=addEntertainment)
    add_btn.grid(column=0, row=1, padx=10, pady=4, ipadx=20, ipady=15)
    delete_btn= Button(entertainment, text="Delete Item", command=delEntertainment)
    delete_btn.grid(column=0, row=2, padx=10, pady=4, ipadx=14, ipady=15)

def viewHousehold():
    household=tk.Toplevel(padx=100, pady=100)
    label = Label(household, text=select_all_household())
    label.grid(column=0, row=0)

    def addHousehold():
        add = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(add, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(add, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(add, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(add, width=25)
        item.grid(column=0, row=2)
        price = Entry(add, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            insert_item = str(item.get())
            insert_price = float(price.get())
            insert_household(insert_item, insert_price, now)
            add.destroy()
            household.destroy()
            viewHousehold()

        def cancelClicked():
            add.destroy()

        ok_btn= Button(add, text= "Confirm", command=okClicked)
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn=Button(add, text= 'Cancel', command=cancelClicked)
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    def delHousehold():
        delete = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(delete, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(delete, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(delete, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(delete, width=25)
        item.grid(column=0, row=2)
        price = Entry(delete, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            delete_item = str(item.get())
            delete_price = float(price.get())
            delete_household(delete_item, delete_price)
            delete.destroy()
            household.destroy()
            viewHousehold()

        def cancelClicked():
            delete.destroy()

        ok_btn = Button(delete, text="Confirm", command=okClicked)
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn = Button(delete, text='Cancel', command=cancelClicked)
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    add_btn= Button(household, text="Add Item", command=addHousehold)
    add_btn.grid(column=0, row=1, padx=10, pady=4, ipadx=20, ipady=15)
    delete_btn= Button(household, text="Delete Item", command= delHousehold)
    delete_btn.grid(column=0, row=2, padx=10, pady=4, ipadx=14, ipady=15)

def viewOther():
    other = tk.Toplevel(padx=100, pady=100)
    label = Label(other, text=select_all_other())
    label.grid(column=0, row=0)
    def addOther():
        add = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(add, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(add, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(add, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(add, width=25)
        item.grid(column=0, row=2)
        price = Entry(add, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            insert_item = str(item.get())
            insert_price = float(price.get())
            insert_other(insert_item, insert_price, now)
            add.destroy()
            other.destroy()
            viewOther()

        def cancelClicked():
            add.destroy()

        ok_btn= Button(add, text= "Confirm", command=okClicked)
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn=Button(add, text= 'Cancel', command=cancelClicked)
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    def delOther():
        delete = tk.Toplevel(padx=100, pady=100)
        heading_lbl = Label(delete, text="Enter Item name and price", font=('helvetica', '20'))
        heading_lbl.grid(column=0, row=0, padx=20, pady=20)
        item_lbl = Label(delete, text='Item')
        item_lbl.grid(column=0, row=1)
        price_lbl = Label(delete, text='Price')
        price_lbl.grid(column=1, row=1)
        item = Entry(delete, width=25)
        item.grid(column=0, row=2)
        price = Entry(delete, width=15)
        price.grid(column=1, row=2)

        def okClicked():
            delete_item = str(item.get())
            delete_price = float(price.get())
            delete_other(delete_item, delete_price)
            delete.destroy()
            other.destroy()
            viewOther()

        def cancelClicked():
            delete.destroy()

        ok_btn = Button(delete, text="Confirm", command=okClicked)
        ok_btn.grid(column=0, row=3, padx=10, pady=20, ipadx=10, ipady=10)
        cancel_btn = Button(delete, text='Cancel', command=cancelClicked)
        cancel_btn.grid(column=1, row=3, padx=10, pady=20, ipadx=12, ipady=10)

    add_btn= Button(other, text="Add Item", command=addOther)
    add_btn.grid(column=0, row=1, padx=10, pady=4, ipadx=20, ipady=15)
    delete_btn= Button(other, text="Delete Item", command=delOther)
    delete_btn.grid(column=0, row=2, padx=10, pady=4, ipadx=14, ipady=15)


def mainWindow():
    root = Tk()
    root.title("Expense Tracker")
    root.geometry("520x350")
    headinglbl = Label(root, text="Expense Tracker", font=('helvetica', '30'))
    headinglbl.grid(column=0, row=0, pady=20, columnspan=3)
    grocery_btn = Button(root, text="View Grocery Table", command=partial(viewGrocery))
    grocery_btn.grid(column=0, row=1, padx=20, pady=20, ipadx=20, ipady=20)
    entertainment_btn = Button(root, text= "View Entertainment Table", command=partial(viewEntertainment))
    entertainment_btn.grid(column=1, row=1, padx=20, pady=20, ipadx=20, ipady=20)
    household_btn = Button(root, text= "View Household Table", command=partial(viewHousehold))
    household_btn.grid(column=0, row=2, padx=20, pady=20, ipadx=20, ipady=20)
    other_btn = Button(root, text="View Other Table", command=partial(viewOther))
    other_btn.grid(column=1, row=2, padx=20, pady=20, ipadx=20, ipady=20)
    root.mainloop()
# ---------------- main ---------


mainWindow()

