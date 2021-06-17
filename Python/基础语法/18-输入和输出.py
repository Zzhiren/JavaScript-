# Python 输入和输出
'''
str(): 函数返回一个用户易读的表达形式
repr(): 产生一个解释器易读的表达形式
'''

str_1 = 'Hello Python!'
print(str(str_1))
print(repr(str_1))

# repr() 函数可以转移字符串中的特殊字符
str_2 = 'Hello, Python\n'
print('repr(str_2)', repr(str_2))

# 读取键盘输入
str_3 = input("请输入：");
print ("你输入的内容是: ", str_3)

# 读和写文件
# open(filename, mode)
