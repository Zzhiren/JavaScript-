# 第一部分

## 第1章 面向对象的JavaScript

### 1.2 多态
* 什么是多态？
* 多态的作用与意义？

### 1.4 原型式和基于原型继承的JavaScript对象系统
* 什么是基于原型的编程范式？
* 原型继承的原理？
* 原型链？

（知识点）
>[].shift.call(arguments)，因为函数的 **arguments** 是一个类数组，
> 无法使用数组方法，但可以借用数组上的方法对 arguments 进行数组操作。
> 
> 可以通过 **Array.prototype.slice.call(arguments)** 将 arguments 转换成数组

### 本章小结
* JavaScript是通过原型来实现继承的。
* 对象会通过构造器原型查找自身没有的属性。
* 原型继承也是一种设计模式-原型模式。
