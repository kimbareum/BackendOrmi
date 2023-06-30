### GROUP BY ROLLUP(조건)

- group당 총계를 만들어줌.
- 여러 그룹이면 그 그룹당 단계를 다 보여줌.

## WINDOW 함수

- 각 row별로 연관되어 있는 데이터를 뽑고 그를 바탕으로 계산을 할 수 있는 함수
- 윈도우 함수는 행 그룹의 값을 계산하고 각 행마다 하나의 결과를 반환
- 누적합계를 구하거나 할 수도 있음

- window함수() OVER ( 조건(ㅖPARTITION BY, ORDER BY, WINDOWING) ) 식으로 사용.

### 분류

- 그룹 내 순위 관련 함수(RANKING FAMILY)
    - RANK, DENSE_RANK, ROW_NUMBER
- 그룹 내 집계 관련 함수(WINDOW AGGREGATE FAMILY)
    - SUM, MAX, MIN, AVG, COUNT
- 그룹 내  행 순서 관련 함수
    - LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE
- 그룹 내 비율 관련 함수
    - CUME_DIST, PERCENT_RANK, NTILE


## RANK, DENSE_RANK, ROW_NUMBER, PERCENT_RANK
- 그룹내 순위를 매기는 함수들.
- 형태 : RANK() OVER ( PARTITION BY (컬럼명, 식) ORDER BY (컬럼명, 식) )
- order by로 순위를 매길 조건을 선택하고, 파티션으로 추가적으로 분류해서 순위를 매길 수 있음.
- 동일 값인 경우 동일 순위가 부여, 다음 순위는 동일값의 수만큼 건너뛰어 부여.
- DENSE_RANK : 동일 값인 경우 동일 순위가 부여, 다음 순위는 그냥 다음 번호로 지정하는 rank.
- ROW_NUMBER : 동일 값이라도 순서대로 순위를 매김.
- PERCENT_RANK : 0-1까지의 백분율 값으로 순위를 매김.

```sql
select 
  id,
  first_name,
  last_name,
  country,
  age,
  RANK() OVER ( PARTITION BY country ORDER BY age ) AS rank_number_in_country
from users
where id between 1 and 20
order by country, age
```

## 탐색함수

### LAG, LEAD
- 바로 이전(LAG) 또는 바로 이후(LEAD) 의 데이터를 읽고, 그를 기준으로 계산.

### FIRST_VALUE, LAST_VALUE, NTH_VALUE(칼럼, 위치)
- 첫번째 값과 마지막 값(현재까지 살펴본 범위의 마지막값), N번째 위치의 값을 가져오는 함수.
- 윈도우함수는 제일 앞에서 자기위치까지가 현재 윈도우범위로 잡힘.
- 이상하긴 한데 누적합같은걸 구할때는 유용함.
- 방지하려면 windowing 사용.

```sql
ROWS BETWEEN UNBOUNDED PRECEDING -- 시작위치
    AND 
UNBOUNDED FOLLOWING -- 끝위치
CURRENT ROW -- 내위치
N PRECEDING -- 내 위치부터 N만큼 앞까지
N FOLLOWING -- 내 위치부터 N만큼 뒤까찌
```

### CUME_DIST()
- 누적분포. 내 앞에 있는 값이 몇개인지 0-1사이 값으로 표기.

```
1000 -> 0.2 
1200 -> 0.6
1200 -> 0.6
1400 -> 0.8
2000 -> 1.0
이런식으로.
```

### NTILE(숫자)
- 숫자만큼의 통을 만들고, 그 안에 순서대로 나눠서 넣음(1번박스부터 채워나가는 식).
- 들어가는 갯수가 딱 나눠지지 않으면 앞에서부터 1개씩 더 들어감.

## 집계 분석 함수

- SUM, AVG, MAX, MIN, COUNT 등 뒤에 OVER 붙여서 똑같이 사용 가능.