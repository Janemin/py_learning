# 元组与列表类似，不同之处在于元组的元素不能修改

# empty tuple
emptyTuple = ()

# 只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
singleElementTuple = (50,)

# 元组连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)                         # (12, 34.56, 'abc', 'xyz')

# delete tuple
del tup3
