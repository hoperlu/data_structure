from random import randrange
from time import time

def printer(func):
	def helper(*args):
		time_start=time()
		res=func(*args)
		if res==ans:
			print(func.__name__,time()-time_start)
		else:
			print(func.__name__,time()-time_start,'wrong answer!!!!!')
	return helper

@printer
def	insertion_sort(res):
	for index in range(len(res)): #unsorted index
		index2=index
		while index2>0 and res[index2-1]>res[index2]:
			res[index2-1],res[index2]=res[index2],res[index2-1]
			index2-=1
	return res

@printer
def	selection_sort(res):
	for index in range(len(res)-1):
		m=res[index] #current min
		mindex=index #index of current min
		for index2 in range(index+1,len(res)):
			if res[index2]<m:
				m=res[index2]
				mindex=index2
		if mindex!=index:
			res[index],res[mindex]=res[mindex],res[index]
	return res

@printer
def	bubble_sort(res):
	for index in range(len(res),1,-1):
		for index2 in range(index-1):
			if res[index2]>res[index2+1]:
				res[index2],res[index2+1]=res[index2+1],res[index2]
	return res

def merge_helper(a,b):
	ia=0
	ib=0
	res=[]
	while ia+ib<len(a)+len(b):
		if ia==len(a):
			res.append(b[ib])
			ib+=1
		elif ib==len(b):
			res.append(a[ia])
			ia+=1
		else:
			if a[ia]<b[ib]:
				res.append(a[ia])
				ia+=1
			else:
				res.append(b[ib])
				ib+=1
	return res

def	merge_sort(res):
	if len(res)<2:
		return res
	m=len(res)//2
	return merge_helper(merge_sort(res[:m]),merge_sort(res[m:]))

def	quick_sort(q):
	if len(q)==2:
		res=q.copy()
		if res[0]>res[1]:
			res[0],res[1]=res[1],res[0]
		return res
	if 2<len(q)<12:
		l=3
		temp=q[:l]
		for index in range(l-1):
			m=temp[index] #current min
			mindex=index #index of current min
			for index2 in range(index+1,l):
				if temp[index2]<m:
					m=temp[index2]
					mindex=index2
			if mindex!=index:
				temp[index],temp[mindex]=temp[mindex],temp[index]
		p=temp[1]
		s=[] #smaller part
		b=[] #bigger part
		count=0 #==p
		for index in range(len(q)):
			if q[index]<p:
				s.append(q[index])
			elif q[index]>p:
				b.append(q[index])
			else:
				count+=1
	else:
		l=11
		temp=q[:l]
		for index in range(l-1):
			m=temp[index] #current min
			mindex=index #index of current min
			for index2 in range(index+1,l):
				if temp[index2]<m:
					m=temp[index2]
					mindex=index2
			if mindex!=index:
				temp[index],temp[mindex]=temp[mindex],temp[index]
		p=temp[5]
		s=[] #smaller part
		b=[] #bigger part
		count=0 #==p
		for index in range(len(q)):
			if q[index]<p:
				s.append(q[index])
			elif q[index]>p:
				b.append(q[index])
			else:
				count+=1
	res=[0 for index in range(len(q))]
	for index in range(len(s),len(s)+count):
		res[index]=p
	if len(s)>1:
		res[:len(s)]=quick_sort(s)
	elif len(s)==1:
		res[0]=s[0]
	if len(b)>1:
		res[len(q)-len(b):]=quick_sort(b)
	elif len(b)==1:
		res[-1]=b[0]
	return res

@printer
def	heap_sort(q):
	res=[]
	for index in range(len(q)):
		res.append(q[index])
		if len(res)>1:
			index2=index
			index3=(index2-1)//2
			while index2>0 and res[index2]>res[index3]:
				res[index3],res[index2]=res[index2],res[index3]
				index2=index3
				index3=(index2-1)//2
	count=len(res)-1
	while count>0:
		res[0],res[count]=res[count],res[0]
		index=0
		while index*2+2<count and res[index]<max(res[index*2+1],res[index*2+2]):
			if res[index*2+1]>res[index*2+2]:
				res[index],res[index*2+1]=res[index*2+1],res[index]
				index=index*2+1
			else:
				res[index*2+2],res[index]=res[index],res[index*2+2]
				index=index*2+2
		count-=1
		if index*2+1==count:
			if res[index*2+1]>res[index]:
				res[index*2+1],res[index]=res[index],res[index*2+1]
	return res

q=[randrange(-100000,100000) for index in range(10000)] #len(q)>1
print(q[:10])
time_start=time()
ans=sorted(q)
print('ans',ans[:10],time()-time_start)

insertion_sort(q.copy())
selection_sort(q.copy())
bubble_sort(q.copy())
printer(merge_sort)(q.copy())
printer(quick_sort)(q.copy())
heap_sort(q.copy())
