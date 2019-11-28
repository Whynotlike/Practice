#-*- coding: utf-8 -*-


#def move(n,a,b,c):
#    if n == 1:
#        print(a,'-->',c)
#    else:
#        move(n-1,a,c,b)#借助c柱降n-1个圆盘从A柱移动到B柱
#        print(a,'-->',c)
#        move(n-1,b,a,c)
#汉诺塔

#list(range(1,100,2))
#打印100以内的奇数

#def ser(s):
#	while s[:1] == ' ':
#		s = s[1:]
#	while s[-1:] == ' ':
#		s = s[:-1]
#	return s
#用切片的方法删除头尾空格

#def findminandmax(L):
#	if L == []:
#		return (None,None)
#	else:
#		min=max=L[0]
#		for i in L:
#			if i <= min:
#				min = i
#			if i >= max:
#				max = i
#		return (min,max)
#迭代：利用for...in求一个list中minAndmax输出tuple

#L1 = ['HELLO','WORLD',18,'APPLE',None]
#[L2.lower() for L2 in L1 if isinstance(L2,str)==True]
#由于非字符串类型没有lower()方法，所以列表生成式会报错
#修改列表生成式，通过添加if语句保证列表生成式能正确地执行

def Fib(max):
	n,a,b = 0,0,1
	while n <= max:
		#print(b)
#把fib函数变成generator，只需要把print(b)改为yield b
		yield b
		a,b = b,a+b
		n = n + 1
	return 'done'
#用函数打印斐波拉契数列

def ser():
	L = [1]	  #定义并赋值
	yield L
	L = [1,1]
	yield L
	while True:
		newL = [1] #每次初始化计算机
		for i in range(1,len(L)): #确定长度
			newL.append(L[i-1] + L[i])  #增加
		newL.append(1) #末尾加1
		L = newL #赋值
		yield L
#杨辉三角
