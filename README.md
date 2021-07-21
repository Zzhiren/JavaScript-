# 目录
* [每周一例](#1)
  * [防抖debounce，节流throttle](#1.1)
  * [Web元素拖动效果](#1.2)
  * [Vue骨架屏](#1.3)
* [正则表达式](#2)
  * [比较好的文章博客](#2.1)
  * [贪婪模式和非贪婪模式](#2.2)
  
---

# <span id='1'>1. [每周一例](./JavaScript/每周一例)</span>
每周解决一个问题，问题可以是不懂的，理解模糊的，工作中遇到的需求等~
* 防抖和节流（已完成）
* Web元素拖动效果（待完成）
* Vue骨架屏（待完成）

## <span id='1.1'>1.1 防抖`debounce`，节流`throttle`（完成）</span>
什么是防抖和节流？
>大多数情况下函数在短时内只需要触发一次即可，但是由于用户操作问题短时间内大量触发函数导致，
而实际只需要第一次或者最后一次触发的结果，中间的函数触发没有意义，这就导致了性能浪费。

## <span id='1.2'>1.2 Web元素拖动效果</span>

## <span id='1.3'>1.3 Vue骨架屏</span>

---

# <span id='2'>2. [正则表达式](./RegEx)</span>

## <span id='2.1'>2.1 比较好的文章博客</span>
* [贪婪模式和非贪婪模式，涉及到匹配的原理。](https://www.cnblogs.com/admans/p/11955614.html)

## <span id='2.2'>2.2 贪婪模式和非贪婪模式</span>
如下示例中贪婪与非贪婪模式区别是在匹配字符时

贪婪模式
> 贪婪模式会匹配最大长度的字符串

```python
# 第一版 查找出《以父之名》
# 开头 <div id="001" class="box">
# 结尾 </div>
def find_yfzm():
    print('找出以父之名歌曲')
    pattern = r'(?<=<div title="以父之名" class="box">)[\s\S]*(?=</div>)'
    print(pattern)
    print(re.findall(pattern, fo))
```

非贪婪模式
> 非贪婪模式匹配最小长度的字符串
```python
def find_yfzm():
    print('找出以父之名歌曲')
    pattern = r'(?<=<div title="以父之名" class="box">)[\s\S]*?(?=</div>)'
    print(pattern)
    print(re.findall(pattern, fo))
```

# <span id='2.3'>2.3 固化分组 (?>…)</span>
固化分组内的字符串匹配成功后将不会被后续匹配规则进行回溯，相当于锁定。
