# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

# = 赋值语句
counter = 100  # 整型变量
miles = 100.0  # 浮点型变量
name = 'Tom'  # 字符串
print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
print('# 多个变量赋值')
print(a)
print(b)
print(c)

# 为多个变量指定多个对象
x, y, z = 1, 2, 'Tom'
print('# 为多个变量指定多个对象')
print(x)
print(y)
print(z)

# Python中六种标准数据类型
# 不可变数据----------------
# Number 数字
# String 字符串
# Tuple 元组
# 可变数据------------------
# List 列表
# Set 集合
# Dictionary 字典

# Number 支持 int，float，bool，complex（复数）
# 使用 type() 函数判断数据类型
'''
注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
'''
print('# 使用 type() 函数判断数据类型')
num_1 = 100
num_2 = 100.1
num_3 = True
num_4 = 4 + 3j
print(type(num_1), type(num_2), type(num_3), type(num_4))

# 还可以使用 isinstance 来判断
print('# 还可以使用 isinstance 来判断')
print(isinstance(num_1, int))


# isinstance 会认为子类是一种父类类型，type() 则不会
class A:
    pass


class B(A):
    pass


print('# isinstance 会认为子类是一种父类类型，type() 则不会')
print(isinstance(A(), A))
print(isinstance(B(), A))
print(type(A()) == A)
print(type(B()) == A)

# 可以使用 del 语句删除一些对象引用
var_1 = 'Tom'
var_2 = 'Jerry'
del var_1, var_2

# 数值运算
'''
注意：
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
'''
print('# 数值运算')
print(5 + 4)
print(5.2 - 4)
print(2 * 3)
print(2 / 4)  # 除法，得到一个浮点数
print(2 // 4)  # 除法，得到一个整数
print(17 % 3)  # 取余
print(2 ** 2)  # 乘方

# String 字符串类型
'''
注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
'''
# 单引号
# 双引号
# 三引号定义段落
# \ 反斜杠用来转义
word_1 = 'Hello\nPython !'
print('\ 反斜杠用来转义')
print(word_1)
# r可以使转义符不发生转义
word_2 = r'Hello \n Python!'
print('r可以使转义符不发生转义')  # 这里的 r 指 raw，即 raw string，会自动将反斜杠转义
print(word_2)

# 字符串可以用 + 号连接在一起
word_3 = 'Hello'
word_4 = ' '
word_5 = 'Python'
print('字符串可以用 + 号连接在一起')
print(word_3 + word_4 + word_5)

# 字符串可以用 * 运算符重复
word_6 = '我是你爸爸'
print('字符串可以用 * 运算符重复')
print(word_6 * 10)

# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
word_7 = '123456789'
print(word_7[0])
print(word_7[-1])
print('# 输出从下标0开始，长度是3的字符串')
print(word_7[1:3])  # 输出从下标index开始，到第三个字符
print(word_7[1:])  # 输出第二个开始后面的所有字符串
print(word_7[0:5:2])  # 输出从第1个字符串到第5个且每隔一个的字符（步长为2）

# print输出默认是换行的，如果不需要换行需要在变量末尾加上 end=""
word_8 = 'Hello '
word_9 = 'Python!'
print(word_8)
print(word_9)
print(word_8, end='')

# List 列表
list_1 = ['Tom', 'Jerry', 1, 2, 3]
list_2 = ['Hello', 'Python']
print(list_1)
print(list_1[0])
print(list_1[0:2])
print(list_1[1:2])
print(list_1 + list_2)  # 使用 + 号连接列表

# 与Python字符串的区别是列表的元素是可以改变的
list_3 = ['Tom', 'Jerry', 1, 2, 3]
print(list_3[0])
list_3[0] = 'Penny'
print(list_3[0])
list_4 = [1, 2, 3, 4, 5, 6, 7]
print('# [2:5] 选中了 3 4 5 三个元素，对应的替换成后边的值')
list_4[2:5] = ['三', '四', '五']  # 从第三个元素开始，替换到第五个元素
print(list_4)
list_5 = [1, 2, 3, 4, 5, 6, 7]
list_5[2:5] = []  # 将对应的元素设置为【】
print(list_5)

# 截取list
list_6 = [1, 2, 3, 4, 5, 6, 7]
print(list_6[1:4:2])
print(list_6[1:7:3])


# 截取中的第三个参数为负数，则是逆向读取
def reverse_words(input):
    input_word = input.split(' ')
    result = input_word[-1::-1]
    output = ' '.join(result)
    return output


if __name__ == "__main__":
    words = '1 2 3 4 5 6 7'
    rw = reverse_words(words)
    print(rw)

# Tuple 元组
'''
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
其实，可以把字符串看作一种特殊的元组。
'''
tuple_1 = ('My', 'name', 'is', 'Tom', 'age', 'is', 22)
tiny_tuple = ('High', 'is', 170)
print(tuple_1)
print(tuple_1[0])
print(tuple_1[1:3])  # 输出元组第二个元素开始到第三个元素
print(tuple_1[2:])  # 输出元组第三个元素开始的所有元素
print(tiny_tuple * 2)  # 输出两遍元组
print(tuple_1 + tiny_tuple)  # 连接元组

# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

# Set 集合
'''
*集合是无序的
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Baidu'}
print(sites)

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# Set 可以进行集合运算
set_1 = set('123ade')
set_2 = set('1245ab')
print(set_1)
print(set_1 - set_2)  # set_1 和 set_2 的差集
print(set_1 | set_2)  # set_1 和 set_2 的并集
print(set_1 & set_2)  # set_1 和 set_2 的交集
print(set_1 ^ set_2)  # set_1 和 set_2 中不同是存在的元素

# Dictionary 字典
dict_1 = {}
dict_1['one'] = '1 - 菜鸟教程'
dict_1[2] = '2 - 菜鸟工具'

tiny_dict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict_1['one'])
print(dict_1[2])
print(tiny_dict)
print(tiny_dict.keys())
print(tiny_dict.values())

# 构造函数 dict() 可以直接从键值对序列中构建字典如下
print(dict([('Runoob', 1), ('Tabao', 2)]))

print({x: x**2 for x in (2, 4, 6)})

print(dict(Runoob=1, Taobao=2))
