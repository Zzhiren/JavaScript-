# HTML/CSS总结
## margin合并问题
所有毗邻的两个或更多盒元素的margin将会合并为一个margin共享之。毗邻的定义为：同级或者嵌套的盒元素，并且它们之间没有非空内容、Padding或Border分隔。

## **1. position的值， relative和absolute分别是相对于谁进行定位的？**
* `absolute`: 生成绝对定位元素，相对于`static/initial`定位以外的第一个父元素进行定位。元素的位置通过 "left", "top", "right" 以及 "bottom" 属性进行规定。当父亲元素为`static/initial`时，子元素会再向外一层元素寻求定位，直到遇到position为`relative/sticky/fixed`时。[示例代码](../example/003-absoulte定位.html)
  
* `fixed`:（老IE不支持）生成绝对定位的元素，通常相对于浏览器窗口或  frame 进行定位，不占用文档流位置。元素的位置通过 "left", "top", "right" 以及"bottom" 属性进行规定。[示例代码](../example/004-fixed定位.html)
  
  **如果fixed元素不设置上面四个属性的话默认位置在前一个元素的下方，如果设置了该属性，元素将会相对于浏览器窗口或frame进行定位**。

  * **fixed1**: 设置里间距，所以会相对于浏览器窗口定位
  * **fixed2**: 未设置间距，默认处于文档流最后，当缩小浏览器高度后，fixed2将超出浏览器界面，且无法通过滚动浏览器来显示，因为fixed属性使dom不占用文档流，它将固定在浏览器边界之外的位置
  * **fixed3**: 不占用文档流，未设置间距，所以与box元素重叠，当浏览器高度变小可滚动时，滚动页面，fixed3将固定在该位置。
  


* `relative`: 生成相对定位的元素，相对于其在普通流中的位置进行定位。

* `static`: 默认值。没有定位，元素出现在正常的流中

* `sticky`: 生成粘性定位的元素，容器的位置根据正常文档流计算得出。在relative和fixed之间切换。当元素在文档的区域内表现为relative，当元素超出文档区域时为fixed。[示例代码](../example/005-sticky定位.html)

## 45个值得收藏的 CSS 形状
[网址](https://segmentfault.com/a/1190000018922732)