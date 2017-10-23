import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO stocks VALUES ('2007-01-05','SELL','HOLYMOLY',100,315.14)")
c.execute("INSERT INTO stocks VALUES ('2008-01-05','BUY','DOLLAR',100,351.14)")
c.execute("INSERT INTO stocks VALUES ('2009-01-05','SELL','RUPEE',100,5.124)")
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()