skill = [
        ('고기잡이', (1, 100, 'S')),
        ('고기팔기', (1, 100, 'A')),
        ('낚시', (2, 100, 'A')),
        ('통발', (2, 100, 'B')),
        ('큰그물', (2, 100, 'S'))
]

for name,(level_limit, point, rank) in skill:
    print(f'축하합니다. {rank}등급의 skill {name}을(를) 습득하셨습니다!\n\
해당 스킬은 레벨 제한 {level_limit}에 스킬 포인트 {point}입니다.')