# Vue面试题
## Vue生命周期
[示例代码](../example/001-Vue生命周期.html)
### beforeCreate 创建前状态
* `$data`未初始化 `undefined`
* `$el`未初始化 `undefined`

### created 创建结束状态
* `$data`已经初始化，可以访问`data`中的数据
* `$el`未初始化 `undefined`

### beforeMount 挂载前状态
* `$data`已经初始化，可以访问`data`中的数据
* `$el`已初始化，但是数据绑定还未进行，dom元素仍然为`<p>{{ message }}</p>`

### mounted 挂载结束状态
* `$el`赋值完成

### beforeUpdate 更新前状态/update更新结束状态
>控制台输入: `app.message = 'Update'`，值被修改后会触发`beforeUpdate/update`生命周期

### beforeDestroy 销毁前状态/destory 销毁结束状态
>vue销毁组件后组件的dom元素仍然存在，但是不受vue的控制，无法访问到当前组件的实例