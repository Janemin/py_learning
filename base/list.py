list = ['Ned', 'Snow', 1997, 2000]

del list[2]               # ['Ned', 'Snow', 2000]      |  删除列表的元素
print(list)

print(list.__len__())     # 3
print(len(list))          # 3

print(['1', '2'] + list)  # ['1', '2', 'Ned', 'Snow', 2000]
print(list * 2)           # ['Ned', 'Snow', 2000, 'Ned', 'Snow', 2000]
print(1 in list)          # False

for x in [1, 2, 3]:
    print(x, end=" ")     # 1 2 3
print("")
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)                  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])               # ['a', 'b', 'c']
print(x[0][1])            # b
print(max(a))             # c
print(min(a))             # a

list.append('Sansa')
print(list)               # ['Ned', 'Snow', 2000, 'Sansa']
print(list.count('Ned'))  # 1
list.insert(1, 1000)      # ['Ned', 1000, 'Snow', 2000, 'Sansa']
print(list.pop(-1))       # Sansa
print(list)               # ['Ned', 1000, 'Snow', 2000]
list.remove(1000)         # ['Ned', 'Snow', 2000]
list.reverse()
print(list)               # [2000, 'Snow', 'Ned']

li = list.copy()
print(li)                 # [2000, 'Snow', 'Ned']
list.clear()
print(list)               # []
print(li)                 # [2000, 'Snow', 'Ned']

list = [4, 2, 3]
list.sort(reverse=False)
print(list)               # [2, 3, 4]

