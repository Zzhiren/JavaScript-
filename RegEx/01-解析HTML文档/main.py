import re
fo = open('./index.html', 'r+').read()


def find_song_li():
    pattern = r'(?<=<li>).*(?=<li>)'
    print(re.findall(pattern, fo))


find_song_li()
