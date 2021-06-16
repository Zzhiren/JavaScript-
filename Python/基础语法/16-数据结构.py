# Python 数据结构

# 列表
# list.append(x) 把一个元素添加到列表的结尾
list_1 = [1, 2, 3, 4, 5]
list_1.append(6)
print('list_1', list_1)

# list.extend(L) 使用另一个列表扩充该列表
list_2 = [1,2,3]
list_3 = [5,6,7]
list_2.extend(list_3)
print('list_2', list_2)

# list.insert(i,x) 在指定位置插入一个元素
list_4 = [1,2,3,4]
list_4.insert(1,'a')
print('list_4', list_4)

# list.remove(x) 删除列表中第一个x元素，如果没有这样的元素就会返回一个错误
list_5 = [1, 2, 2, 3, 3]
list_5.remove(3)
print('list_5', list_5)
'''
会报错
list_5.remove(10)
print('list_5', list_5)
'''

# list.pop([i]) 从列表指定位置移除元素，并将其返回，如果没有指定，则移除左后一个元素
list_6 = [1, 2, 3, 4, 5]
print(list_6.pop(1))
print('list_6', list_6)

# list.clear() 移除列表中的所有项，相当于del a[:]
list_7 = [1, 2, 3, 4, 5]
list_7.clear()
print('移除列表中的所有项目：list_7.clear()：list_7=', list_7)

# list.index(x) 返回列表中第一个值为 x 的索引，如果没有匹配到就会返回一个错误
list_8 = [1, 2, 3, 4, 5]
print(list_8.index(2))
try:
    print(list_8.index(10));
except ValueError:
    print(ValueError)

# list.count(x) 返回 x 在列表中出现的次数
list_9 = [1, 2, 2, 3, 4, 5]
print(list_9.count(2))

# list.sort() 对列表中的元素进行排序
list_10 = [1, 10, 2, 12, 0, 8, 7, 3, 2, 10]
list_10.sort()
print(list_10)

# list.reverse() 倒排列表中的元素
list_11 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list_11.reverse()
print(list_11)

# list.copy() 返回列表的浅复制
list_a = ['a']
list_12 = [1, 2, 3, list_a]
list_copy = list_12.copy()
print(list_a)
print(list_copy)
list_a.append('b')
print(list_a)
print(list_copy)

# 列表推导式
'''
列表推导式提供了从序列创建列表的简单途径。
通常应用程序将一些操作应用于某个序列的每个元素，
用其获得的结果作为生成新列表的元素，
或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，
然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
如果希望表达式推导出一个元组，就必须使用括号。
'''

# 这里我们将列表中每个数值乘三，获得一个新的列表：
vec = [2, 4, 6]
list_13 = [3 * x for x in vec]
print(list_13)
list_14 = [[3, 3*x] for x in vec]
print(list_14)

# 对列表的每个元素调用某个方法
list_15 = [' Hello ', ' Tom! ']
list_16 = [str.strip() for str in list_15]
print(list_16)

# 可以使用 if 子句作为过滤器
list_17 = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
list_18 = [x for x in list_17 if x >= 10]
print(list_18)

# 关于循环和其它技巧的演示
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
list_19 = [x*y for x in vec1 for y in vec2]
list_20 = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(list_19)
print(list_20)

# 嵌套列表解析
list_21 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list_22 = [[row[i] for row in list_21] for i in range(4)]
print('list_21', list_21)
print('list_22', list_22)

# del 语句
'''
使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，
或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）
'''
list_23 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del list_23[0]
print('del list_23[0]', list_23)
del list_23[2:4]
print('del list_23[2:4]', list_23)
del list_23[:]
print('del list_23[:]', list_23)


# 元组和序列
tuple_1 = 1, 123, 'hello python'
tuple_2 = 'Hello Tuple', 2
tuple_3 = tuple_1, tuple_2
print(tuple_1)
print(tuple_1[0])
print(tuple_3)


# 集合
'''
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；
后者创建一个空的字典，下一节我们会介绍这个数据结构。
'''
set_1 = {'Hello', 'Python', 'Hello', 'Python'}
print('set_1', set_1)
# 监测成员
print('Hello' in set_1)

set_2 = set('abcdef123z')
set_3 = set('abcef12y')
print(set_2)
print(set_2 - set_3)  # 在set_2中但不再set_3中的
print(set_2 | set_3)  # 在set_2或set_3中的
print(set_2 & set_3)  # 同时存在于set_2和set_3 中的
print(set_2 ^ set_3)  # 在 set_2或set_3某一个中，不同时存在

# 集合也支持推导式
set_4 = {x for x in 'abracadabra' if x not in 'abc'}
print('set_3', set_4)

# 字典
dict_1 = {'name': 'Tom', 'age': 18}
# 从元组构建字典
tuple_4 = ('name', 'Tom'), ('age', 18)
dict_2 = dict(tuple_4)
dict_3 = dict([('job', 'web dev'), ('title', '工程师')])
dict_4 = dict(name='Zzhiren', age=26)
print(dict_2)
print(dict_3)
print(dict_4)
