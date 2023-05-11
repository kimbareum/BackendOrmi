import xlsxwriter

# 엑셀 파일 생성
workbook = xlsxwriter.Workbook("./excel/test2.xlsx")

# 워크시트 생성
worksheet = workbook.add_worksheet("test")

title = ["이름", "국어", "영어", "수학", "평균"]
홍길동 = [33, 88, 24]
이호준 = [34, 66, 77]
김철수 = [78, 82, 36]
dic = {"홍길동": 홍길동, "이호준": 이호준, "김철수": 김철수}

for i in range(len(title)):
    worksheet.write(0, i, title[i])

for i, name in enumerate(dic, 1):
    worksheet.write(i, 0, name)
    for j in range(len(dic.get(name))):
        worksheet.write(i, j + 1, dic.get(name)[j])
    else:
        worksheet.write(
            i, len(dic.get(name)) + 1, sum(dic.get(name)) / len(dic.get(name))
        )

workbook.close()
