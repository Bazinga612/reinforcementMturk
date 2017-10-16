import csv
'''
with open('tv_movie_combined.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	k=0
	for row in spamreader:
		print(k,len(row),row)
'''

def combinefunc(arr):			#function to eliminate deformities in the CSV file
	print("The input array is",arr)
	stat,addons=0,0
	for j in range(len(arr)-addons):
		#print("Stat is",stat,arr[j-addons])
		if stat==0:
			#arrord=[ord(p) for p in arr[j]]
			if ord(arr[j-addons][0])==34:
				stat=1
				if ord(arr[j-addons][-1])!=34:
					tempstr=arr[j-addons][1:]
					#print("case1")
				else:
					arr[j-addons]=arr[j-addons][1:-1]
					#print("case2")
					continue;
			else:
				continue;
		elif stat==1:
			tempstr+=', '
			if ord(arr[j-addons][-1])!=34:
				tempstr+=arr[j]
				arr[j-1-addons]=tempstr
				arr.pop(j-addons)
				#print("case3")
			else:
				tempstr+=arr[j-addons][:-1]
				arr[j-1-addons]=tempstr
				arr.pop(j-addons)
				stat=0
				#print("case4")
			addons+=1
		#print("tempstr=",tempstr)
		#print("arr=",arr)
	print("The output array is",arr)


testcases=[['"hey','this is','insane"','"i know right"'],
['"hey','this is insane"','"i know right"']
]
for el in testcases:
	combinefunc(el)