// 找出对象 obj 不在原型链上的属性(注意这题测试例子的冒号后面也有一个空格~)
// 1、返回数组，格式为 key: value
// 2、结果数组不要求顺序

// 通过getOwnPropertyNames获取对象自身属性，返回对象名数组
// 一个对象，其自身的可枚举和不可枚举属性的名称被返回。
function fn1(obj) {
  return Object.getOwnPropertyNames(obj).map(function (key) {
    return key + ': ' + obj[key]
  })
}

// 方法2：通过改变原型链，然后遍历对象属性
function fn2(obj){
  obj.__proto__ = null
  var arr = []
  for(var key in obj){
    var str = key+': '+obj[key]
    arr.push(str)
  }
  return arr
}