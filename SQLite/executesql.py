import sqlite3
conn = sqlite3.connect('rlmturk.db')
c = conn.cursor()

class execit:
	def __init__(self):
		self.flagged=[]

	def runit(self):		
		inf = open('commands.sql','r')
		inl = inf.readlines()
		cnt=0
		print(len(inl),"total lines")
		for line in inl:
			if line[0]!='#':
				#print(line)
				try:
					c.execute(line)
				except:
					self.flagged.append(line)
		print(len(self.flagged),"flagged commands!")
		for ln in self.flagged:
			print(ln)

ex1=execit()
ex1.runit()
conn.commit()