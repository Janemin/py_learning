# line comment

"""
block comment 1
"""

'''
block comment 2
'''

###################################################################

# hello world
print("hello world!")

###################################################################

# 缩进
if True:
    print("True")
else:
    print("False")

''' error indentation case
if True:
    print("True")
  print("False")   # IndentationError: unindent does not match any outer indentation level
else:
    print("False")
'''

###################################################################

# Use '\' to concat Multi-line statement
total = 1 + \
        2 + \
        3
# It's unnecessary to use '\' to concat Multi-line statement in '[]', '{}' or '()'
arr = ['item_one', 'item_two', 'item_three',
      'item_four', 'item_five']

###################################################################

# Use ';' to separate multiple statements in the same line
import sys; x = 'GOT'; sys.stdout.write(x + '\n')

###################################################################

'''
if expression :       # clause 1
   suite                # code group 1 start 
   suite                # code group 1 end    
elif expression :     # clause 2
   suite                # code group 2  
else :                # clause 3
   suite                # code group 3  
'''

###################################################################

# default print in new line
print("GOT Awesome!!!")
# No line feed output
print("GOT", end='')
print(" Awesome!!!")

###################################################################

# import 与 from...import
# 用 import 或者 from...import 来导入相应的模块。
#   - 将整个模块(somemodule)导入，格式为： import somemodule
#   - 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#   - 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#   - 将某个模块中的全部函数导入，格式为： from somemodule import *

###################################################################

# 赋值
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "GOT"     # 字符串

a = b = c = 1
d, e, f = 1, 2, "GOT"

###################################################################

# del var1, var2    (delete instance reference)
del a, b
