// 给方法传入一个数组arr，返回一个数组，数组中包含重复的元素

/** 方法1：使用filter遍历数组，
 * indexOf从数组左端开始查询，找到元素后返回index
 * lastIndexOf从数组右端查询，找到元素后返回index
 * 然后判断两次index是否相同，不同则重复，然后判断临时数组temp中是否已经存在该元素，没有则push
 */
function fn1(arr) {
  var temp = []
  return arr.filter(function (item, index) {
    if (arr.lastIndexOf(item) !== index && temp.indexOf(item) < 0) {
      temp.push(item)
      return item
    }
  })
}

/**方法2：先排序，再比较
 * sort()方法排序数组，然后从第二个元素开始比较前一个元素，如果相同且临时数组中没有该元素，则push
 * 最后返回临时数组
 */
function fn2(arr) {
  var temp = []
  var i
  arr.sort()
  for (i = 1; i < arr.length; i++) {
    if (arr[i] === arr[i - 1] && temp.indexOf(arr[i]) < 0) {
      temp.push(arr[i])
    }
  }
  return temp
}

/**方法3：判断是否是第一个出现，且不是最后一个
 */
function fn3(arr){
  var temp = []
  var i
  for(i = 0; i < arr.length; i++){
    if(arr.indexOf(arr[i]) === i && arr.lastIndexOf(arr[i]) !== i){
      temp.push(arr[i])
    }
  }
  return temp
}