
# 使用 Python 源文件
# import module1[, module2[,... moduleN]
import sys

# 并没有把直接定义在fibo中的函数名称写入到当前符号表里，只是把模块fibo的名字写到了那里。
# 可以使用模块名称来访问函数
import fibo

fibo.fib(1000)

print(sys.path)

# 赋给一个本地的名称
path = sys.path



# 从模块中导入一个指定的部分到当前命名空间
# from modname import name1[, name2[, ... nameN]]
# from modname import *
from fibo import fib, fib2
fib(500)

import using_name           # 我来自另一模块

# dir() 函数 内置的函数, dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回

print(dir(fibo))    # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']

dir() # 没有给定参数, 得到一个当前模块中定义的属性列表
