function say() {
  let name = 'Jerry'
  return function () {
    console.log(`My name is ${name}`)
  }
}

let man = say()

man()
