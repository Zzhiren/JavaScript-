/**实现函数 makeClosures，调用之后满足如下条件：
 * 1、返回一个函数数组 result，长度与 arr 相同
 * 2、运行 result 中第 i 个函数，即 result[i]()，结果与 fn(arr[i]) 相同 
 */

//  使用map
function makeClosures(arr, fn) {
  return arr.map(function (item) {
    return function (val) {
      // 定义函数体。立即执行，返回一个fn函数
      return function () {
        return fn(val)
      }
    }(item)
  })
}

// 使用for循环
function fn2(arr, fn) {
  var result = []
  var i
  for (i = 0; i < arr.length; i++) {
    // 使用一个立即执行函数，也就是匿名函数来访问当前的i
    result[i] = function (val) {
      //这里使用立即执行函数，使用当前的i，如果不适用立即执行函数生成的只是一个函数体，全部函数体的i都相等
      return function () {
        return fn(val)
      }
    }(arr[i])
  }
  return result
}

// 实现函数 functionFunction，调用之后满足如下条件：
// 1、返回值为一个函数 f
// 2、调用返回的函数 f，返回值为按照调用顺序的参数拼接，拼接字符为英文逗号加一个空格，即 ', '
// 3、所有函数的参数数量为 1，且均为 String 类型

function functionFunction(str) {
  return function(val){
      return str+', '+val
  }
}

// 已知函数 fn 执行需要 3 个参数。请实现函数 partial，调用之后满足如下条件：
// 1、返回一个函数 result，该函数接受一个参数
// 2、执行 result(str3) ，返回的结果与 fn(str1, str2, str3) 一致
//https://www.nowcoder.com/practice/fb2d46b99947455a897f2e9fe2268355?tpId=6&tqId=10973&tPage=2&rp=3&ru=%2Fta%2Fjs-assessment&qru=%2Fta%2Fjs-assessment%2Fquestion-ranking

function partial(fn, str1, str2) {
  return function(str3){
      return fn(str1,str2,str3)
  }
}