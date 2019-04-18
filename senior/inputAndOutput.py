# 输出值的方式
#  - 表达式语句
#  - print() 函数
#  - 文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用

# 将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
#    - repr() 函数可以转义字符串中的特殊字符
#    - repr() 的参数可以是 Python 的任何对象

got = 'Game of Thrones'

print(str(got))           # Game of Thrones
print(repr(got))          # 'Game of Thrones'

#　write file
f = open('test.txt', 'w', encoding='utf-8')
# f.writelines('')
f.write('Python 是一个非常好的语言。\n是的，的确非常好!!\n')
f.close()

# read file
f = open('test.txt', 'r', encoding='utf-8')
str = f.read()
# str = f.readline()    # 读一行
# strList = f.readlines()    # 读多行   ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']
print(str)
f.close()


f = open('test.txt', 'r', encoding='utf-8')
for line in f:
    print(line, end='')
f.close()
