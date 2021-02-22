#Critical Path Analysis, see PDF 6-73

#AOE(Activity-on-Edge) Network is shown as following
#key is vertex, value is the list which contains (vertex pointed by key, time) pairs
aoe={0:[(1,3),(2,2)],1:[(4,3),(3,0)],2:[(3,0),(6,1)],3:[(5,2)],4:[(7,0)],5:[(7,0),(8,0)],6:[(8,0),(11,4)],7:[(9,3)],8:[(10,2)],9:[(12,0)],10:[(12,0)],11:[(12,0)],12:[(13,1)],13:[]}

#step 1: find in-degree of every vertex
in_degree=[0 for x in range(len(aoe))]
for key in aoe:
	for pair in aoe[key]:
		in_degree[pair[0]]+=1

#step 2: find Earliest completion times with the help of in-degree (the following code assume there is only one vertex with zero in-degree in aoe originally)
queue=[index for index in range(len(in_degree)) if in_degree[index]==0]#儲存in-degree==0且還未處理過的點
ect=[0 for index in range(len(aoe))] #Earliest completion times
while queue:
	key=queue.pop()
	for pair in aoe[key]:
		in_degree[pair[0]]-=1
		if in_degree[pair[0]]==0:
			queue.append(pair[0])
		ect[pair[0]]=max(ect[pair[0]],ect[key]+pair[1])

#step 3: find reverse in-degree
reverse_in_degree=[len(aoe[index]) for index in range(len(aoe))]

#step 4: find Latest completion times with the help of reverse in-degree
queue=[index for index in range(len(reverse_in_degree)) if reverse_in_degree[index]==0]#儲存reverse in-degree==0且還未處理過的點
lct=[max(ect) for index in range(len(aoe))]
while queue:
	key=queue.pop()
	for k in aoe:
		for pair in aoe[k]:
			if pair[0]==key:
				reverse_in_degree[k]-=1
				if reverse_in_degree[k]==0:
					queue.append(k)
				lct[k]=min(lct[key]-pair[1],lct[k])

#step 5: give critical path with ect and lct
ans=[]
if len(ect)!=len(lct):
	print('waarning')
else:
	for index in range(len(ect)):
		if ect[index]==lct[index]:
			ans.append(index)
	print(ans)