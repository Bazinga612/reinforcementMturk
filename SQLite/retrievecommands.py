import sqlite3
conn = sqlite3.connect('rlmturk.db')
c = conn.cursor()

'''
for row in c.execute('SELECT * FROM slot1 ORDER BY slot1_id'):
    print(row)
'''
print("slot1 is Answer.joking_sarcastic and slot2 is Answer.elaboration")

query0 = "SELECT * from mappings"

query1 = "SELECT * from starter where starter.starter_id=5"

query2 = "SELECT utterance1 from mappings INNER JOIN slot1 ON mappings.slot1_id = slot1.slot1_id and slot1.name_act1=4"

query3 = "SELECT mapping_id, starter_id, slot1.utterance1, slot2.utterance2 from mappings join slot1 ON mappings.slot1_id = slot1.slot1_id join slot2 ON mappings.slot2_id =slot2.slot2_id and slot1.name_act1=1 and slot2.name_act2=5"

# talkmore -> elaboration -> sarcastic
query4 = "SELECT mapping_id, starter_id, slot1.utterance1, slot2.utterance2 from mappings join slot1 ON mappings.slot1_id = slot1.slot1_id join slot2 ON mappings.slot2_id =slot2.slot2_id join slot3 ON mappings.slot3_id = slot3.slot3_id and slot1.name_act1=1 and slot2.name_act2=5 and slot3.name_act3=4"

#print("Utterances which have all 4 slots filled!")
query3 = "SELECT mapping_id, starter_id, utterance1, utterance2 from mappings join slot1 ON mappings.slot1_id = slot1.slot1_id join slot2 ON mappings.slot2_id = slot2.slot2_id join slot3 ON mappings.slot3_id = slot3.slot3_id join slot4 ON mappings.slot4_id = slot4.slot4_id"

#print("First utterances (slot1) of conversations which start with I STILL think ""Monty Python and the Holy Grail"" is funny.")

def processcommand(commandx):
	count=0
	for row in c.execute(commandx):
		print(row)
		count+=1
	print(count,"rows retrieved!")

processcommand(query4)