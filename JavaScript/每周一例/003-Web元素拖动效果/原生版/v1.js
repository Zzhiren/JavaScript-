function setDrag() {
  console.log('setDrag')
  let el = document.getElementById('drag_1')
  let x = 0
  let y = 0
  el.ondrag = function (e) {
    console.log('ondrag', e)
    if (e.clientX !== 0) {
      el.style.left = e.clientX + 'px'
      el.style.top = e.clientY + 'px'
    }
  }

  el.ondragstart = function (e) {
    console.log('ondragstart', e)

  }

  el.ondragend = function (e)  {
    console.log('ondragend', e)
    // if (e.clientX !== 0) {
    //   el.style.left = e.clientX + 'px'
    //   el.style.top = e.clientY + 'px'
    // }
  }
}

function dragStart(e) {
  console.log('dragStart', e)
}

function ondrag(e) {
  console.log('ondrag', e)
}

function ondragend(e) {
  console.log('ondragend', e)
}

setDrag()
