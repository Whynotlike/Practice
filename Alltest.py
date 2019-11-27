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

def findminandmax(L):
	if L == []:
		return (None,None)
	else:
		min=max=L[0]
		for i in L:
			if i <= min:
				min = i
			if i >= max:
				max = i
		return (min,max)
#迭代：利用for...in求一个list中minAndmax输出tuple

L1 = ['HELLO','WORLD',18,'APPLE',None]
[L2.lower() for L2 in L1 if isinstance(L2,str)==True]
#由于非字符串类型没有lower()方法，所以列表生成式会报错
#修改列表生成式，通过添加if语句保证列表生成式能正确地执行