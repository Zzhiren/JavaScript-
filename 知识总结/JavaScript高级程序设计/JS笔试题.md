<!-- TOC -->

- [**JS笔试题**](#js%E7%AC%94%E8%AF%95%E9%A2%98)
  - [下面函数的最终打印顺序](#%E4%B8%8B%E9%9D%A2%E5%87%BD%E6%95%B0%E7%9A%84%E6%9C%80%E7%BB%88%E6%89%93%E5%8D%B0%E9%A1%BA%E5%BA%8F)

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