import csv
import sqlite3

class csvprocessing:
	def __init__(self):
		self.labels=None
		self.commands=[]
		self.dialogact_commands=[]
		self.mapping_commands=[]
		self.starter_commands=[]
		self.slot1_commands=[]
		self.slot2_commands=[]
		self.slot3_commands=[]
		self.slot4_commands=[]
		self.slot5_commands=[]
		self.dialogacts={}
		self.starters={}
		self.slots1={}
		self.slots2={}
		self.slots3={}
		self.slots4={}
		self.slots5={}
		self.counter={'starter':0,'da':0,'da1':0,'da1':0,'da2':0,'da3':0,'da4':0,'da5':0,'mapping_no':0}
		self.files=['tv_movie_combined.csv','Combined_General_long.csv','Combined_General_short.csv']

	def mainprocess(self):
		self.initialize_database()
		for fname in self.files:
			print("sent",fname,"for processing!")
			self.processcsv(fname)
		self.createalltables()
		self.writeallcommands()

	def processcsv(self,fname):
		with open('../datasets/' + fname, 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			k,lmt=0,0

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
				#if k==lmt:
				#	break;
			#print("Labels",self.labels)		

	def initialize_database(self):
		#initialize table 'dialog_acts'
		self.commands.append("CREATE TABLE dialog_acts (dialog_act_id int NOT NULL PRIMARY KEY, dialog_act text);")
		self.commands.append("CREATE TABLE starter (starter_id int NOT NULL PRIMARY KEY, utterance text);")
		self.commands.append("CREATE TABLE mappings (mapping_id int NOT NULL PRIMARY KEY, starter_id int, slot1_id int, slot2_id int, slot3_id int, slot4_id int, FOREIGN KEY(starter_id) REFERENCES starter(starter_id), FOREIGN KEY(slot1_id) REFERENCES slot1(slot1_id), FOREIGN KEY(slot2_id) REFERENCES slot2(slot2_id), FOREIGN KEY(slot3_id) REFERENCES slot3(slot3_id), FOREIGN KEY(slot4_id) REFERENCES slot4(slot4_id));")
		self.commands.append("CREATE TABLE slot1 (slot1_id int NOT NULL PRIMARY KEY, utterance1 text, name_act1 int, FOREIGN KEY(name_act1) REFERENCES dialog_acts(dialog_act_id));")
		self.commands.append("CREATE TABLE slot2 (slot2_id int NOT NULL PRIMARY KEY, utterance2 text, name_act2 int, FOREIGN KEY(name_act2) REFERENCES dialog_acts(dialog_act_id));")
		self.commands.append("CREATE TABLE slot3 (slot3_id int NOT NULL PRIMARY KEY, utterance3 text, name_act3 int, FOREIGN KEY(name_act3) REFERENCES dialog_acts(dialog_act_id));")
		self.commands.append("CREATE TABLE slot4 (slot4_id int NOT NULL PRIMARY KEY, utterance4 text, name_act4 int, FOREIGN KEY(name_act4) REFERENCES dialog_acts(dialog_act_id));")
		self.commands.append("CREATE TABLE slot5 (slot5_id int NOT NULL PRIMARY KEY, utterance5 text, name_act5 int, FOREIGN KEY(name_act5) REFERENCES dialog_acts(dialog_act_id));")

	def processrow(self,arx):
		#print(arx)
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
		#dialog_act_5
		if len(arx[4])!=0:
			if self.dialogacts.get(arx[4],-1)==-1:
				self.dialogacts[arx[4]]=self.counter['da']
				da4id=self.counter['da']
				self.counter['da']+=1
			else:
				da5id=self.dialogacts[arx[4]]
		else:
			da5id=None
		#slot0 or starter
		if len(arx[5])!=0:
			if self.starters.get(arx[5],-1)==-1:
				self.starters[arx[5]]=self.counter['starter']
				starterid=self.counter['starter']
				self.counter['starter']+=1
			else:
				starterid=self.starters[arx[5]]
		else:
			starterid=None
		#slot1
		if da1id!=None:
			if self.slots1.get(arx[6],-1)==-1:
				self.slots1[arx[6]]=(self.counter['da1'],da1id)
				slot1id=self.counter['da1']
				self.counter['da1']+=1
			else:
				slot1id=self.slots1[arx[6]][0]
		else:
			slot1id=None
		#slot2
		if da2id!=None:
			if self.slots2.get(arx[7],-1)==-1:
				self.slots2[arx[7]]=(self.counter['da2'],da2id)
				slot2id=self.counter['da2']
				self.counter['da2']+=1
			else:
				slot2id=self.slots2[arx[7]][0]
		else:
			slot2id=None
		#slot3
		if da3id!=None:
			if self.slots3.get(arx[8],-1)==-1:
				self.slots3[arx[8]]=(self.counter['da3'],da3id)
				slot3id=self.counter['da3']
				self.counter['da3']+=1
			else:
				slot3id=self.slots3[arx[8]][0]
		else:
			slot3id=None
		#slot4
		if da4id!=None:
			if self.slots4.get(arx[9],-1)==-1:
				self.slots4[arx[9]]=(self.counter['da4'],da4id)
				slot4id=self.counter['da4']
				self.counter['da4']+=1
			else:
				slot4id=self.slots4[arx[9]][0]
		else:
			slot4id=None
		#slot4
		if da5id!=None:
			if self.slots5.get(arx[10],-1)==-1:
				self.slots5[arx[10]]=(self.counter['da5'],da4id)
				slot5id=self.counter['da5']
				self.counter['da5']+=1
			else:
				slot5id=self.slots5[arx[10]][0]
		else:
			slot5id=None			
		commandx = "INSERT INTO mappings VALUES ("
		commandx += str(self.counter['mapping_no'])			#adding mappingid
		commandx +=", "
		commandx += str(starterid)
		commandx +=", "
		if slot1id==None:
			commandx+='NULL'
		else:
			commandx += str(slot1id)
		commandx +=", "		
		if slot2id==None:
			commandx+='NULL'
		else:
			commandx += str(slot2id)
		commandx +=", "
		if slot3id==None:
			commandx+='NULL'
		else:
			commandx += str(slot3id)
		commandx +=", "
		if slot4id==None:
			commandx+='NULL'
		else:
			commandx += str(slot4id)
		commandx += ");"
		if slot5id==None:
			commandx+='NULL'
		else:
			commandx += str(slot5id)
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

		for key in self.slots1.keys():
			if key=='':
				continue;
			retrieved=self.slots1[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO slot1 VALUES ("
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
			self.slot1_commands.append(commandx)

		for key in self.slots2.keys():
			retrieved=self.slots2[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO slot2 VALUES ("
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
			self.slot2_commands.append(commandx)

		for key in self.slots3.keys():
			retrieved=self.slots3[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO slot3 VALUES ("
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
			self.slot3_commands.append(commandx)

		for key in self.slots4.keys():
			retrieved=self.slots4[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO slot4 VALUES ("
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
			self.slot4_commands.append(commandx)

		for key in self.slots5.keys():
			retrieved=self.slots5[key]
			did1=retrieved[0]
			dactid=retrieved[1]
			commandx = "INSERT INTO slot5 VALUES ("
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
			self.slot5_commands.append(commandx)

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

		ofile.write("\n\n#slot1 table commands\n")
		for comx in self.slot1_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#slot2 table commands\n")
		for comx in self.slot2_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#slot3 table commands\n")
		for comx in self.slot3_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#slot4 table commands\n")
		for comx in self.slot4_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#slot5 table commands\n")
		for comx in self.slot5_commands:
			ofile.write(comx+'\n')

		ofile.write("\n\n#Mapping commands\n")
		for comx in self.mapping_commands:
			ofile.write(comx+'\n')


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
csvp.mainprocess()
