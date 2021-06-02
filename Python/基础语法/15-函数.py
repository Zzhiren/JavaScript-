# Python 函数
def fun_name(param):
    print(param)


fun_name('Hello Python!')


# Python 传不可变对象实例
def change_int(a):
    a = 10


b = 2
change_int(b)
print(b)


# Python 传可变对象实例
def change_list(my_list):
    my_list.append([1, 2, 3, 4])
    print("函数内取值: ", my_list)
    return


my_list = [10, 20, 30]
change_list(my_list)


# Python 必备参数 调用该函数必须传递一个参数
def print_me(msg):
    print(msg)


print_me('Hello Python!')


# Python 关键字参数
# 关键字参数不需要遵从参数顺序
def print_msg(name, age):
    print(name)
    print(age)


print_msg(age=18, name='Tom')


# Python 函数默认参数
# 默认值参数要放在没有默认值的参数后面
def print_default(age, name='Tom'):
    print(name)
    print(age)


print_default(28)


# Python 不定长参数
def long_arg(arg1, *vartuple):
    print(arg1)
    print(vartuple)
    print(arg1)
    for var in vartuple:
        print(var)

long_arg(1, 2, 3, 4)
long_arg(1)

# 两个 * 号参数会以字典传递
def dict_arg(name, **args):
    print(name)
    print(args)


dict_arg('Tom', age=10, sex='男')


# Python 使用 lambda 来创建匿名函数
sum = lambda arg_1, arg_2: arg_1 + arg_2
print(sum(1,2))


# Python return 语句
# 不带参数值的return语句返回None
def sum_1(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum_1(10, 20)
print("函数外 : ", total)


# 前置位置参数
# 形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
