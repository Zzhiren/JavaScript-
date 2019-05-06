# JS面试题
## 箭头函数的this指向
[参考文章](https://www.cnblogs.com/dongcanliang/p/7054176.html)
>箭头函数的this指向当前函数所在的上下文的this值
```js
// 箭头函数会捕获Person的上下文当作自己的this
function Person(){
  this.age = 10
  setTimeout(()=>{
    this.age++
  },2000)
}
```

## 闭包
* 函数内部可以应用外部的参数和变量
* 参数和变量不会被垃圾回收机制回收

## 阻止冒泡事件