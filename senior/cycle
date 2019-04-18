# while

# sum 0 - 100   ==>  5050
n = 100
sum = 0
counter = 1

while counter <= n:
    sum += counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))


# while … else
count = 0
while count < 5:
    count += 1
    print(count, " 小于 5")
else:
    print(count, " 大于或等于 5")

# simple while
count = 0
while count < 3: count +=1
print("count = ", count)

# for
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    if x == 'Perl':
        break
    else:
        print(x, end=" ")

print("")

# range()
for i in range(5):           # [0, 5)
    if i == 3:
        continue
    else:
        print(i, end=' ')

print("")

for i in range(0, 10, 3):    # 0 3 6 9
    print(i, end=' ')

print('')

# range() & len()
for i in range(len(languages)):
    print(i, languages[i])


# construct list with range()
print(list(range(5)))     # [0, 1, 2, 3, 4]


# for … else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:     # 穷尽列表(以for循环)
        # 循环中没有找到元素
        print(n, ' 是质数')

# pass 是空语句，是为了保持程序结构的完整性
while True:
    pass  # 等待键盘中断 (Ctrl+C)




