pairs=((0,4), (3,1), (6,10), (8,9), (7,4), (6,8), (3,5), (2,11), (11,0))
#ans={0,2,4,7,11}; {1,3,5}; {6,8,9,10}
#implement with linked list
ref=[[False] for index in range(12)]
for term in pairs:
	ref[term[0]].append(term[1])
	ref[term[1]].append(term[0])
ans=[]
for index in range(len(ref)):
	if not ref[index][0]:
		ref[index][0]=True
		ans.append([index])
		queue=ref[index][1:]
		while queue:
			if ref[queue[0]][0]:
				queue.pop(0)
			else:
				ref[queue[0]][0]=True
				queue.extend(ref[queue[0]][1:])
				ans[-1].append(queue[0])
print(ans)