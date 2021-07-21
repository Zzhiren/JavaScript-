/**
 * @desc debounce防抖函数
 * @param {function} func - 需要防抖的函数
 * @param {number} wait - 延时的毫秒数
 * @param {boolean} immediate - 是否立即执行
 * @returns {function(): *}
 */
export function debounce(func, wait= 1000, immediate= false) {
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
        result = func.apply(context, arguments)
      }
    } else {
      timer = setTimeout(() => {
        func.apply(context, arguments)
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

/**
 * @desc 节流函数 leading和trailing不可同时使用
 * @param {function} func - 需要防抖的函数
 * @param {number} wait - 延时的毫秒数
 * @param {object} options
 * @param {boolean} options.leading - true 立即执行
 * @param {boolean} options.trailing - true 停止后是否执行
 * @returns {function(): *}
 */
export function throttle(func, wait, options = { leading: true, trailing: true }) {
      let context
      let timer
      let args
      let previous = 0

      let later = function () {
        previous = options.leading === false ? 0 : new Date().getTime()
        timer = null
        if (!timer) func.apply(context, args)
      }

      let throttled = function () {
        context = this
        args = arguments
        // 立即执行的
        let now = +new Date()
        if (!previous && options.leading === false) previous = now;
        // now - previous 为上一次触发到这一次触发的间隔
        // 如果这个间隔小于 wait 等待时间，则不会触发fun
        let remaining = wait - (now - previous)
        // 等待时间 wait 对比前后两次触发的间隔时间
        // remaining > wait 排除修改系统时间
        if (remaining <= 0 || remaining > wait) {
          if (timer) {
            clearTimeout(timer)
            timer = null
          }
          previous = now
          console.log('stamp')
          if (!timer) func.apply(context, args)
        } else if (!timer && options.trailing !== false) {
          // 当前后间隔时间小于 wait时间时，走 定时器流程，
          // 因为在 wait时间内可能停止触发了，所以停止后还可以触发一次
          console.log('timer')
          timer = setTimeout(later, remaining)
        }
      }

      throttled.cancel = function() {
            clearTimeout(timeout);
            previous = 0;
            timer = null;
      }

      return throttled
    }
