import sqlite3
conn = sqlite3.connect('rlmturk.db')
c = conn.cursor()

class execit:
	def runit(self):
		inf = open('commands.sql','r')
		inl = inf.readlines()
		for line in inl:
			if line[0]!='#':
				print(line)
				c.execute(line)

ex1=execit()
ex1.runit()
