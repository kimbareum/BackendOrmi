class Blog(object):
    dataset = []

    def __init__(self, title, content, count, writer, create_day):
        self.title = title
        self.content = content
        self.count = count
        self.writer = writer
        self.create_day = create_day
        self.dataset.append(self)

    def __str__(self):
        return f"제목 : {self.title}, 내용 : {self.content[0:5]}..., 글쓴이 : {self.writer}"


게시글1 = Blog("오늘 제주의 날씨", "오늘 제주의 날씨는 참 좋네요! ~~", "0", "이호준", "2023/05/10")

게시글2 = Blog("오늘 부산의 날씨", "오늘 부산의 날씨는 좋네요! ~~", "10000", "김재현", "2023/05/10")

게시글3 = Blog("오늘 강원도의 날씨", "오늘 강원도의 날씨는 괜찮네요! ~~", "100", "남궁범", "2023/05/10")


print(게시글1)

for i in Blog.dataset:
    print(i.title)
    print(i.count)
    print(i.writer)
    print(i.create_day)
    print(i.content)
