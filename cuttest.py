
#去除首位空格字符 
#注意不能简单得使用[0][-1]取首尾，如果空字符串会溢出
def trim(s):
    while s[:1]==' ':
        s = s[1:]
    while s[-1:]==' ':
        s = s[:-1]
    return s
str=''
print(str[:1])
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

#L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = [s.lower() for s in L1 if isinstance(s, str)]
#L2 = [s.lower() if isinstance(s, str) else 'YES' for s in L1]


def triangles():
    L= [1]
    while True:
        yield L
        L= [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]


a=range(1)
print(a)

J = [1]
print(J[0])
J = [1]+[J[i] for i in (range(0))]+[1]
print(J)
