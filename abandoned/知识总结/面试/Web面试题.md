# 
## **一些开放性题目**
```javascript
1.自我介绍：除了基本个人信息以外，面试官更想听的是你与众不同的地方和你的优势。

2.项目介绍

3.如何看待前端开发？

4.平时是如何学习前端开发的？

5.未来三到五年的规划是怎样的？
```
  
## **如何解决跨域问题**
>JSONP:通过script标签来实现跨域请求

[示例代码](./example/004-jsonp跨域.html)

**原理**：浏览器拥有一个同源策略，同源策略就是发送请求的ip+port与服务端一致。而script标签不受该策略限制。所有我们通过包装一个script标签的方法来获取数据。

请求是可以，但是获取的数据该怎么拿到呢，这里我们就需要在url后一个callback参数具体如下：`&callback=funName`；后端会根据将数据包装成一个json对象通过funName(json)传回，具体后台怎么实现，我目前也没有弄明白，根据查询的资料默认情况下写成 `callback=funName`这种key=value的形式，其中的key:`callback`也可以后端自己定义，如定义成`returnJSON`，那此时我们的写法应该是 `returnJSON=funName`，funName可以由前端自己定义。
```js
/** 
 * @desc 封装jsonp
 * @param {String} url 请求地址
 * @param {Object} data 请求参数
 * @param {Function} success 回调函数
*/
function jsonp(obj){
  // 回调函数名称
  var callbackName = 'jsonp_callback_' + Date.now() + Math.random().toString().substr(2, 5);
  // 拼接url
  var arr = [];
  var params = '';
  for(var key in obj.data){
    arr.push(key+ '=' + obj.data[key])
  }
  params = arr.join('&');
  var url = obj.url + '?' + params + '&callback=' + callbackName;

  // 创建script标签
  var script = document.createElement('script');
  script.type='text/javascript';
  script.src=url;

  // 将script标签加入head标签中
  document.getElementsByTagName('head')[0].appendChild(script);

  // 将回掉函数挂载到window上，获取完数据后再删除
  window[callbackName] = function(res){
    obj.success(res);
    // 使用完在删除script标签
    delete window.callbackName;
    document.getElementsByTagName('head')[0].removeChild(script)
  }
}
```

## **封装Ajax**
[004-封装Ajax](./example/004-封装Ajax.html)

## **常见web安全及防护原理**
>SQL注入原理

通过把sql命令插入到Web表单或请求参数或url地址，最终达到欺骗服务器执行恶意的sql命令。

如何避免：
* 不要相信用户的输入，对用户的输入做校验，包括长度，类型等。
* 使用参数化的sql，通过判断参数来组装sql。
* 不要使用管理员权限来连接数据库，为每个应用使用单独权限和有限的数据库连接。
* 对机密和敏感信息加密处理。

## **说说TCP传输的三次握手四次挥手策略**

## **对前端模块化的认识**（待完善）
>AMD是`RequireJS`在推广过程中对模块定义的规范化产出。

>CMD是`SeaJS`在推广过程中对模块定义的规范化产出。

`AMD`是提前执行，`CMD`是延迟执行。

## **快速排序**
快速排序的原理

1. 在数据集中，找到中间值。 
2. 将小于中间值的数据放在左边数组，大于中间值的放在右边数组。
3. 通过递归将左边数组和右边数组执行`1 2`步。
```js
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  // 找到中间值，如果是浮点数，则向下取整
  var index = Math.floor(arr.length / 2);
  console.log(index)
  console.log(arr)
  var numValue = arr.splice(index,1);//找到中间数的值
  var left = [];
  var right = [];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] < numValue) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }
  // return quickSort(left).concat(numValue,quickSort(right));//递归不断重复比较
  return [...quickSort(left), numValue, ...quickSort(right)]
};

function start(){
  var arr = [100,200,300,88,99,1000,288,422,900];
  var result = quickSort(arr);
  document.getElementById('result').innerText=result;
};
```

## **JS闭包**
### 闭包的特性
* 函数内部可以应用外部的参数和变量。
* 参数和变量不会被垃圾回收机制回收。
* 设置私有方法和变量。
* 函数嵌套函数。
  
[006-闭包](./example/006-闭包.html)
```js
// 嵌套函数的闭包
function close(){
  var a = 0;
  console.log(`close${a}`);
  return function(){
    a++;
    console.log(a)
  }
};

let a = close();
let b = close();
// 按下列顺序执行
a() // 输出：1
a() // 输出：2
a() // 输出：3
b() // 输出：1
b() // 输出：2

```
>面试题：获取页面所有li标签，给所有li标签添加点击事件，每个li标签打印出自己的index[示例代码](006-闭包.html)



















