<!-- TOC -->

- [《JavaScript高级程序设计》学习笔记](#javascript%E9%AB%98%E7%BA%A7%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0)
  - [第1章 JavaScript简介](#%E7%AC%AC1%E7%AB%A0-%08javascript%E7%AE%80%E4%BB%8B)
  - [第2章 在HTML中使用JavaScript](#%E7%AC%AC2%E7%AB%A0-%E5%9C%A8html%E4%B8%AD%E4%BD%BF%E7%94%A8javascript)
  - [第3章 基本概念](#%E7%AC%AC3%E7%AB%A0-%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5)
    - [3.4 数据类型](#34-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)
      - [3.4.1 tyiepof操作符（注意：typeof不是函数）](#341-tyiepof%E6%93%8D%E4%BD%9C%E7%AC%A6%E6%B3%A8%E6%84%8Ftypeof%E4%B8%8D%E6%98%AF%E5%87%BD%E6%95%B0)
      - [3.4.2 Undifined类型](#342-undifined%E7%B1%BB%E5%9E%8B)
      - [3.4.3 Null类型](#343-null%E7%B1%BB%E5%9E%8B)
      - [3.4.4 Boolean类型](#344-boolean%E7%B1%BB%E5%9E%8B)
      - [3.4.5 Number类型](#345-number%E7%B1%BB%E5%9E%8B)
        - [1. 浮点数值](#1-%E6%B5%AE%E7%82%B9%E6%95%B0%E5%80%BC)
        - [2. 数值范围](#2-%E6%95%B0%E5%80%BC%E8%8C%83%E5%9B%B4)
        - [3. NaN](#3-nan)
        - [4. 数值转换](#4-%E6%95%B0%E5%80%BC%E8%BD%AC%E6%8D%A2)
      - [3.4.6 String类型](#346-string%E7%B1%BB%E5%9E%8B)
        - [1. 字符字面量](#1-%E5%AD%97%E7%AC%A6%E5%AD%97%E9%9D%A2%E9%87%8F)
        - [2. 转换为字符串](#2-%E8%BD%AC%E6%8D%A2%E4%B8%BA%E5%AD%97%E7%AC%A6%E4%B8%B2)
        - [3.4.7 Object类型](#347-object%E7%B1%BB%E5%9E%8B)
  - [第4章 变量、作用域和内存问题](#%E7%AC%AC4%E7%AB%A0-%E5%8F%98%E9%87%8F%E4%BD%9C%E7%94%A8%E5%9F%9F%E5%92%8C%E5%86%85%E5%AD%98%E9%97%AE%E9%A2%98)
    - [4.1 基本类型和引用类型的值](#41-%E5%9F%BA%E6%9C%AC%E7%B1%BB%E5%9E%8B%E5%92%8C%E5%BC%95%E7%94%A8%E7%B1%BB%E5%9E%8B%E7%9A%84%E5%80%BC)
      - [4.1.1 动态的属性](#411-%E5%8A%A8%E6%80%81%E7%9A%84%E5%B1%9E%E6%80%A7)
      - [4.1.2 复制变量值](#412-%E5%A4%8D%E5%88%B6%E5%8F%98%E9%87%8F%E5%80%BC)
      - [4.1.3 传递参数](#413-%E4%BC%A0%E9%80%92%E5%8F%82%E6%95%B0)
      - [4.1.4 检测类型](#414-%E6%A3%80%E6%B5%8B%E7%B1%BB%E5%9E%8B)
    - [4.2 执行环境及作用域](#42-%E6%89%A7%E8%A1%8C%E7%8E%AF%E5%A2%83%E5%8F%8A%E4%BD%9C%E7%94%A8%E5%9F%9F)

<!-- /TOC -->



# 《JavaScript高级程序设计》学习笔记
## 第1章 JavaScript简介

## 第2章 在HTML中使用JavaScript

## 第3章 基本概念
### 3.4 数据类型
>6种数据类型
* Undefined
* Null
* Number
* String
* Boolean
* Object

#### 3.4.1 tyiepof操作符（注意：typeof不是函数）
`typeof`返回值: 
* `undefined`-值未定义
* `string`-值为字符串
* `boolean`-**值为布尔值**
* `number`-**值为数字**
* `Object`-值为对象/null
* `function`-值为函数

`null被认为是一个空的对象引用，原型链中最顶端的 Object.prototype(构造函数原型) 的 __proto__ 指向 null`

#### 3.4.2 Undifined类型
>Undefined类型只有一个值，即特殊的`undefined`，使用`typeof`检测`undefined`时返回`undefined`
```js
// 声明了变量，但未初始化
let message;
let str = undefined;
typeof messge; // undefined
typeof str; // undefined

console.log(message == undefined); // true
console.log(str == undefined); // true

console.log(message === undefined); // true
console.log(str === undefined); // true
```

`注意：对于为定义的变量，typeof 操作符仍然会返回 undefined`
```js
// let test
console.log(test); // 会报错，提示test is not defined
typeof test; // 返回undefined
```

#### 3.4.3 Null类型
>Null类型是第二个只有一个值的类型，即`null`，`null`值表示一个空对象指针，所以使用`typeof`检测`null`值时返回`object`
```js
let car = null;
console.log(typeof car); // object
```
>如果定义的变量准备保存`对象`，那么最好将对象初始化为`null`，这样可以直接通过检测null值来判断变量是否已经保存了一个对象的引用。
```js
let car = null;
if (car != null) {
  // do something
}
```
>其实 `undefined` 是派生自 `null`，所以它们的想等性(==)检测结果为`true`，但是如果使用严格等于(===)，因为 `typeof null` 返回 `object` ，`typeof undefined` 返回   `undefined`，二者数据类型不一致，所以使用严格等于判断时返回 `false`
```js
console.log(undefined == null); // true

console.log(undefined === null); // false
```
#### 3.4.4 Boolean类型
>`Boolean` 有两个字面值：`true/false`，虽然Boolean只有两个值，但ECMAScript中的所有类型都有与这两个Boolean值等价的值，可以调用`Boolean()`进行转换

```js
let message = 'Hello JS';
let messageBoolean = Boolean(message);
console.log(messageBoolean); // true
```

| 数据类型 | 转换为true值 | 转换为false值 
| - | - | - |
| Boolean | true | false
| String | 任何非空字符串 | 空字符串
| Number | 任何非0数值（包括无穷大） | 0/NaN
| Object | 任何对象 | null
| Undefined | 不适用 | undefined

> 字符串无法与`true`直接通过`==`进行判断，无论为`正常字符串`还是`空字符串`都返回false；但是字符串`1`除外。
```js
// String
let str = 'Hello JS';
function test(){
  if(str == true){
    console.log('str == true')
  } else if(str){
    console.log(str)
  }
}

test(); // Hello JS

console.log(str == true); // false
console.log('hello js' == true); // false
console.log('' == true); // false
console.log(1 == true); // true
console.log('1' == true); // true
```

>数字与`true`通过`==`进行判断，只有`1`会返回`true`，其他数字都会返回`false`；但是是如果通过`if(num)`进行判断，任何非`0`数值（包括无穷大）都为`true`，当数值通过严格等于`===`与`true/false`进行判断时全部返回`false`，因为数值为`Number`类型

```js
// Number
function test(){
  let num1 = 0;
  let num2 = 1;
  let num3 = 999;

  if(!0){
    // do something;
  };

  // 0 == false 判断返回false
  if(0 != false){
    // do something
  };

  if(1){
    // do something
  };

  // 1 == true 返回true
  if(1 == true){
    // do something
  };

  if(999){
    // do something
  };

  // 999 == true 返回false
  if(999 != true){
    // do something
  }

  // 正无穷，负无穷
  if(Infinity){
    // do something
  }
  if(-Infinity){
    // do something
  }
};

test();
```

>`Object` 都返回 `true` ，只有空对象 `null` 返回 `false`

```js
function test(){
  let obj = {};
  let data = {
    name: 'Zzhiren'
  };
  let empty = null;
  if(obj){ // true
    // do something
  }

  if(data){ // true
    // do something
  }

  if(!empty){ // true
    // do something
  }
}

test();
```

>`Undefined` 返回 `false`，`undefined` 不同通过 `==` 与 `true/false` 进行判断

```js
function test(){
  let value;
  if(!value){ // true
    // do something
  }

  if(value == true){
    console.log('undefined == true');
  }else if(value == false){
    console.log('undefined == false');
  }else{
    console.log('undefined != false && undefined != true');
  }
}
test();
```

#### 3.4.5 Number类型
`注意：在进行算术计算时，所有八进制和十六进制数都将转换成十进制数进行计算。`

##### 1. 浮点数值
* 浮点数值需要的内存空间为整数值的两倍
* ECMAScript会将一些浮点数保存为整数值来节省内存空间
  * `1.` 解析为 `1`
  * `10.0` 解析为 `10
* 浮点数最高精度为17位，浮点数进行算术运算可能会丢失精度

>0.1加0.2不等于0.3，而等于0.30000000000000004，所以不要用浮点数做如下的一些测试

```js
// 不要做这样的测试
if(a + b == 0.3){
  console.log('a加b等于0.3)
}
```

##### 2. 数值范围
* 最大值：保存在Number.MAX_VALUE
* 最小值：保存在Number.MIX_VALUE

##### 3. NaN
>`NaN`表示非数值，即（Not a Number），这个数值表示一个本来应该返回数值的操作未返回数值的情况

```js
// 数值除以字符串结果肯定不为数值
console.log(999/'test'); // NaN
```

##### 4. 数值转换
* **Number()**
  * `Boolean` 转换成 `0/1`
  * `null` 返回 `0`
  * `undefined` 返回 `NaN`
  * 字符串
    * 只包含数字（包括正负号），转为十进制数，前面的0被忽略
    * 浮点数转换为浮点数，前面的0被忽略
    * 字符串中包含有效的`十六进制格式`，则会转换为相等的`十进制数`
    * 如果字符中包含除上述格式之外的字符，转为NaN `举例：'this is a string'`
    * 转换对象
  * **`总结：`**
    * 只要字符串中有非数字（十六进制格式除外），全部转换为NaN
    * 其他进制全部转换为十进制数
    * 数值正负转换后依然保留正负
* **parseInt()**
  * 从字符串第一个字符开始解析，遇到非字符串解析停止，返回非字符串之前的数值
  * 能够识别其他进制，将其他进制转换为十进制数
    * `空字符串`返回`NaN`，`Number()`则返回`0`
* **parseFloat()**
  * 只转换十进制，十六进制将转换为0
  * 如果字符串包含的是一个整数格式，则会返回整数
  * 其他规则与parseInt()类型

```js
// Number()，
let num1 = Number('Hello JS'); // NaN
let num3 = Number('00011'); // 11
let num4 = Number(true); // 1

// parseInt()
let num1 = parseInt('123blue'); // 123
let num3 = parseInt('-999'); // -999
let num4 = parseInt('0xf'); // 15
let num5 = parseInt('070', 8); // 56

// 转换空字符串的区别
let num2 = Number(''); // 0
let num2 = parseInt(''); // NaN
```

#### 3.4.6 String类型

##### 1. 字符字面量
`转义字符`
>这些字符字面量可以出现在字符串中的任意位置，而且也被当作一个字符来解析

| 字面量 | 含义 |
| - | - |
| \n | 换行
| \t | 制表
| \b | 空格
| \r | 回车
| \f | 走纸换页
| \' | 单引号
| \" | 双引号

##### 2. 转换为字符串
`注意以下几点`
```js
let num1 = null;
num1.toString(); // 报错，没有toString()方法
String(num1); // 返回字符串'null'

let num2;
num2.toString(); // 报错，undefined的值没有toString()方法
String(num2); // 返回字符串 'undefined'
```

##### 3.4.7 Object类型
创建一个对象
```js
let obj = new Object(); // 不推荐写法
let obj = new Object;   // 不推荐写法

let obj = {};   // 推荐写法
```

>所有的对象都源于`Object`对象

`Object`的每个实例都具有下列属性和方法
* `Constructor`（构造函数）: 保存用户创建当前对象的函数，上面的例子构造函数就是`Object()`
* `hasOwnProperty(propertyName)`: 检查当前对象中是否有某个属性（`不检查原型链，只检查当前对象的私有属性`）
* `isPrototypeOf(Object)`: 检查传入的对象是否存在于另一个对象的原型链中
* `propertyIsEnumerable(propertyName)`: 检查给定的属性是否能够使用`for-in`语句来枚举
* `toLocaleString()`: 返回对象的字符串表示，该字符串与执行环境的地区对应
* `toString()`: 返回对象的字符串表示
* `valueOf()`: 返回对象的字符串、数值或布尔值表示

```js
// hasOwnProperty(propertyName)
function Man() {
  this.sex = 'man'
}
Person.prototype.type = 'person'
Man.hasOwnProperty('type'); // false 不检查原型链上的属性

// isPrototypeOf(Object)
function Person(){
  this.type = 'person' 
}
let person = new Person();
let man = new Person();
console.log(man.type);

// man的原型对象存在于Person对象的原型链中
console.log(Person.prototype.isPrototypeOf(man)); // true
```

## 第4章 变量、作用域和内存问题
### 4.1 基本类型和引用类型的值
* 按值访问，可以直接操作保存在变量中的实际的值
  * Undefined
  * Null
  * Boolean
  * Number
  * String
* 按引用访问
  * Object

#### 4.1.1 动态的属性

#### 4.1.2 复制变量值

* 基本类型值（两个变量值一样，当时相互独立）
* 引用类型值（复制的是引用地址值，相互独立，但两个变量的值仍然指向同一个对象）

#### 4.1.3 传递参数

>所有函数的参数都是按值传递的

```js
// 示例1
let num = 100;
let obj = {name:'Alice'}; // obj存储着对象的地址值 0x000000

function test(num,obj){
  // o 保存着对象的地址 0x000000，与外部的obj指向同一个对象
  let n = num; // 100
  let o = obj; // 指向 {name:'Alice'}
}
test(num,obj);

// 示例2
function setName(obj) {
  obj.name = 'Alice';
  obj = new Object();
  obj.name = 'Tom';
}
var person = new Object();
setName(person);
console.log(person.name); // Alice

```
>`setName()`的内部`obj`会在函数执行完成后被销毁

#### 4.1.4 检测类型
* `typeof` 只能检测基本类型，引用类型一律返回 `Object`
* instanceof 检测引用类型

>`instanceof` 检测的缺点，只要是引用类型的都属于 `Object`
```js
// instanceof 的缺点
let arr = [];
arr instanceof Object; // true
arr instanceof Array; // true

function test(){

}

test instanceof Object; // true
```

### 4.2 执行环境及作用域

概念
* 函数执行环境
* 执行环境栈
* 作用域/作用域链

>分析执行环境与作用域

分析：
* 创建 `one()` 执行环境，压栈
* 调用 `two()` ，创建 `tow()` 执行环境，压栈
* 调用 `three()` ，创建 `three()` 执行环境，压栈
* `three()` 执行完成，出栈，继续执行 `tow()` 
* `two()` 执行完成，出栈，继续执行 `one()` 
* `one()` 执行完成，出栈

```js
// 执行环境
function one() {
  console.log('one');
  two();
  console.log('tow()出栈‘)
};

function two() {
  console.log('创建two()的执行环境，并压栈');
  three();
  console.log('two');
};

function three() {
  console.log('创建three()的执行环境，并压栈‘);
  console.log('three')
}

one();

// 作用域
function person(){
  let type = 'person'

  function man() {
    let name = 'Tom';
    console.log(type); // 可以访问person的变量
  };

  function woman() {
    let height = 170;
    console.log(type); // 可以访问person的变量
    console.log(name); // 会报错，因为无法访问到man的变量
  };

  man();
  woman();
}

person();
```

总结：js在执行到函数时，会创建执行环境，执行环境中保存着变量对象和作用域链，作用域链中保存着当前函数可以访问到的所有变量对象，所以当一个函数自身未定义某个变量时，会沿着作用域链查找，当查找到需要的变量时立即停止查找，如果知道查找到全局执行环境还未查询到改变了则会返回未定义。

[拓展: 下面函数的打印顺序](./JS笔试题.md)













