# SIMPLE DEMO
class MyClass:
    """一个简单的类实例"""
    i = 0

    # 构造方法
    def __init__(self, i):
        print('execute __init__')
        self.i = i

    def prt(self):
        print(self)
        print(self.__class__)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()

# 实例化类
x = MyClass(100)

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print(x.prt())


# 类定义
class Human:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = Human('runoob', 10, 30)
p.speak()


class Student(Human):
    grade = ''

    def __init__(self,n,a,w,g):
        #调用父类的构函
        Human.__init__(self,n,a,w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = Student('ken', 10, 60, 3)
s.speak()          # ken 说: 我 10 岁了，我在读 3 年级


#另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))


# 多重继承
# ，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法
class StudentSpeaker(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


ss = StudentSpeaker("Tim", 25, 80, 4, "Python")
ss.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法   我叫 Tim，我是一个演说家，我演讲的主题是 Python


# overwrite
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法


# 类的专有方法
#　__init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
