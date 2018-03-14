// 获取 url 中的参数
// 1. 指定参数名称，返回该参数的值 或者 空字符串
// 2. 不指定参数名称，返回全部的参数对象 或者 {}
// 3. 如果存在多个同名参数，则返回数组
// http://www.nowcoder.com?key=1&key=2&key=3&test=4#hehe
// [1, 2, 3]
function getUrlParam(sUrl, sKey) {
  var arr = []
  var temp = []
  var obj = {}
  if(sKey === '' || sKey === null){
      temp = sUrl.split('?')[1].split('&') //['key=1','key=2','key=3','test=4#hehe']
      for(var i= 0 ; i<temp.length;i++){
        var middle = temp[i].split('=')
        var one = middle[0]
        obj[one] = middle[1]
        console.log(middle)
      }
      return obj
  }
}