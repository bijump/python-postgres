import psycopg2

conn = psycopg2.connect(database="Inventory",
                        host="localhost",
                        user="postgres",
                        password="pass@123",
                        port="5432")
cursor = conn.cursor()

cursor.execute("SELECT * FROM product")
print(cursor.fetchall())

itm='raw rice'

cursor.execute(f'''INSERT INTO product values(105,'{itm}')''')
conn.commit()
cursor.execute("SELECT * FROM product")
print(cursor.fetchall())



conn.close()