student_score = {
		'홍의': 97,
		'원희': 60,
		'동해': 77,
		'변수': 79,
		'창현': 89,
}
print(f'총점 : {sum(student_score.values())}')
print(f'평균 : {sum(student_score.values())/len(student_score)}')
# max_student = max(student_score,key=lambda x: student_score[x])
max_student = max(student_score,key=student_score.get)
min_student = min(student_score,key=student_score.get)
print(f'점수가 가장 높은 학생 : {max_student} / {student_score[max_student]}점')
print(f'점수가 가장 낮은 학생 : {min_student} / {student_score[min_student]}점')

like = ['볶음밥', '라면', '국수', '파스타', '치킨', '짜장면', '국밥']
dislike = ['국밥', '짬뽕', '찜닭', '파스타', '국수', '카레', '덮밥']

final_like = list(set(like) - set(dislike))
print(final_like)