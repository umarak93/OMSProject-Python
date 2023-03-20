import sqlite3

################################## connect to database##################################
conn = sqlite3.connect("orders.db")

##########create a cursor that connects to above connection
c = conn.cursor()

############################# create a table ############################################ 

#c.execute("""CREATE TABLE orders (
#		order_id DATATYPE integer,
#		customer_name DATATYPE text,
#		drink DATATYPE text,
#		size DATATYPE text,
#		extras DATATYPE text,
#		price DATATYPE real
#	)""")

############################ populate a single row ######################################

#many_orders = [
#				(4, 'Mike', 'Cappucino', 'S', 'sandwich', 5.00),
#				(5, 'Luke', 'Tea', 'L', 'N/A', 1.50),
#				(6, 'Robin', 'Hot Chocolate', 'M', 'Pastry', 4.80),
#			]
#c.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?)", many_orders)

############################# populate a single row ######################################

#c.execute("INSERT INTO orders VALUES (03, 'Sarah', 'Flat White', 'M', 'FlapJack', 2.00)")

############################## Update the database ######################################

#c.execute("UPDATE orders SET price = 3.00 WHERE order_id = 03")

#conn.commit()

############################### Delete a record ########################################

#c.execute("DELETE from orders WHERE drink = 'Hot Chocolate'")

#conn.commit()

############################### Delete the table ########################################

#c.execute("DROP TABLE customers")
#conn.commit

############################# Query the database #########################################

c.execute("SELECT * FROM orders ORDER BY price DESC")
#c.execute("SELECT * FROM orders WHERE price < 4.00")
#c.fetchone()
#c.fetchmany(3)

items = c.fetchall()
for item in items:
	print(str(item[0]) + " | " + item[1] + " | " + item[2] + " | " + item[3] + " | " + item[4] + " | " + str(item[5]))

print("Command executed successfully...")

############################ Define a function ##########################################

#def show_all():
#	conn = sqlite3.connect('orders.db')
	
#	c = conn.cursor()

#	c.execute("SELECT * FROM orders")
#	items = c.fetchall()

#	for item in items:
#		print(str(item[0]) + " | " + item[1] + " | " + item[2] + " | " + item[3] + " | " + item[4] + " | " + str(item[5]))

#commit the command
conn.commit()

#close the connection
conn.close()

#Add a new record to the table
#def add_one(order_id, customer_name,drink,size,extras,price):
#	conn =sqlite3.connect('orders.db')
#	c = conn.cursor()
#	c.execute("INSERT INTO orders VALUES (?,?,?,?,?,?)" (order_id, customer_name,drink,size,extras,price))
#	#commit the command
#	conn.commit()
#	#close the connection
#	conn.close()