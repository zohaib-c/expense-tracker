from datetime import datetime
import sqlite3

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
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
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
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
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
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
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
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


def select_grocery(good):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_GROCERIES, (good,))
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_entertainment(good):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ENTERTAINMENT, (good,))
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_household(good):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_HOUSEHOLD, (good,))
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_other(good):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_OTHER, (good,))
        print_list = c.fetchall()
        c.close()
        output = ''
        for x in print_list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
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
        conn.commit()
        c.close()
# -------------main-------------------------------------------


# only needs to run once
# create_grocery_table()
# create_other_table()
# create_household_table()
# create_entertainment_table()

# to insert
enter=str(input('Would you like to enter an item?\n'))
while enter == 'yes':
    type_item=str(input("What type of item is this?\n"))
    item=str(input('Input the item name\n'))
    cost=int(input('Input the item price\n'))

    if type_item=='grocery':
        insert_groceries(item, cost, now)
    elif type_item=='entertainment':
        insert_entertainment(item, cost, now)
    elif type_item == 'household':
        insert_household(item, cost, now)
    elif type_item == 'other':
        insert_other(item, cost, now)

    enter=str(input('Would you like to enter another item?\n'))

# to print entire table
to_print = str(input("Would you like to print a table?\n"))
while to_print == 'yes':
    select_table = str(input("What table would you like to print?\n"))

    if select_table=='grocery':
        print (select_all_groceries())
    elif select_table=='entertainment':
        print (select_all_entertainment())
    elif select_table == 'household':
        print (select_all_household())
    elif select_table == 'other':
        print (select_all_other())

    to_print = str(input("Would you like to print another table?\n"))

# to print specific items
item_print = str(input("Would you like to print a certain item?\n"))
while item_print == 'yes':
    select_table = str(input("From what table would you like to print?\n"))
    select_item = str(input("What is the name of the item?\n"))

    if select_table=='grocery':
        print (select_grocery(select_item))
    elif select_table=='entertainment':
        print (select_entertainment(select_item))
    elif select_table == 'household':
        print (select_household(select_item))
    elif select_table == 'other':
        print (select_other(select_item))

    item_print = str(input("Would you like to print another certain item?\n"))

# to delete specific item
item_delete = str(input("Would you like to delete an item?\n"))
while item_delete == 'yes':
    select_table = str(input("From what table would you like to delete?\n"))
    select_item_delete = str(input("What is the name of the item?\n"))
    select_cost = str(input("What is the cost of the item?\n"))

    if select_table=='grocery':
        delete_grocery(select_item_delete, select_cost)
        print ("item deleted, here is the new table\n")
        print(select_all_groceries())
    elif select_table=='entertainment':
        delete_entertainment(select_item_delete, select_cost)
        print("item deleted, here is the new table\n")
        print(select_all_entertainment())
    elif select_table == 'household':
        delete_household(select_item_delete, select_cost)
        print("item deleted, here is the new table\n")
        print(select_all_household())
    elif select_table == 'other':
        delete_other(select_item_delete, select_cost)
        print("item deleted, here is the new table\n")
        print(select_all_other())

    item_delete = str(input("Would you like to delete another item?\n"))

