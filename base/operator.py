# logic operator
# True : 1 , False : 0
print(1 and 2)  # 2
print(1 and 0)  # 0
print(1 or 2)  # 1
print(1 or 0)  # 1
print(not 2)  # False
print(not 0)  # True

if (10 and 20):
    print("t")

###############################################

# member operator
# in / not in    work on  string, list, tuple
# string、list 和 tuple 都属于 sequence（序列）。
list = [1, 2, 'a', 'b']
str = 'PYTHON'
tup = (1, 2, 'a', 'b')

print(2 in list)    # True
print('P' in str)   # True
print(1 in tup)     # True

###############################################

# identity operator
# is / is not   compare the reference refer to the same instance, like id(a) == id(b)
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
a = 20
b = 20
print(a is b)             # True
print(id(a) == id(b))     # True

b = 30
print(a is b)             # False
print(id(a) == id(b))     # False
