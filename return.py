def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())
    return fs
f1, f2, f3 = count()
print(f1())
f2()
f3()

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


def createCounter():
    cnt = [0] # 将cnt设定为数组
    def counter():
        cnt[0] = cnt[0]+1 # 修改数组中的元素值
        return cnt[0] # 返回修改的元素值
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 