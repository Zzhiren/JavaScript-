# 目录
* [第一部分](#one)
  * [第1章 面向对象的JavaScript](#1)
    * [多态](#1.2)
    * [原型式和基于原型继承的JavaScript对象系统](#1.4)
    * [本章小结](#one-end)
  * [第2章 this，call和apply](#2)
  * [第3章 闭包和高阶函数](#3)

# <span id='one'>第一部分</span>

---

## <span id='1'>第1章 面向对象的JavaScript</span>

### <span id='1.2'>1.2 多态</span>
* 什么是多态？
* 多态的意义？

**1. 什么是多态？**
“多态性”一词最早用于生物学，指同一种族的生物体具有不同的特性。

在面向对象编程中，“多态性”指不同类的实例在接收到相同消息时做出的不同反应。

举个例子：
> 喜鹊，兔子，金鱼分别是鸟类的实例、走兽的实例和鱼类实例，当它们同时感受到生命威胁时它们都会逃跑，但是它们逃跑的方式不一样，喜鹊会飞走，兔子会钻进洞中逃跑，鱼会游走；这就是不同的类实例在接收到相同消息时做出的不同反应。

再举个例子：
> 兔子和梅花鹿分别是兔科实例和鹿科实，它们接收到危险信号时兔子会钻洞，而梅花鹿会进行奔跑来躲避危险。

再举个例子：
> 喜鹊，兔子，金鱼都属于动物的实例，而中国人则属于人类的一个实例，当动物与人类接收到危险信号时，动物会逃跑，人类会反击。

在上面例子中，不同类的实例都具有接收危险信号的属性，但是他们的反应行为都不一样，这就是我理解的多态。

**2. 静态多态性**
>

**3. 动态多态性**
>

**4. 多态的意义**
> 多态可以让发出消息的主体不需要对接收实体进行区分，而接收的实体在接收到消息后会自行进行逻辑处理。

### <span id='1.4'>1.4 原型式和基于原型继承的JavaScript对象系统</span>
* 什么是基于原型的编程范式？
* 原型继承的原理？
* 原型链？

**1.4.4 原型编程范型的一些规则**
* 所有数据都是对象。
* 要得到一个对象，是将另一个对象座位原型并克隆它。
* 对象会记住它的原型。
* 如果对象无法响应某个请求，它会把这个请求委托给它自己的原型。

**1.4.5 JavaScript中的原型继承**

模拟 new 的实现过程 [code](../code/001-JavaScript中的原型继承.js)

```javascript
let objectFactory = function () {
  let obj = new Object();
  let Constructor = [].shift.call(arguments); // 取得外部传入的构造函数
  obj.__proto__ = Constructor.prototype;
  let result = Constructor.apply(obj, arguments); // 借用外部传入的构造器给obj设置属性
  return typeof  result === 'object' ? result : obj; // 确保构造器总是会返回一个对象
}
```
通过 `__proto__` 与 Constructor.prototype(构造函数原型) 建立连接并继承原型的属性，这个连接就是原型链。
> obj.__proto__ = Constructor.prototype

（知识点）
>[].shift.call(arguments)，因为函数的 **arguments** 是一个类数组，
> 无法使用数组方法，但可以借用数组上的方法对 arguments 进行数组操作。
> 
> 可以通过 **Array.prototype.slice.call(arguments)** 将 arguments 转换成数组

### <span id='one-end'>本章小结</span>
* JavaScript是通过原型来实现继承的。
* 对象会通过构造器原型查找自身没有的属性。
* 原型继承也是一种设计模式-原型模式。

---

## <span id='2'>第2章 this，call和apply</span>

### <span id='2.1'>this</span>
JavaScript的 this 是根据`执行环境动态绑定（或叫确定）`的，不是声明的时候确定的。

#### 2.1.1 this的指向
* bind的实现原理？
* 构造函数的默认返回和手动return的结果区别？
* 构造函数手动return对象和return非对象的区别？
* V8引擎中Array各种操作的源码？（push,pop等）

---

## <span id='3'>第3章 闭包和高阶函数</span>

### <span id='3.1'>3.1 闭包</span>

#### 3.1.1 变量的作用域
* 全局作用域
* 函数内部作用域

#### 3.1.2 变量的生存周期
* 全局变量的生命周期
* 函数内部变量的生命周期
* 闭包函数访问的变量生命周期

1. 全局变量的生命周期
> 全局变量的生命周期是永久的，除非我们主动销毁

2. 函数内部变量的生命周期
> 当这个函数执行完毕，函数退出执行栈时，下一次垃圾清理机制运行时将会被销毁。

3. 闭包函数访问的变量生命周期 [code](../code/002-变量的生存周期.js)
> 被闭包函数引用的变量，当它的执行环境退出时，它任然不会被销毁。

理论上函数 say() 在 let man = say() 这个赋值语句执行完成后已经退出执行环境，name，应该会被销毁，但是因为 say() 返回了一个匿名函数，而匿名函数引用了 name 局部变量，所以垃圾回收机制不会销毁 name
```javascript
function say() {
  let name = 'Jerry'
  return function () {
    console.log(`My name is ${name}`)
  }
}

let man = say()

man()
```

#### 3.1.3 闭包的更多作用

1.封装变量 [cdoe](../code/003-闭包_封装变量.js)
   
>闭包可以把一些不需要暴露在全局的变量封装成“私有变量”。

用一个自执行匿名函数返回一个匿名函数，mult 其实是 return 后面的这一段，而cache则被闭包在匿名自执行函数内，起到了“私有变量”保护的作用
```javascript
let mult = (function () {
  let cache = {}
  return function () {
    let args = Array.prototype.join.call(arguments, ',')
    if (args in cache) {
      return cache[args]
    }
    let a = 1
    for (let i = 0, l = arguments.length; i < l; i++) {
      a = a * arguments[i]
    }

    return cache[args] = a
  }
})()
```

将计算乘积的函数也封闭在闭包内。
```javascript
let mult = (function () {
  let cache = {}
  let calculate = function () { // 封闭计算乘积函数
    let a = 1
    for (let i = 0, l = arguments.length; i < l; i++) {
      a = a * arguments[i]
    }
    return a
  }
  return function () {
    let args = Array.prototype.join.call(arguments, ',')
    if (args in cache) {
      return cache[args]
    }
    
    return cache[args] = calculate.call(null, arguments)
  }
})()
```

2.延续局部变量的寿命


#### 3.1.4 闭包和面向对象设计 
   
闭包的写法
```javascript
let extent = function () {
  let value = 0
  return {
    call: function () {
      value++
      console.log(value)
    }
  }
}

extend.call() // 1
extend.call() // 2
extend.call() // 3
```

面向对象的写法
```javascript
let extent = {
    value: 0,
    call: function () {
        this.value++
        console.log(this.value)
    }
}

extend.call() // 1
extend.call() // 2
extend.call() // 3
```

#### 3.1.5 用闭包实现命令模式 [code](../code/004-实现命令模式.html)

### <span id='3.2'>3.2 高阶函数</span>
