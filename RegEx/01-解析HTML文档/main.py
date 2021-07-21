import re
fo = open('./index.html', 'r+').read()


# 查找出歌名列表
def find_song_name_list():
    # pattern = r'.'
    print('查找歌名列表')
    pattern = r'(?<=<li>).*(?=</li>)'
    print(pattern)
    print(re.findall(pattern, fo))


find_song_name_list()


# 第一版 查找出《以父之名》
# 开头 <div id="001" class="box">
# 结尾 </div>
def find_yfzm():
    print('找出以父之名歌曲')
    pattern = r'(?<=<div title="以父之名" class="box">)[\s\S]*?(?=</div>)'
    print(pattern)
    print(re.findall(pattern, fo))


find_yfzm()
