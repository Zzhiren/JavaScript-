# 第一个注释
print('Hello Python!')  # 第二个注释

# 多行注释
# 可以使用多个 # 号

'''
第一行注释
第二行注释
第三行注释
'''

"""
第四行注释
第五行注释
"""

print('注释的使用！')

# 行与缩进，python使用缩进代替大括号，所有行代码缩进必须对齐
status = True
if status:
    print('True')
else:
    print('False')

# 以下代码因为缩进未对齐，运行时会报错
# if status:
#     print('Tom')
#     print('True')
# else:
#     print('Jerry')
#   print('run') # 缩进不一致，会导致运行错误

# 多行语句
item_one = 'Hello'
item_tow = 'Python'
item_three = '!'
total_one = item_one + \
        item_tow + \
        item_three

print(total_one)

# 在[],{},()中的多行语句不需要使用反斜杠(\)
total_two = [
    'item_one', 'item_tow',
    'item_three'
]

print(total_two)

# 数字(Number)类型
# int(整数)，表示长整型
# bool(布尔)，True
# float(浮点数)，如 1.23、3E-2
# complex(复数)，如 1 + 2j、 1.1 + 2.2j

# 字符串(String)
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
print(word_7[0:3])  # 输出从下标0开始，长度是3的字符串
print(word_7[1:])  # 输出第二个开始后面的所有字符串
print(word_7[0:5:2])  # 输出从第1个字符串到第5个且每隔一个的字符（步长为2）

# print输出默认是换行的，如果不需要换行需要在变量末尾加上 end=""
word_8 = 'Hello '
word_9 = 'Python!'
print(word_8)
print(word_9)
print(word_8, end='')
print(word_9)

# import 与 from...import 的区别
# 在 python 用 import 或者 from...import 来导入相应的模块
# 将整个模块(someModule)导入，格式为 import someModule
# 从某个模块中导入某个函数，格式为 from someModule import someFunction
# 从某个模块中导入多个函数，格式为 from someModule import firstFunction, secondFunction, threeFunction
# 将某个模块中的函数全部导入, 格式为 from someModule import *

# 导入sys磨具爱
import sys
print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)

print('\n python 路径为', sys.path)
