# 迭代器与生成器

# 迭代器
# 迭代器的两个基本方法 iter()和next()
# 迭代器执行完就不会在执行了
list_1 = [1, 2, 3]
it_list_1 = iter(list_1)
print(next(it_list_1))
print(next(it_list_1))
print(next(it_list_1))

print('-----------------')
it_list_2 = iter(list_1)
for i in it_list_2:
    print(i)


# 创建一个迭代器
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myClass = MyNumber()
myIter = iter(myClass)
print('MyNumber')
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

# 生成器 yield 每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        print('a: %s, b: %s ' % (a, b))
        counter += 1


f = fibonacci(10)
print('fibonacci')
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
