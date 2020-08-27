
# -*- coding: utf-8 -*-
#请用sorted()对上述列表分别按名字排序：
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
#相当于针对key函数计算出来的值进行排序规则，但是排序的最终对象还是原始list或tuple
#每次key函数都处理一个元素
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#print(L[1])
def by_name(t):
    #print(t[1])
    #print(len(t))
    #i=0
    #S=[]

    #if i<len(t):
    #    S[i]=t[i][1]
    #    i=i+1 
    #    print(S)
    return t[0]
#print(S)
by_name(L)
L2 = sorted(L, key=by_name)
print(L2)
