
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)
'''
这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( 	 )。
也可以使用换行符 [ 
 ]。
 '''

# Built-in function
str = "abcde"
a = ''

print(str.capitalize())   # Abcde        |  将字符串的第一个字符转换为大写
# print(str.center(2, 'x'))
print(str.count('cd'))    # 1
# print(str.encode())
print(str.startswith('de'))  # False
print(str.endswith('de')) # True
print(str.find('cd'))     # 2
print(str.rfind('cd'))    # 2            |  从右边开始查找
print(str.find('cad'))    # -1
print(str.index('cd'))    # 2
print(str.rindex('cd'))   # 2            |  从右边开始查找
# print(str.index('cad'))   # ValueError: substring not found
print(str.isalnum())      # True         |  所有字符都是字母或数字
print(str.isalpha())      # True         |  所有字符都是字母
print(str.isdigit())      # False        |  字符串只包含数字
print(str.islower())      # True         |  字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写
print(str.isupper())      # False        |  字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写
print(str.isnumeric())    # False        |  字符串中只包含数字字符
print(str.isspace())      # False        |  字符串中只包含空白
print(str.__len__())      # 5
print(len(str))           # 5
print(str.lower())        # abcde        |  转换字符串中的小写字母为小写
print(str.upper())        # ABCDE        |  转换字符串中的小写字母为大写
print(max(str))           # e            |  返回字符串 str 中最大的字母
print(min(str))           # a            |  返回字符串 str 中最小的字母
print(str.replace('ab', '11'))  # 11cde  |  返回字符串 str 中最小的字母
print(str.lstrip('ab'))   # cde          |  截掉字符串左边的空格或指定字符
print(str.rstrip())       # abcde        |  删除字符串字符串末尾的空格
print(str.strip('a'))     # bcde         |  截掉字符串两边的空格或指定字符
print("1 2 3 4".split(" ", 2))  # ['1', '2', '3 4']
print("1\r2\n3\r\n4".splitlines())  # ['1', '2', '3', '4']
print("1\r2\n3\r\n4".splitlines(keepends=True))  # ['1\r', '2\n', '3\r\n', '4']
print('aBcD'.swapcase())  # AbCd         |  大写转换为小写，小写转换为大写
print('aBcD'.title())     # Abcd         |  "标题化"的字符串, 所有单词都是以大写开始，其余字母均为小写
print('Abcd'.istitle())   # True
print('10d'.isdecimal())  # False        |  只包含十进制字符
