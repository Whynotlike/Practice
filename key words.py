#def message(name,age,*,city='fujian',juice):
#    print(name,age,city,juice)

#def message(name,age,**kw):
#    if 'city' in kw:
#        pass
#    if 'juice' in kw:
#        pass
#    print(name,age,kw)
#调用者在限制条件下仍然可以传入

#def product(x,*z):
#    sum = x
#    for n in z:
#        sum = sum * n
#    return sum
#计算多个数的乘积


#def calc(numbers):
#    sum = 0
#    for n in numbers:
#        sum = sum + n * n
#    return sum
#求a*a+b*b...
#优化后
#def calc(*number):
#    sum = 0
#    for n in number:
#        sum = sum + n * n
#    return sum
#增加了可变参数...
