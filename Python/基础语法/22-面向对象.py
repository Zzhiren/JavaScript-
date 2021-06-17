# 面向对象

class MyClass:
    name = 'Tom'

    # self代表类的实例，而非类
    def __init__(self):
        print(self)

    def show(self):
        print(self.name)


myClass = MyClass()
myClass.show()


# 继承
class People:
    name = ''
    sex = ''
    age = 0

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def speak(self):
        print('%s 说，我是 %s 生，今年 $d 岁了！' % (self.name, self.sex, self.age))


# 单继承
class Student(People):
    come = 0

    def __init__(self, name, sex, age, come):
        # 调用父类的构函
        People.__init__(self, name, sex, age)
        self.come = come

    # 覆写父类方法
    def speak(self):
        print('%s 说，我是 %s 生，今年 %d 岁了, 来自 %s！' % (self.name, self.sex, self.age, self.come))


s = Student('Jerry', '男', 10, 'Chinese')
s.speak()

