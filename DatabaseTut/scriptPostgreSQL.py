import psycopg2


def create_table():
	conn=psycopg2.connect("dbname='myDB' user='postgres' password='postgres123' host='localhost' port='5432' ")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()


def insert(item,quantity,price):
	conn=psycopg2.connect("dbname='myDB' user='postgres' password='postgres123' host='localhost' port='5432' ")
	cur=conn.cursor()
	cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
	conn.commit()
	conn.close()

def view():
	conn=psycopg2.connect("dbname='myDB' user='postgres' password='postgres123' host='localhost' port='5432' ")
	cur=conn.cursor()
	cur.execute("SELECT * FROM store")
	rows=cur.fetchall()
	conn.close()
	return rows


def Delete(item):
	conn=psycopg2.connect("dbname='myDB' user='postgres' password='postgres123' host='localhost' port='5432' ")
	cur=conn.cursor()
	cur.execute("DELETE  FROM store WHERE item=%s",(item,))
	conn.commit()
	conn.close()
	
def update(qty,price,item):
	conn=psycopg2.connect("dbname='myDB' user='postgres' password='postgres123' host='localhost' port='5432' ")
	cur=conn.cursor()
	cur.execute("UPDATE  store  SET quantity=%s , price=%s WHERE item=%s",(qty,price,item))
	conn.commit()
	conn.close()


# create_table()
insert('Apple',250,7.60)

# Delete("Orange")
# update(100,5,'Orange')


rows=view()
for r in rows:
	print(r)

# # insert('Water Glass',250,7.60)
