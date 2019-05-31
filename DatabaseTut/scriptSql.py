import sqlite3

def create_table():
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()


def insert(item,quantity,price):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM store")
	rows=cur.fetchall()
	conn.close()
	return rows


def Delete(item):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("DELETE  FROM store WHERE item=?",(item,))
	conn.commit()
	conn.close()
	
def update(qty,price,item):
	conn=sqlite3.connect("lite.db")
	cur=conn.cursor()
	cur.execute("UPDATE  store  SET quantity=? , price=? WHERE item=?",(qty,price,item))
	conn.commit()
	conn.close()



# Delete("Wine Glass")
update(100,5,'Water Glass')


rows=view()
for r in rows:
	print(r)
# insert('Water Glass',250,7.60)
