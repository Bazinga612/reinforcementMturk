import sqlite3
conn = sqlite3.connect('rlmturk.db')
c = conn.cursor()

query0 = "SHOW TABLES"
#print("First utterances (slot1) of conversations which start with I STILL think ""Monty Python and the Holy Grail"" is funny.")

def processcommand(commandx):
	count=0
	for row in c.execute(commandx):
		print(row)
		count+=1
	print(count,"rows retrieved!")

processcommand(query0)