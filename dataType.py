
# 标准数据类型
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
# string、list 和 tuple 都属于 sequence（序列）。
###################################################################

# number type
#   1. int     : 1     ('long type' only in python2)
#   2. bool    : True
#   3. float   : 1.23 , 3E-2
#   4. complex : 1 + 2j , 1.1 + 3.2j

number_int, number_float, number_bool, number_complex = 20, 5.5, True, 4+3j
# type()
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
print(type(number_int), type(number_float), type(number_bool), type(number_complex))
# isinstance()
print(isinstance(number_int, int))  # True

# PS: - type() 不会认为子类是一种父类类型。
#     - isinstance() 会认为子类是一种父类类型。

###################################################################

print(4 + 5)     # 9
print(4.3 - 2)   # 2.3
print(3 * 7)     # 21
print(2 / 4)     # 0.5
print(17 % 3)    # 2
print(2 ** 5)    # 32

###################################################################

# string type (has't char type)
word1 = '字符串'
word2 = "字符串"
# multi-line string
paragraph1 = '''这是一个段落，
可以由多行组成'''
paragraph2 = """这是一个段落，
可以由多行组成"""

# escapes '\'
new_line = "this is a line with \n"
# unescaped r (r : raw)
one_line = r"this is a line with \n"

# index
#   - left -> right from 0
#   - right -> left from -1
# subString: 变量[头下标:尾下标:步长]
# string case
str = 'GameOfThrones'

print(str)                # GameOfThrones
print(str[0:-1])          # GameOfThrone
print(str[0])             # G
print(str[2:5])           # meO
print(str[0:-1:2])        # GmOTrn
print(str[2:])            # meOfThrones
print(str * 2)            # GameOfThronesGameOfThrones
print(str + ' wow')       # GameOfThrones wow

print('hello\nJon Snow')  # hello
                          # Jon Snow
print(r'hello\nJon Snow') # hello\nJon Snow

###################################################################

# list type : use '[]' to define
# The list can contains number, string, list type elements.
# One list can contains different types elements
list = [786, 'Sansa Stark', 70.2]
tinylist = [123, 'Robb Stark']

print(list)             # 输出完整列表                   | [786, 'Sansa Stark', 70.2]
print(list[0])          # 输出列表第一个元素              | 786
print(list[0:2])        # 从第一个开始输出到第三个元素     | [786, 'Sansa Stark']
print(list[2:])         # 输出从第三个元素开始的所有元素   | [70.2]
print(list * 2)         # 输出两次列表                   | [786, 'Sansa Stark', 70.2, 786, 'Sansa Stark', 70.2]
print(list + tinylist)  # 连接列表                      | [786, 'Sansa Stark', 70.2, 123, 'Robb Stark']

int_list = [1, 2, 3, 4, 5, 6]
int_list[0] = 9   # [9, 2, 3, 4, 5, 6]
int_list[2:5] = [13, 14, 15]  # [9, 2, 13, 14, 15, 6]
int_list[2:5] = []  # [9, 2, 6]
###################################################################

# Tuple(元组) : use '()' to define
# The elements in the tuple can't be changed, but can be modified

tuple  = (786, 'Sansa Stark', 70.2, 'Ned')
tinytuple = (123, 'Robb Stark')

print(tuple)              # 输出完整元组
print(tuple[0])           # 输出元组的第一个元素
print(tuple[1:3])         # 输出从第二个元素开始到第三个元素
print(tuple[2:])          # 输出从第三个元素开始的所有元素
print(tinytuple * 2)      # 输出两次元组
print(tuple + tinytuple)  # 连接元组

tup1 = ()     # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

###################################################################

# Set（集合） : use '{}' or set() to define

roles = {'Jon Snow', 'Sansa', 'Ned', 'Arya'}
if 'Ned' in roles :
    print('Ned')

a = set('abcde')
b = set('defg')

print(a)      # {'d', 'a', 'c', 'b', 'e'}
print(a - b)  # a 和 b 的差集             {'b', 'a', 'c'}
print(a | b)  # a 和 b 的并集             {'d', 'a', 'f', 'c', 'b', 'g', 'e'}
print(a & b)  # a 和 b 的交集             {'d', 'e'}
print(a ^ b)  # a 和 b 中不同时存在的元素   {'a', 'f', 'b', 'c', 'g'}

###################################################################

# Dictionary（字典） : use '{key:value}'  to define
dict = {}
dict['name'] = 'Jon Snow'
dict[18] = 'Age 18'

tinydict = {'name': 'Jon Snow', 'age': 18, 'profile': 'Winter is coming'}


print(dict)               # 输出完整的字典          {'name': 'Jon Snow', 18: 'Age 18'}
print(dict['name'])       # 输出键为 'one' 的值     Jon Snow
print(dict[18])           # 输出键为 18 的值        Age 18
# print(dict[2])          # 输出键为 2 的值 error
print(tinydict)           # 输出完整的字典          {'name': 'Jon Snow', 'age': 18, 'profile': 'Winter is coming'}
print(tinydict.keys())    # 输出所有键              dict_keys(['name', 'age', 'profile'])
print(tinydict.values())  # 输出所有值              dict_values(['Jon Snow', 18, 'Winter is coming'])
