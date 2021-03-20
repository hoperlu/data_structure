#一次只能走一或兩格樓梯 走完42格樓梯有幾種走法
def helper(n):
	if n==1:
		return 1
	if n==2:
		return 2
	return helper(n-1)+helper(n-2)
print(helper(42))