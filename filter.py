#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
n=18981
print(n)
print(str(n))
print(list(str(n)))
print(len(str(n))//2)

def is_palindrome(n):
    L = str(n)  #将int类型转换成str才能取数列中的单个值
    #L = list(s)
    flag = True
    #def huishu(L):
    i = 0
    while i<((len(L)//2)+1):   #//整除
    #while(i<len(L)):
        if(L[i]!=L[-(i+1)]):
            flag=False
            break
        i = i+1
    return flag

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

#def is_palindrome(n):
#   return  int(str(n)[::-1]) == n  #str(n)将n转换为string才能进行reverse操作，翻转之后再转换成int格式与原来的数比较是否相同
#   n[::-1]翻转数列