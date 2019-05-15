# **JS面试题**
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

## 前端跨域解决方案
### 通过修改document.domain来跨子域
>将子域和主域的document.domain设为同一个主域，前提条件：这两个域名必须属于同一个基础域名，而且所用的协议、端口都需要一致
```js
// 浏览器打开 id.qq.com
// 控制台输入如下内容
document.domain // 'id.qq.com'
var w = window.open('http://qq.com')

// 在id.qq.com的控制台输入如下命令
document.domain = 'qq.com'
w.document // 打印出http://qq.com的dom结构
```

### 使用window.name来进行跨域
* window.name可以存储不超过2M的数据，数据格式按需自定义。
* 浏览器的每个tab窗口关闭之前，加载不同的网页window.name不会改变，如果a.html改变了window.name，再加载b.html后且不改变window.name，window.name仍然为a.
[示例代码](../example/006-使用window.name跨域.html)

```js
/**
* @desc 通过iframe获取跨域数据
* @param {String} url 需要跨域的地址
* @param {Function} 获取数据后的回调
*/
function getIframeData(url, success){
  let iframe = document.createElement('iframe');
  iframe.src=url;
  iframe.frameBorder = 0;
  iframe.id = 'iframe';
  // 让iframe标签内容不影响当前页面
  iframe.style.position = 'absoulte';
  iframe.style.top = '-99999px';
  iframe.style.width = 0;
  iframe.style.height = 0;
  iframe.onload = load;
  document.body.appendChild(iframe);

  function load (){
    let window = iframe.contentWindow;
    let value = window.name;
    document.body.removeChild(iframe); // 取完数据后删除该标签
    success(value)
  }
}
```

### 使用HTML5中新引进的window.postMessage方法来跨域传送数据


