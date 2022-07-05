import sqlite3

def show_all():
	""" this function fetches all records in a table"""
	connection=sqlite3.connect('customer.db')
	c=connection.cursor()
	c.execute('SELECT rowid, * FROM customer')
	records=c.fetchall()
	for items in records:
		print(items)
	connection.commit()
	connection.close()

def add_one_record(first,last,email):
	""" this function add one record to the table"""
	connection=sqlite3.connect('customer.db')
	c=connection.cursor()
	c.execute("INSERT INTO customer VALUES(?,?,?)", (first,last,email))
	connection.commit()
	connection.close()
def add_many_record(list):
	""" this function adds many records to the table"""
	connection=sqlite3.connect('customer.db')
	c=connection.cursor()
	c.executemany("INSERT INTO customer VALUES(?,?,?)", list)
	connection.commit()
	connection.close()
def email_lookup(email):
	""" this function fetches all records in a table based on certain condtions (email id)"""
	connection=sqlite3.connect('customer.db')
	c=connection.cursor()
	c.execute("SELECT rowid, * FROM customer WHERE email_id = (?)", (email,))
	records=c.fetchall()
	for items in records:
		print(items)
	connection.commit()
	connection.close()



