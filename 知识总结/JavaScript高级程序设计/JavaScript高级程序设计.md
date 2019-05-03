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
>其实`undefined`是派生自`null`，所以它们的想等性检(==)测结果为`true`，但是如果使用严格等于(===)，因为`typeof null`返回`object`，`typeof undefined`返回`undefined`，二者数据类型不一致，所以使用严格等于判断时返回`false`
```js
console.log(undefined == null); // true

console.log(undefined === null); // false
```
#### 3.4.4 Boolean类型
>`Boolean`有两个字面值：`true/false`，虽然Boolean只有两个值，但ECMAScript中的所有类型都有与这两个Boolean值等价的值，可以调用`Boolean()`进行转换
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
    console.log(`0 -> false`);
  };

  // 0 == false 返回false
  if(0 == false){
    console.log('0 == false');
  };

  if(1){
    console.log(`1 -> true`);
  };

  // 1 == true 返回true
  if(1 == true){
    console.log(`1 == true`);
  };

  if(999){
    console.log(`999 -> true`);
  };

  // 999 == true 返回false
  if(999 == true){
    console.log(`999 == true`);
  }else {
    console.log(`999 != true`);
  }

  if(Infinity){
    console.log('正无穷相当于true')
  }
  if(-Infinity){
    console.log('负无穷相当于true')
  }
};

test();
// num1 -> false
// num1 == false
// num2 -> true
// num2 == true
// num3 -> true
// num3 != true
```

>`Object`都反悔`true`，只有控对象`null`返回`false`
```js
function test(){
  let obj = {};
  let data = {
    name: 'Zzhiren'
  };
  let empty = null;
  if(obj){
    console.log('obj is true');
  }else{
    console.log('obj is false');
  }

  if(data){
    console.log('data is true');
  }else{
    console.log('data is false');
  }

  if(empty){
    console.log('empty is true');
  }else{
    console.log('empty is false');
  }
}

test();
// obj is true
// data is true
// empty is false
```

>`Undefined`返回`false`，`undefined`不同通过`==`与`true/false`进行判断
```js
function test(){
  let value;
  if(value){
    console.log('value is true');
  }else {
    console.log('value is false');
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
`注意：在进算术计算时，所有八进制和十六进制数都将转换成十进制数进行计算。`

#### 1. 浮点数值
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

#### 2. 数值范围
* 最大值：保存在Number.MAX_VALUE
* 最小值：保存在Number.MIX_VALUE

#### 3. NaN





















