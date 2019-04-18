# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
# 字符串，列表或元组对象都可用于创建迭代器

list = list(range(5))

# for
it = iter(list)
for x in it:
    print(x, end=" ")
print("")

# while & next()
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        break


# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # 触发 StopIteration 异常来结束迭代


myClass = MyNumbers()
myIter = iter(myClass)

for x in myIter:
    print(x, end=" ")


# 使用了 yield 的函数被称为生成器（generator）
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        break
