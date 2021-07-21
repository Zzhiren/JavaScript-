function demo() {
  console.log('demo')
  console.info(this)
  return function () {
    console.log('匿名函数this指向window')
    console.warn(this)
  }
}

function demo2() {
  console.log('demo2')
  console.info(this)
  return () => {
    console.log('匿名函数this指向window')
    console.warn(this)
  }
}

demo()()
demo2()()

function currying (fn) {
  var args = []

  return function () {
    if (arguments.length === 0) {
      return fn.apply(this, args)
    } else {
      [].push.apply(args, arguments)
      return arguments.callee
    }
  }
}

let cost = (function () {
  let money = 0
  return function () {
    for (let i = 0; i < arguments.length; i++) {
      money += arguments[i]
    }
    return money
  }
})()

cost = currying(cost)
cost(100)
cost(200)
cost(300)
console.log(cost())
