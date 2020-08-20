print('##########################################################')
#参数顺序 位置参数，默认参数，可变参数，命名关键参数，关键参数
def pp(name,sex='男/女',*arg,state,**other):
    #for x in sex:
        print('first arg:',name)   #位置参数 必须存在
        print('second arg:',sex)   #默认参数  可有可无
        print('third arg:',arg)    #可变参数 可有可无 tuple
        print('forth arg:',state)   #命名关键参数 必须指定参数值dict
        print('other arg:',other)   #关键字参数 可有可无 dict
pp('Austin','男','where',state='califorlia',answer='no')
print('##########################################################')

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x,*y):   
    #res = 1
    #if x is None:
    #    return None
    #if y is None:  #当参数y tuple没有元素即为()时，不会进入for循环
    #    return x
    
    for i in y:
        x = x * i  #或者写为x *= i
    return x

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

 #   print(list(range(100)))



