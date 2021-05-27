# Python 循环语句

# while

# for in

# range()
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
for i in range(5):
    print(i)

print('-------------------')

# 指定循环区间
for i in range(1, 5):
    print(i)

print('-------------------')

# 第三个参数指定步长
for i in range(1, 5, 2):
    print(i)

print('-------------------')

# 负数使用负数步长
for i in range(-10, -100, -10):
    print(i)

# 可以结合range()和len()函数以遍历一个序列的索引,如下所示:
list_1 = ['Google', 'Baidu', 'Tencent']
for i in range(len(list_1)):
    print(i, list_1[i])

# pass 语句 pass 不做任何事情，一般用做占位语句
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
