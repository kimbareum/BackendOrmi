import re

def md_to_html(text):
    # 토글
    text = re.sub(r'(>+) (.*)', r'<blockquote>\1 \2</blockquote>', text)
    # 헤딩
    text = re.sub(r'### (.*)', r'<h3>\1</h3>', text)
    text = re.sub(r'## (.*)', r'<h2>\1</h2>', text)
    text = re.sub(r'# (.*)', r'<h1>\1</h1>', text)
    # 코드블럭
    if re.match('\t?```', text):
        text = re.sub(r'^\t?```.*', r'<pre><code>', text)
        text = re.sub(r'\t?```$', r'</code></pre>', text)
    text = re.sub(r'\t?`(.*)`', r'<pre><code>\1</code></pre>', text)
    # 볼드
    text = re.sub(r'[\*_]{2}(.*)[\*_]{2}', r'<strong>\1</strong>', text)
    # 이탤릭
    text = re.sub(r'[\*_]{1}(.*)[\*_]{1}', r'<em>\1</em>', text)
    # 취소선
    text = re.sub(r'~~(.*)~~', r'<del>\1</del>', text)
    # 이미지
    text = re.sub(r'!\[(.*)]\((.*)\)', r'<div><img src = "\2" alt:="\1" width = "100"></div>', text)
    # 링크
    text = re.sub(r'\[(.*)]\((.*)\)', r'<div><a href = "\2">\1</a></div>', text)
    # 순서 없는 리스트
    if re.match(r'[ \t]*[\*-]+[ \t]+', text):
        text = re.sub(r'^[ \t]*[\*-]+[ \t]+(.+)', r'<ul>\n<li>\1</li>', text)
        text = re.sub(r'[ \t]*[\*-]+[ \t]+(.+)', r'<li>\1</li>', text)
        text += '</ul>'
    # 순서 있는 리스트
    if re.match(r'[ \t]*\d+\.', text):
        text = re.sub(r'^[ \t]*\d+\.[ \t]+(.+)', r'<ol>\n<li>\1</li>', text)
        text = re.sub(r'[ \t]*\d+\.[ \t]+(.+)', r'<li>\1</li>', text)
        text += '</ol>'
    return text
    
    
name = 'markdown'

f1 = open(f'{name}.md', 'r' ,encoding='UTF8')
f2 =  open(f'{name}.html', 'w' ,encoding='UTF8')
text = f1.readlines()
temp = ''
flag = 0
for i in text:
    # 여러줄짜리 코드블럭 처리
    if re.match('\t?```', i):
        temp += i
        if flag == 1:
            f2.write(md_to_html(temp))
            temp, flag = '', 0   
        flag = 1
        continue
    if flag == 1:
        temp += i
        continue
    # 순서있는 리스트 처리
    if re.match(r'[ \t]*\d+\.', i):
        temp += i
        flag = 2
        continue
    if flag == 2:
        f2.write(md_to_html(temp))
        temp = ''
    # 순서없는 리스트 처리
    if re.match(r'[ \t]*[\*-]+[ \t]+', i):
        temp += i
        flag = 3
        continue
    if flag == 3:
        f2.write(md_to_html(temp))
        temp = ''
    #특이사항없을시
    f2.write(md_to_html(i))

f1.close()
f2.close()

# import re

# def md_to_html(name):
#     with open(f'{name}.md', 'r' ,encoding='UTF8') as f:
#         text = f.read()
#         # 토글
#         text = re.sub(r'(>+) (.*)', r'<blockquote>\1 \2</blockquote>', text)
#         # 헤딩
#         text = re.sub(r'### (.*)', r'<h3>\1</h3>', text)
#         text = re.sub(r'## (.*)', r'<h2>\1</h2>', text)
#         text = re.sub(r'# (.*)', r'<h1>\1</h1>', text)
#         # 코드블럭
#         text = re.sub(r'\t?`(.*)`', r'<pre><code>\1</code></pre>', text)
#         # 볼드
#         text = re.sub(r'[\*_]{2}(.*)[\*_]{2}', r'<strong>\1</strong>', text)
#         # 이탤릭
#         text = re.sub(r'[\*_]{1}(.*)[\*_]{1}', r'<em>\1</em>', text)
#         # 취소선
#         text = re.sub(r'~~(.*)~~', r'<del>\1</del>', text)
#         # 순서 없는 리스트
#         text = re.sub(r'\n[ \t]*[\*-]+[ \t]+(.+)', r'\n<ul>\n<li>\1</li>\n</ul>', text)
#         # 이미지
#         text = re.sub(r'!\[(.*)]\((.*)\)', r'<div><img src = "\2" alt:="\1" width = "100"></div>', text)
#         # 링크
#         text = re.sub(r'\[(.*)]\((.*)\)', r'<div><a href = "\2">\1</a></div>', text)
#     with open(f'{name}.html', 'w' ,encoding='UTF8') as f:
#         f.write(text)


# md_to_html(name = 'markdown')