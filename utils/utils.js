/**
 * @desc debounce防抖函数
 * @param {function} fun - 需要防抖的函数
 * @param {number} wait - 延时的毫秒数
 * @param {boolean} immediate - 是否立即执行
 * @returns {function(): *}
 */
export function debounce(fun, wait= 1000, immediate= false) {
  let timer
  let result
  let debounced = function () {
    const context = this
    if (timer) {
      clearTimeout(timer)
    }
    if (immediate) {
      let callNow = !timer
      timer = setTimeout(() => {
        timer = null;
      }, wait)
      if (callNow) {
        result = fun.apply(context, arguments)
      }
    } else {
      timer = setTimeout(() => {
        fun.apply(context, arguments)
      }, wait)
    }

    return result
  }
  debounced.cancel = function () {
    clearTimeout(timer)
    timer = null
  }

  return debounced
}
