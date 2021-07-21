/**
 * @desc 模拟 new 的过程
 */
function Person(name) {
  this.name = name;
}

Person.prototype.getName = function () {
  return this.name;
}

let objectFactory = function () {
  let obj = new Object();
  let Constructor = [].shift.call(arguments); // 取得外部传入的构造函数
  obj.__proto__ = Constructor.prototype;
  let result = Constructor.apply(obj, arguments); // 借用外部传入的构造器给obj设置属性
  return typeof  result === 'object' ? result : obj; // 确保构造器总是会返回一个对象
}

let a = objectFactory(Person, 'Tom')
let b = new Person('Jerry')

console.log('a:')
console.log(a.name)
console.log(a.getName())
console.log(Object.getPrototypeOf(a) === Person.prototype)

console.log('\nb:')
console.log(b.name)
console.log(b.getName())
console.log(Object.getPrototypeOf(b) === Person.prototype)
