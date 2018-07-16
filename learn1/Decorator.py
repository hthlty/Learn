#装饰器

# 1.基本函数
def shi1():
    print('1')

#shi1()

# 2.扩展函数
def zs2(func):
    print('1')
    func()
    print('2')
def shi2():
    print('shi 2')

#shi2 = zs2(shi2)
#shi2()

# 3.实现函数的扩展功能
def zs3(func):
    def inner():
        print('1')
        func()
        print('2')
    return inner

def shi3():
    print('shi3')

# shi3 = zs3(shi3)
# shi3()

# 4语法糖
def zs4(func):
    def inner():
        print('1')
        func()
        print('2')
    return inner

@zs4
def shi4():
    print('shi4')
#shi4()

#5 带参数的语法糖 返回值
def zs5(func):
    def  inner(a,b):
        print('1')
        func(a,b)
        print('2')
    return inner
@zs5
def shi5(who,who2):
    print(who,'在和',who2,'打架')
#shi5('11','22')
# 5_2 返回值
def zs5_2(func):
    def inner(a,b):
        print('1')
        var = func(a,b)
        print('2')
        return var
    return inner
@zs5_2
def shi5_2(who,who2):
    print(who,'在和',who2,'打架')
    return 'fhz'
#shi5_2('22','11')
# resu = shi5_2('33','44')
# print(resu)

# 6收集参数的语法糖
def zs6(func):
    def inner(*a,**b): #inner接收收集参数 ，形参*a **b
        print('1')
        func(*a,**b) #形参*a **b
        print('2')
    return inner
@zs6
def shi6(*arg,**kwargs): #本体函数 具有收集参数
    print(arg,'在和',kwargs,'打架')
#shi6('小明',one='校长')

# 7带参数的装饰器
def plus(arg): #接收参数arg的实参 ’ss'
    def zs7(func): #本体方法形参func
        def inner():
            if arg=='ss':
                print('1')
                func()
                print('2')
            else:
                print('3')
                func()
                print('4')
        return inner
    return zs7
@plus('aa')
def shi7():
    print('shi7')
#shi7()

# 8装饰器的类参数
class Lei:
    def f1(): #类方法1
        print('f1')
    def f2(): #类方法2
        print('f2')
def plus8(cls):
    def zs8(func):
        def inner():
            cls.f1()
            func()
            cls.f2()
        return inner
    return zs8
@plus8(Lei)
def shi8():
    print('shi8')
#shi8()

# 9类装饰器
class Lei8:
    def __init__(self,arg):
        self.arg = arg #把arg标志传递给对象
    def __call__(self, func):
        self.func=func #func传递给对象
        return self.inner
    def inner(self):
        if self.arg=='shi':
            print('Hello 1')
            self.func()  #类的func方法
            print('Hello2')
        else:
            print('Hello 3')
            self.func()  #类的func方法
            print('Hello4')
@Lei8('shi') #shi 参数为arg 为了判断而特意加的
def shi9():
    print('shi9')
#shi9()

# 10类的装饰器
def zs10(cls): #形参为类cls
    def inner():
        print('Hello1')
        var = cls()
        print('Hello2')
        return var #返回一个对象，实现实例化的原功能
    return inner
@zs10
class Lei10:
    pass
# Lei10()
# resu = Lei10()
# print(resu)

# 11装饰器的嵌套
def zs11_1(cls):
    def inner():
        print('Hello 1')
        var = cls()
        print('Hello 2')
        return var
    return inner
def zs11_2(cls):
    def inner():
        print('Hello 3')
        var = cls()
        print('Hello 4')
        return var
    return inner
def zs11_3(cls):
    def inner():
        print('Hello 5')
        var = cls()
        print('Hello 6')
        return var
    return inner
@zs11_1#先执行一个到cls（）就向下执行
@zs11_2#执行一个到cls（）就向下执行
@zs11_3#执行一个到cls（）就向下执行 直到没有cls（），就一个一个完结
def shi11():
    print('shi--11')
shi11()
