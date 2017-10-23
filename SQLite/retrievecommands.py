import sqlite3
conn = sqlite3.connect('rlmturk.db')
c = conn.cursor()

'''
for row in c.execute('SELECT * FROM slot1 ORDER BY slot1_id'):
    print(row)
'''
print("slot1 is Answer.TalkMore and slot2 is Answer.elaboration")
commandx1 = "SELECT mapping_id, starter_id, slot1.utterance1, slot2.utterance2 from mappings join slot1 ON mappings.slot1_id = slot1.slot1_id join slot2 ON mappings.slot2_id =slot2.slot2_id and slot1.name_act1=1 and slot2.name_act2=5"

print("Utterances which have all 4 slots filled!")
commandx2 = "SELECT mapping_id, starter_id, slot1.utterance1 from mappings join slot1 ON mappings.slot1_id = slot1.slot1_id join slot2 ON mappings.slot2_id = slot2.slot2_id join slot3 ON mappings.slot3_id = slot3.slot3_id join slot4 ON mappings.slot4_id = slot4.slot4_id"

print("First utterances (slot1) of conversations which start with I STILL think ""Monty Python and the Holy Grail"" is funny.")
queryyy="I sometimes get confused by ""How to Get Away With Murder."""
commandx3 = "SELECT mapping_id, starter_id from mappings join starter ON starter.starter_id = mapping.starter_id AND starter.utterance = "Sometimes Star Trek is less than stellar,  but I still like it overall.

def processcommand(commandx):
	count=0
	for row in c.execute(commandx):
		print(row)
		count+=1
	print(count,"rows retrieved!")

processcommand(commandx3)