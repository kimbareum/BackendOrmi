while True:
    try:
        money = int(input("금액을 입력해 주세요. "))
    except:
        print("숫자만 입력해주세요.")
        continue
    if money>=0:
        break
    else:
        print("0 이상의 수를 입력해주세요.") 
money_type = (5000,1000,500,100)
money_num = []
for i in range(4):
    money_num.append(money//money_type[i])
    # money-=money_type[i]*money_num[i]
    money %= money_type[i]

print(f'5000원:{money_num[0]}장, 1000원:{money_num[1]}장,',
        f'500원:{money_num[2]}개, 100원:{money_num[3]}개')
