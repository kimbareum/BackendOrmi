import random

class Hero(object):

    def __init__(self, 이름, 레벨, 경험치, 공격력, 방어력, 체력, 마력, 크기_넓이, 크기_높이, x, y):
        self.name = 이름
        self.lv = 레벨
        self.exp = 경험치
        self.power = 공격력
        self.defence = 방어력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.x = x
        self.y = y
    
    def attack(self, mob):
        mob.hp -= self.power
        print(f'{self.name}이 {max(self.power,0)}의 데미지로 공격했습니다.\n{mob.name}의 체력이 {max(mob.hp,0)}이 되었습니다.')
        if mob.hp <= 0:
            if random.randint(1,100) <= mob.droprate:
                print(f'{mob.name}이 아이템을 드롭하고 사라졌습니다.')
            else:
                print(f'{mob.name}이 사라졌습니다.')


class Mob(object):
    
    def __init__(self, 이름, 공격력, 체력, 마력, 크기_넓이, 크기_높이, 아이템확률, x = 1, y= 1):
        self.name = 이름
        self.power = 공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.droprate = 아이템확률
        self.x = x
        self.y = y

    def __add__(self, next):
        if self.name == '슬라임':
            return Mob(이름 = f'왕{self.name+next.name}', 공격력 = self.power+next.power, 체력 = self.hp+next.hp, 마력 = self.mp+next.mp, 크기_넓이 = self.width+next.width, 크기_높이 = self.height+next.height, 아이템확률 = (self.droprate+next.droprate)//2)

    def attack(self, hero):
        hero.hp -= max(self.power-hero.defence,0)
        print(f'{self.name}이 {max(self.power-hero.defence,0)}의 데미지로 공격했습니다.\n{hero.name}의 체력이 {max(hero.hp,0)}이 되었습니다.')
        if hero.hp <= 0:
            print(f'{hero.name}이 죽었습니다.')

licat = Hero(이름 = 'licat', 레벨 = 1, 경험치 = 0, 공격력 = 10, 방어력 = 5, 체력 = 10000, 마력 = 20, 크기_넓이 = 2, 크기_높이 = 2, x = 1, y = 1)
mura = Hero(이름 = 'mura', 레벨 = 1, 경험치 = 0, 공격력 = 10, 방어력 = 5, 체력 = 5000, 마력 = 100, 크기_넓이 = 2, 크기_높이 = 2, x = 1, y = 1)

슬라임 = Mob(이름 = '슬라임', 공격력 = 1, 체력 = 10, 마력 = 10, 크기_넓이 = 2, 크기_높이 = 2, 아이템확률 = 100)
오크 = Mob(이름 = '오크', 공격력 = 10, 체력 = 10, 마력 = 10, 크기_넓이 = 2, 크기_높이 = 2, 아이템확률 = 80)
고블린 = Mob(이름 = '고블린', 공격력 = 100, 체력 = 10, 마력 = 10, 크기_넓이 = 2, 크기_높이 = 2, 아이템확률 = 60)
드래곤 = Mob(이름 = '드래곤', 공격력 = 1000, 체력 = 10, 마력 = 10, 크기_넓이 = 2, 크기_높이 = 2, 아이템확률 = 40)
해골 = Mob(이름 = '해골', 공격력 = 10000, 체력 = 10, 마력 = 10, 크기_넓이 = 2, 크기_높이 = 2, 아이템확률 = 1)

해골.attack(mura)
licat.attack(오크)
왕슬라임오크 = 슬라임+오크
왕슬라임오크.name