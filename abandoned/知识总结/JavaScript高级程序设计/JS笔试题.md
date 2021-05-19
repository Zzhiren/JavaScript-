<!-- TOC -->

- [**JS笔试题**](#js%e7%ac%94%e8%af%95%e9%a2%98)
  - [下面函数的最终打印顺序](#%e4%b8%8b%e9%9d%a2%e5%87%bd%e6%95%b0%e7%9a%84%e6%9c%80%e7%bb%88%e6%89%93%e5%8d%b0%e9%a1%ba%e5%ba%8f)

<!-- /TOC -->

# **JS笔试题**
## 下面函数的最终打印顺序
>setTimeout的时间参数最低为`4ms`，浏览器会将`0`改为`4ms`；js为单线程执行，当第一个`setTimeout`为延时执行后，js会立即执行后面的代码，此时执行到`new Promise`，其中的`a`和`b`方法就是`promise`的两个回调`resolve`（成功后执行的方法，then）和`reject`（错误后执行的方法catch），
```js
function test() {
  setTimeout(function(){
      console.log(1)
  }, 0);
  new Promise(function(a, b){
      setTimeout(function(){
          for(var i=0; i< 10 ; i++){
            i == 9 && a()
          }
      }, 2000);
      console.log(2)
  }).then(function(){
    console.log(3)
  })catch(function(){
  });
  console.log(4)
}
// 2,4,1,3

function test2(){
  setTimeout(function(){
      console.log(1)
  }, 0);
  console.log(2)
}
```