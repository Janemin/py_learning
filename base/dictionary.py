# 键必须是唯一的
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name']  # 删除键 'Name'
dict.clear()      # 清空字典
del dict          # 删除字典


dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dictCopy = dict.copy()        # 浅复制
print(dictCopy)               # {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dictFromKeys = dict.fromkeys(dict.keys())   # 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
print(dictFromKeys)           # {'Name': None, 'Age': None, 'Class': None}

print(dict.get('hobby', None))  # None   返回指定键的值，如果值不在字典中返回default值
dict.setdefault('hobby', 'Coding')  # 如果键不存在于字典中，将会添加键并将值设为default

print(dict.items())           # [('Name', 'Runoob'), ('Age', 7), ('Class', 'First')]   以列表返回可遍历的(键, 值) 元组数组

print(dictFromKeys)           # {'Name': None, 'Age': None, 'Class': None}
dictFromKeys.update(dict)     # 把字典dict的键/值对更新到dictFromKeys里
print(dictFromKeys)           # {'Name': 'Runoob', 'Age': 7, 'Class': 'First', 'hobby': 'Coding'}

print(dict.pop('Name', None))  # Runoob
print(dict)                    # {'Age': 7, 'Class': 'First', 'hobby': 'Coding'}

print(dict.popitem())          # ('hobby', 'Coding')   随机返回并删除字典中的一对键和值(一般删除末尾对)
print(dict)                    # {'Age': 7, 'Class': 'First'}

for k, v in dict.items():
    print(k, v)                # Age 7
                               # Class First
