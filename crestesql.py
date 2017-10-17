import csv
import sqlite3

class csvprocessing:
	def __init__(self):
		conn = sqlite3.connect('rlmturk.db')
		self.c = conn.cursor()
		self.labels=None
		self.commands=[]
		self.dialogact_commands=[]
		self.mapping_commands=[]
		self.starter_commands=[]
		self.dialog_act1_commands=[]
		self.dialog_act2_commands=[]
		self.dialog_act3_commands=[]
		self.dialog_act4_commands=[]
		self.dialogacts={}
		self.starters={}
		self.dialogacts1={}
		self.dialogacts2={}
		self.dialogacts3={}
		self.dialogacts4={}
		self.counter={'starter':0,'da':0,'da1':0,'da1':0,'da2':0,'da3':0,'da4':0,'mapping_no':0}

	def initialize_database(self):
		#initialize table 'dialog_acts'
		self.commands.append("CREATE TABLE dialog_acts (dialog_act_id int NOT NULL PRIMARY KEY, dialog_act text);")
		self.commands.append("CREATE TABLE starter (starter_id int NOT NULL PRIMARY KEY, utterance text);")
		self.commands.append("CREATE TABLE mappings (mapping_id int NOT NULL PRIMARY KEY, starter_id int, dialog_act1_id int, dialog_act2_id int, dialog_act3_id int, dialog_act4_id int, FOREIGN KEY(starter_id) REFERENCES starter(starter_id), FOREIGN KEY(dialog_act1_id) REFERENCES dialog_act1(dialog_act1_id), FOREIGN KEY(dialog_act2_id) REFERENCES dialog_act2(dialog_act2_id), FOREIGN KEY(dialog_act3_id) REFERENCES dialog_act3(dialog_act3_id), FOREIGN KEY(dialog_act4_id) REFERENCES dialog_act1(dialog_act4_id));")
		self.commands.append("CREATE TABLE dialog_act1 (dialog_act1_id int NOT NULL PRIMARY KEY, utterance text, name_act1 int, FOREIGN KEY(name_act1) REFERENCES dialog_acts(dialog_act_id));")
		self.commands.append("CREATE TABLE dialog_act2 (dialog_act2_id int NOT NULL PRIMARY KEY, utterance text, name_act2 int, FOREIGN KEY(name_act2) REFERENCES dialog_acts(dialog_act_id));")
		self.commands.append("CREATE TABLE dialog_act3 (dialog_act3_id int NOT NULL PRIMARY KEY, utterance text, name_act3 int, FOREIGN KEY(name_act3) REFERENCES dialog_acts(dialog_act_id));")
		self.commands.append("CREATE TABLE dialog_act4 (dialog_act4_id int NOT NULL PRIMARY KEY, utterance text, name_act4 int, FOREIGN KEY(name_act4) REFERENCES dialog_acts(dialog_act_id));")

	def processrow(self,arx):
		#dialog_act_1 	
		if len(arx[0])!=0:
			if self.dialogacts.get(arx[0],-1)==-1:
				self.dialogacts[arx[0]]=self.counter['da']
				da1id=self.counter['da']
				self.counter['da']+=1
			else:
				da1id=self.dialogacts[arx[0]]
		else:
			da1id=None
		#dialog_act_2
		if len(arx[1])!=0:
			if self.dialogacts.get(arx[1],-1)==-1:
				self.dialogacts[arx[1]]=self.counter['da']
				da2id=self.counter['da']
				self.counter['da']+=1
			else:
				da2id=self.dialogacts[arx[1]]
		else:
			da2id=None
		#dialog_act_3
		if len(arx[2])!=0: 
			if self.dialogacts.get(arx[2],-1)==-1:
				self.dialogacts[arx[2]]=self.counter['da']
				da3id=self.counter['da']
				self.counter['da']+=1
			else:
				da3id=self.dialogacts[arx[2]]
		else:
			da3id=None
		#dialog_act_4
		if len(arx[3])!=0:
			if self.dialogacts.get(arx[3],-1)==-1:
				self.dialogacts[arx[3]]=self.counter['da']
				da4id=self.counter['da']
				self.counter['da']+=1
			else:
				da4id=self.dialogacts[arx[3]]
		else:
			da4id=None
		#slot0 or starter
		if len(arx[12])!=0:
			if self.starters.get(arx[12],-1)==-1:
				self.starters[arx[12]]=self.counter['starter']
				starterid=self.counter['starter']
				self.counter['starter']+=1
			else:
				starterid=self.starters[arx[12]]
		else:
			starterid=None
		#slot1
		if da1id!=None:
			if self.dialogacts1.get(arx[13],-1)==-1:
				self.dialogacts1[arx[13]]=(self.counter['da1'],da1id)
				dact1id=self.counter['da1']
				self.counter['da1']+=1
			else:
				dact1id=self.dialogacts1[arx[13]][0]
		else:
			dact1id=None
		#slot2
		if da2id!=None:
			if self.dialogacts2.get(arx[14],-1)==-1:
				self.dialogacts2[arx[14]]=(self.counter['da1'],da2id)
				dact2id=self.counter['da2']
				self.counter['da2']+=1
			else:
				dact2id=self.dialogacts2[arx[14]][0]
		else:
			dact2id=None
		#slot3
		if da3id!=None:
			if self.dialogacts3.get(arx[15],-1)==-1:
				self.dialogacts3[arx[15]]=(self.counter['da3'],da3id)
				dact3id=self.counter['da3']
				self.counter['da3']+=1
			else:
				dact3id=self.dialogacts3[arx[15]][0]
		else:
			dact3id=None
		#slot4
		if da4id!=None:
			if self.dialogacts4.get(arx[16],-1)==-1:
				self.dialogacts4[arx[16]]=(self.counter['da4'],da4id)
				dact4id=self.counter['da4']
				self.counter['da4']+=1
			else:
				dact4id=self.dialogacts4[arx[16]][0]
		else:
			dact4id=None
		commandx = "INSERT INTO mappings VALUES ("
		commandx += str(self.counter['mapping_no'])			#adding mappingid
		commandx +=", "
		commandx += str(starterid)
		commandx +=", "
		commandx += str(dact1id)
		commandx +=", "		
		commandx += str(dact2id)
		commandx +=", "
		commandx += str(dact3id)
		commandx +=", "
		commandx += str(dact4id)
		commandx += ");"
		#print(commandx)
		#print("da1234id",da1id,da2id,da3id,da4id)
		self.mapping_commands.append(commandx)
		self.counter['mapping_no']+=1

	def createalltables(self):
		for key in self.dialogacts.keys():
			commandx = "INSERT INTO dialog_acts VALUES ("
			commandx += str(self.dialogacts[key])
			commandx += ", \""
			commandx += key
			commandx += "\");"
			self.dialogact_commands.append(commandx)		

		for key in self.starters.keys():
			commandx = "INSERT INTO starter VALUES ("
			commandx += str(self.starters[key])
			if ord(key[0])!=34:
				commandx += ", \""
			else:
				commandx += ", "
			commandx += key
			if ord(key[-1])!=34:
				commandx += "\") "
			else:
				commandx += ") "
			self.starter_commands.append(commandx)

		for key in self.dialogacts1.keys():
			retrieved=self.dialogacts1[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO dialog_act1 VALUES ("
			commandx += str(did1)
			if ord(key[0])!=34:
				commandx += ", \""
			else:
				commandx += ", "
			commandx += key
			if ord(key[-1])!=34:
				commandx += "\", "
			else:
				commandx += ", "
			commandx += str(dactid)
			commandx += ");"
			self.dialog_act1_commands.append(commandx)

		for key in self.dialogacts2.keys():
			retrieved=self.dialogacts2[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO dialog_act2 VALUES ("
			commandx += str(did1)
			if ord(key[0])!=34:
				commandx += ", \""
			else:
				commandx += ", "
			commandx += key
			if ord(key[-1])!=34:
				commandx += "\", "
			else:
				commandx += ", "
			commandx += str(dactid)
			commandx += ");"
			self.dialog_act2_commands.append(commandx)

		for key in self.dialogacts3.keys():
			retrieved=self.dialogacts3[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO dialog_act3 VALUES ("
			commandx += str(did1)
			if ord(key[0])!=34:
				commandx += ", \""
			else:
				commandx += ", "
			commandx += key
			if ord(key[-1])!=34:
				commandx += "\", "
			else:
				commandx += ", "
			commandx += str(dactid)
			commandx += ");"
			self.dialog_act3_commands.append(commandx)

		for key in self.dialogacts4.keys():
			retrieved=self.dialogacts4[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO dialog_act4 VALUES ("
			commandx += str(did1)
			if ord(key[0])!=34:
				commandx += ", \""
			else:
				commandx += ", "
			commandx += key
			if ord(key[-1])!=34:
				commandx += "\", "
			else:
				commandx += ", "
			commandx += str(dactid)
			commandx += ");"
			self.dialog_act4_commands.append(commandx)


	def writeallcommands(self):
		ofile=open("commands.sql",'w')
		#create_table_commands
		ofile.write("# create table commands!\n")
		for comx in self.commands:
			ofile.write(comx+"\n")

		ofile.write("\n\n#Dialog acts table commands\n")
		for comx in self.dialogact_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#Starter table commands\n")
		for comx in self.starter_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#Dialog acts1 table commands\n")
		for comx in self.dialog_act1_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#Dialog acts2 table commands\n")
		for comx in self.dialog_act2_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#Dialog acts3 table commands\n")
		for comx in self.dialog_act3_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#Dialog acts4 table commands\n")
		for comx in self.dialog_act4_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#Mapping commands\n")
		for comx in self.mapping_commands:
			ofile.write(comx+'\n')

	def processcsv(self):
		with open('tv_movie_combined.csv', 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			k,lmt=0,50

			for row in spamreader:
				rowx=self.combinefunc(row)
				if k==0:
					self.labels=rowx
					k+=1
					continue;	
				#print(len(rowx),rowx)
				#self.properprint(rowx)
				k+=1
				self.processrow(rowx)
				if k==lmt:
					break;
			#print("Labels",self.labels)
		self.initialize_database()
		self.createalltables()
		self.writeallcommands()


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
