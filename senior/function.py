# 计算面积函数
def area(width, height):
    return width * height

print(area(10, 10))

"""
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""

# arguments


def printme(str):
   "打印任何传入的字符串"
   print(str)
   return

# 必需参数
printme("test")

# 关键字参数(关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值)
printme(str="test")

# 默认参数(如果没有传递参数，则会使用默认参数)


def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")

# 不定长参数


def print_vars(arg1, *var_args_tuple):
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   print(var_args_tuple)


print_vars(70, 60, 50)
# 70
# (60, 50)


def print_dict( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)


print_dict(1, a=2, b=3)
# 1
# {'a': 2, 'b': 3}


# 参数中星号 * 可以单独出现


def f(a,b,*,c):
    return a + b + c

# f(1,2,3)                 error
# 单独出现星号 * 后的参数必须用关键字传入
f(1,2,c=3)


# 匿名函数 （用 lambda 来创建匿名函数）
"""
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

lambda [arg1 [,arg2,.....argn]]:expression
"""

sum = lambda arg1, arg2: arg1 + arg2
print ("相加后的值为 : ", sum(10, 20))

'''
变量作用域
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
'''

g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域


# 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内
import builtins

# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
# 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
# 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
# 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
# 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
# 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
# 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
# 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning',
# 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
# 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning',
# 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__',
# '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable',
# 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
# 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help',
# 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max',
# 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
# 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
print(dir(builtins))


# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这些语句内定义的变量，外部也可以访问

if True:
    msg = 'Python'

print(msg)   # Python


def var_Scope():
    test_var = 'define in function'

# print(test_var)             error


"""
全局变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
"""

total = 0  # 这是一个全局变量


# 可写函数说明
def sum_number(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)      # 函数内是局部变量 :  30
    return total


# 调用sum函数
sum_number(10, 20)
print("函数外是全局变量 : ", total)          # 函数外是全局变量 :  0


# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字

num = 1

def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)            # 1
    num = 123
    print(num)            # 123

fun1()
print(num)                # 123

#　如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了


def outer_func():
    num = 10

    def inner_func():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)     # 100

    inner_func()
    print(num)         # 100


outer_func()


# error  局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改
# UnboundLocalError: local variable 'a' referenced before assignment
# a = 10
# def test():
#     a = a + 1
#     print(a)
# test()

# 修改 a 为全局变量，通过函数参数传递，可以正常执行
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)
