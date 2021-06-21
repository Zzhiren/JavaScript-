# [每周一例](./JavaScript/每周一例)
每周解决一个问题，问题可以是不懂的，理解模糊的，工作中遇到的需求等~

## 防抖`debounce`，节流`throttle`（完成）
### 1.什么是防抖和节流
大多数情况下函数在短时内只需要触发一次即可，但是由于用户操作问题短时间内大量触发函数导致，
而实际只需要第一次或者最后一次触发的结果，中间的函数触发没有意义，这就导致了性能浪费。

## Web元素拖动效果（待完成）

## Vue骨架屏（待完成）

# [正则表达式](./RegEx)

## 需要反复研究的文章
* [贪婪模式和非贪婪模式，涉及到匹配的原理。](https://www.cnblogs.com/admans/p/11955614.html)

## 贪婪模式和非贪婪模式
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

## 固化分组 (?>…)
固化分组内的字符串匹配成功后将不会被后续匹配规则进行回溯，相当于锁定。
