class UserInfo(object):
    dataset = []

    def __init__(self, user_id, nickname, email_adress, phone_number, money, point):
        self.user_id = user_id
        self.nickname = nickname
        self.email_adress = email_adress
        self.phone_number = phone_number
        self.money = money
        self.point = point
        self.dataset.append(self)

    def __str__(self):
        return f"이름 : {self.nickname}, 소지금 : {self.money}, 포인트 : {self.point}"

    def buy(self, stuff):
        if stuff.price > self.money:
            print("잔액이 부족합니다")
        else:
            self.money -= stuff.price
            self.point += stuff.price // 10
            print(
                f'{self.nickname}님의 "{stuff.name}" 구매가 성공적으로 진행되었습니다.\n현재 잔액은 {self.money}원 이며, 포인트는 {self.point} 입니다.'
            )


user1 = UserInfo(
    "right", "right", "right.kim93@gmail.com", "010-xxxx-xxxx", 50000, 1000
)


class BookInfo(object):
    dataset = []

    def __init__(self, name, author, publisher, category, introduction, price):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.category = category
        self.introduction = introduction
        self.price = price
        self.dataset.append(self)

    def __str__(self):
        return f"{self.name}\n{self.author} · {self.publisher} · {self.category}\n{self.introduction[0:50]}.....\n{self.price}원"


book1 = BookInfo(
    "알아서 잘 딱 깔끔하고 센스있게 정리하는 GitHub 핵심 개념",
    "김진 외 15명",
    "사도출판",
    "개발/프로그래밍",
    "이제 막 개발자가 되기로 결심하고 공부를 하시는 분에게 GitHub은 하나의 허들이 됩니다. 그 허들을 좀 더 쉽게 넘겨드리고자 비영리 프로젝트로 해당 프로젝트를 시작하였습니다.\n이 책은 ‘30분 요약강좌 시즌4’ 무료 영상과 함께 출시되는 무료 책입니다. 영상을 함께 보면서 정리하는 책이니 제주코딩베이스캠프 YouTube나 인프런 등 30분 요약강좌 시즌4 영상과 함께 공부해 주세요.\n취지에 공감하여 참여해 주신 저자분들에게, 책이 나오기까지 힘써주신 위니브 직원분들에게 감사 인사를 올립니다.",
    0,
)
book2 = BookInfo(
    "책2",
    "작가2",
    "출판사2",
    "카테고리2",
    "책소개내용들2책소개내용들2책소개내용들2책소개내용들2책소개내용들2책소개내용들2책소개내용들2책소개내용들2",
    40000,
)

print(user1)
print(book1)
print(book2)
user1.buy(book2)
user1.buy(book2)
