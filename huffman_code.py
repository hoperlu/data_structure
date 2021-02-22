#編碼文字檔, 呈現huffman tree, encode, decode
class TreeNode():
	def __init__(self,val,right=None,left=None):
		self.val=val
		self.right=right
		self.left=left

class Heap():
	def __init__(self):
		self.val=[]
	def pop(self):#pop第一個node後，把最後一個node拉到index=0的地方, 然後跟其最小的child比
		if len(self.val)<1:
			print('heap is empty')
		elif len(self.val)<3:
			return self.val.pop(0)
		else:
			res=self.val[0]
			self.val[0]=self.val.pop(-1)
			i=0
			while len(self.val)>i*2+2:#當i有兩個child
				if self.val[i*2+1].val<self.val[i*2+2].val:
					j=i*2+1
				else:
					j=i*2+2
				if self.val[j].val<self.val[i].val:
					(self.val[i],self.val[j])=(self.val[j],self.val[i])
					i=j
				else:
					break
			if len(self.val)==i*2+2:#當i只有一個child
				if self.val[i*2+1].val<self.val[i].val:
					(self.val[i],self.val[i*2+1])=(self.val[i*2+1],self.val[i])
			return res
	def push(self,node):#push的node放heap最後面，然後跟其parent比
		self.val.append(node)
		i=len(self.val)-1
		j=(i-1)//2
		while self.val[i].val<self.val[j].val and i!=0:
			(self.val[i],self.val[j])=(self.val[j],self.val[i])
			i=j
			j=(i-1)//2

def build_tree(input_):
	heap=Heap()
	for term in input_:
		heap.push(TreeNode(term))
	while len(heap.val)>=2:
		temp=heap.pop()
		temp2=heap.pop()
		heap.push(TreeNode(temp.val+temp2.val,temp,temp2))
	return heap.pop()

def plot_tree(tree):
	ans=[]
	queue=[tree]
	while queue:
		if queue[0]=='null':
			ans.append('null')
		else:
			ans.append(queue[0].val)
			if queue[0].left:
				queue.append(queue[0].left)
			else:
				queue.append('null')
			if queue[0].right:
				queue.append(queue[0].right)
			else:
				queue.append('null')
		queue.pop(0)
	print('tree:',ans)

def encoder(input_,count,tree):
	ref={}
	for term in count:
		if count[term] in ref:
			ref[count[term]].append(term)
		else:
			ref[count[term]]=[term]
	huffman_code={}
	def helper(tree,s):
		if tree.right==None and tree.left==None:
			huffman_code[ref[tree.val].pop(0)]=s
		if tree.left!=None:
			helper(tree.left,s+'0')
		if tree.right!=None:
			helper(tree.right,s+'1')
	helper(tree,'')
	res=''
	for term in input_:
		res+=huffman_code[term]
	return (res,huffman_code)
def decoder(encoded,huffman_code):
	ref={}
	for term in huffman_code:
		ref[huffman_code[term]]=term
	ans=''
	temp=''
	for term in encoded:
		temp+=term
		if temp in ref:
			ans+=ref[temp]
			temp=''
	return ans

input_='Eerie eyes seen near lake.'
#input_=(1,8,2,1,4,1,2,2,2,1,1,1)
#input_=(5,3,13,7,9,2)
if type(input_)==str:
	count={}
	for term in input_:
		if term in count:
			count[term]+=1
		else:
			count[term]=1
	tree=build_tree(count.values())
	plot_tree(tree)
	(encoded,huffman_code)=encoder(input_,count,tree)
	print(huffman_code)
	print(len(encoded))
	print(encoded)
	decoded=decoder(encoded,huffman_code)
	print(decoded)
else:
	plot_tree(build_tree(input_))