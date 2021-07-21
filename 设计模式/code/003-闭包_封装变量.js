function v1() {
  let mult = function () {
    let a = 1
    for (let i = 0, l = arguments.length; i < l; i++) {
      a = a * arguments[i]
    }

    return a
  }

  console.log('v1', mult(1,2,3,4))
}

function v2() {
  let cache = {}
  let mult = function () {
    let args = Array.prototype.join.call(arguments, ',')
    if (args in cache) {
      return cache[args]
    }
    let a = 1
    for (let i = 0, l = arguments.length; i < l; i++) {
      a = a * arguments[i]
    }

    return cache[args] = a
  }

  console.log('v2', mult(1,2,3,4,5))
}

function v3() {
  let mult = (function () {
    let cache = {}
    return function () {
      let args = Array.prototype.join.call(arguments, ',')
      if (args in cache) {
        return cache[args]
      }
      let a = 1
      for (let i = 0, l = arguments.length; i < l; i++) {
        a = a * arguments[i]
      }

      return cache[args] = a
    }
  })()
}

function v4() {
  let mult = (function () {
    let cache = {}
    let calculate = function () { // 封闭计算乘积函数
      let a = 1
      for (let i = 0, l = arguments.length; i < l; i++) {
        a = a * arguments[i]
      }
      return a
    }
    return function () {
      let args = Array.prototype.join.call(arguments, ',')
      if (args in cache) {
        return cache[args]
      }

      return cache[args] = calculate.call(null, arguments)
    }
  })()
}

v1()
v2()
v3()
v4()
