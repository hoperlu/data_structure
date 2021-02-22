from random import randrange
from time import time

def printer(func):
	def helper(*args):
		time_start=time()
		res=func(*args)
		print(func.__name__,res==ans,time()-time_start)
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

@printer
def	quick_sort(q):
	if len(q)==2:
		res=q.copy()
		if res[0]>res[1]:
			res[0],res[1]=res[1],res[0]
		return res
	#if 2<len(q)<12:

	#res=[0 for index in range(len(q))]

	return res

@printer
def	heap_sort():
	return res

q=[randrange(-100000,100000) for index in range(10000)] #len(q)>1
print(q[:10])
time_start=time()
ans=sorted(q)
print('ans',ans[:10],time()-time_start)

insertion_sort(q.copy())
selection_sort(q.copy())
bubble_sort(q.copy())
time_start=time()
res=merge_sort(q.copy())
print('merge_sort',res==ans,time()-time_start)
#quick_sort(q.copy())
#heap_sort(q.copy())
