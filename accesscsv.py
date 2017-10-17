import csv
import sqlite3

class csvprocessing:
	def __init__(self):
		conn = sqlite3.connect('rlmturk.db')
		self.c = conn.cursor()
		self.labels=None
		self.commands=[]
		self.dialogacts=[]

	def initialize_database(self):
		#initialize table 'dialog_acts'
		self.commands.append("CREATE TABLE dialog_acts (dialog_act_id int NOT NULL PRIMARY KEY, dialog_act symbol text)")
		self.commands.append("CREATE TABLE starter (starter_id int NOT NULL PRIMARY KEY, utterance text)")
		self.commands.append("CREATE TABLE mappings (mapping_id int NOT NULL PRIMARY KEY, starter_id int, dialog_act1_id int, dialog_act2_id int, dialog_act3_id int, dialog_act4_id int, FOREIGN KEY(starter_id) REFERENCES starter(starter_id), FOREIGN KEY(dialog_act1_id) REFERENCES dialog_act1(dialog_act1_id), FOREIGN KEY(dialog_act2_id) REFERENCES dialog_act2(dialog_act2_id), FOREIGN KEY(dialog_act3_id) REFERENCES dialog_act3(dialog_act3_id), FOREIGN KEY(dialog_act4_id) REFERENCES dialog_act1(dialog_act4_id))")
		self.commands.append("CREATE TABLE diakog_act1 (dialog_act1_id int NOT NULL PRIMARY KEY, utterance text, name_act1 int, FOREIGN KEY(name_act1) REFERENCES dialog_acts(dialog_act_id))")
		self.commands.append("CREATE TABLE diakog_act2 (dialog_act2_id int NOT NULL PRIMARY KEY, utterance text, name_act2 int, FOREIGN KEY(name_act2) REFERENCES dialog_acts(dialog_act_id))")
		self.commands.append("CREATE TABLE diakog_act3 (dialog_act3_id int NOT NULL PRIMARY KEY, utterance text, name_act3 int, FOREIGN KEY(name_act3) REFERENCES dialog_acts(dialog_act_id))")
		self.commands.append("CREATE TABLE diakog_act4 (dialog_act4_id int NOT NULL PRIMARY KEY, utterance text, name_act4 int, FOREIGN KEY(name_act4) REFERENCES dialog_acts(dialog_act_id))")

	def prcessrow(self,arx):
		

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
		return arr		

csvp = csvprocessing()
csvp.processcsv()
