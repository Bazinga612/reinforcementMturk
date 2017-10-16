import csv
import sqlite3

class csvprocessing:
	def __init__(self):
		conn = sqlite3.connect('rlmturk.db')
		self.c = conn.cursor()
		self.labels=None
		self.commands=[]

	def initialize_database(self):
		#initialize table 'dialog_acts'
		self.commands.append("CREATE TABLE dialog_acts (date text, trans text, symbol text, qty real, price real)")
		self.commands.append("")

	def properprint(self,arx):
		for j in range(len(arx)):
			print(j,arx[j])

	def processcsv(self):
		with open('tv_movie_combined.csv', 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			k,lmt=0,100

			for row in spamreader:
				rowx=self.combinefunc(row)
				if k==0:
					self.labels=rowx
				#print(len(rowx),rowx)
				#self.properprint(rowx)
				k+=1
				if k==lmt:
					break;
			print("Labels",self.labels)

	def combinefunc(self,arr):
		#print("\nThe input array is",arr)
		stat,addons=0,0
		for j in range(len(arr)-addons):
			#print("Stat is",stat,arr[j-addons])
			if len(arr[j-addons])==0:
				continue;
			else:
				temparrx=[ord(f) for f in arr[j-addons]]
				if stat==0:
					if temparrx.count(34)%2==1:
						tempstr=arr[j-addons] if temparrx[0]!=34 else arr[j-addons][1:]
						stat=1
					else: 
						continue;
				elif stat==1:
					tempstr+=', '
					tempstr+=arr[j-addons]
					arr[j-1-addons]=tempstr
					arr.pop(j-addons)
					if temparrx.count(34)%2==1:	
						stat=0						
					addons+=1
			#print("tempstr=",tempstr)
			#print("arr=",arr)
		#print("The output array is",arr)
		return arr		

csvp = csvprocessing()
csvp.processcsv()
