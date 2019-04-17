emptySet = set()

a = set('abcde')
b = set('defg')

print(a)      # {'d', 'a', 'c', 'b', 'e'}
print(a - b)  # a 和 b 的差集             {'b', 'a', 'c'}
print(a | b)  # a 和 b 的并集             {'d', 'a', 'f', 'c', 'b', 'g', 'e'}
print(a & b)  # a 和 b 的交集             {'d', 'e'}
print(a ^ b)  # a 和 b 中不同时存在的元素   {'a', 'f', 'b', 'c', 'g'}

b.add('h')

print(a.isdisjoint(b))   # False  判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False

# 参数可以是列表，元组，字典等, 参数可以有多个
b.update({'i', 'j'})
b.update([1, 4], [5, 6])
print(b)      # {'i', 1, 4, 5, 6, 'j', 'd', 'g', 'h', 'f', 'e'}

b.remove('i')   # 移除元素, 不存在会发生错误
b.discard('i')  # 移除元素, 不存在不会发生错误
b.pop()         # 随机删除集合中的一个元素（删除集合的第一个元素（排序后的集合的第一个元素））

b.clear()       # 清空集合

b = a.copy()

b.discard('a')

c = a.difference(b)
print(c)        # {'a'}          返回多个集合的差集

a.difference_update(c)     # 移除集合中的元素，该元素在指定的集合也存在。
print(a)        # {'d', 'c', 'e', 'b'}

print(a.intersection(c))   # set()   返回集合的交集

c.intersection_update(a)   # set()   删除集合中的元素，该元素在指定的集合中不存在
print(c)        # set()

c = {'1', '2'}

print(c.issubset({'1', '2', '3'}))  # True  指定集合是否为该方法参数集合的子集
print(c.issuperset({'1'}))          # True  该方法的参数集合是否为指定集合的子集

c.remove('1')                       # 移除指定元素
c.pop()                             # 随机移除元素

a = set('abcde')
b = set('defg')

print(a.union(b))                   # {'b', 'f', 'e', 'g', 'd', 'c', 'a'}  返回两个集合的并集
print(a.symmetric_difference(b))    # {'a', 'c', 'b', 'g', 'f'}   返回两个集合中不重复的元素集合

a.symmetric_difference_update(b)    # 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
print(a)                            # {'b', 'f', 'g', 'a', 'c'}
