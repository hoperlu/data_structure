a='0 1 0 0 0 1 1 0 0 0 1 1 1 1 1'
b='1 0 0 0 1 1 0 1 1 1 0 0 1 1 1'
c='0 1 1 0 0 0 0 1 1 1 1 0 0 1 1'
d='1 1 0 1 1 1 1 0 1 1 0 1 1 0 0'
e='1 1 0 1 0 0 1 0 1 1 1 1 1 1 1'
f='0 0 1 1 0 1 1 1 0 1 0 0 1 0 1'
g='0 1 1 1 1 0 0 1 1 1 1 1 1 1 1'
h='0 0 1 1 0 1 1 0 1 1 1 1 1 0 1'
i='1 1 0 0 0 1 1 0 1 1 0 0 0 0 0'
j='0 0 1 1 1 1 1 0 0 0 1 1 1 1 0'
k='0 1 0 0 1 1 1 1 1 0 1 1 1 1 0'
maze=[]
for term in (a,b,c,d,e,f,g,h,i,j,k):
	temp=term.split(' ')
	temp.insert(0,'1')
	temp.append('1')
	maze.append(temp)
maze.insert(0,['1' for index in range(len(maze[0]))])
maze.append(['1' for index in range(len(maze[0]))])

for term in maze:
	print(term)
#maze completed

directions=((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
p=[1,1]#目前位置
queue=[]#記錄走的方向 directions[0~7]
walked=[[1,1]]#走過的路
d=0#index of directions
while p!=[11,15]:
	while d<8:
		p[0]+=directions[d][0]
		p[1]+=directions[d][1]
		if maze[p[0]][p[1]]=='0' and p not in walked:
			walked.append(p.copy())
			queue.append(d)
			d=0
			break
		else:
			p[0]-=directions[d][0]
			p[1]-=directions[d][1]
			d+=1
	else: #目前的p沒有能走的路
		if queue:
			d=queue.pop(-1)
			p[0]-=directions[d][0]
			p[1]-=directions[d][1]
			d+=1
		else:
			print('no path from start to end')
			break
print([directions[x] for x in queue])
print(queue)