## 조건 분기(CASE)

CASE WHEN 
	조건 
THEN 
	참일경우_실행구문 
ELSE 
	거짓일경우_실행구문 
END
-- 일반적인 구조

SELECT 
    CASE 
        WHEN floor = 1 THEN '1층 입니다.' 
        WHEN floor = 2 THEN '2층 입니다.'
        WHEN floor = 3 THEN '3층 입니다.'
        WHEN floor = 4 THEN '4층 입니다.'
    ELSE 
        '층수가 없어요' 
    END;
-- break 문이 필요가 없음. 하나만 실행하고 끝냄. 일반적인 if, elseif문을 이렇게 쓴다고 생각해도 괜찮음.

select
  extract(YEAR FROM created_at) as year,
  count(CASE WHEN gender = 'M' THEN gender END) AS male,
  count(CASE WHEN gender = 'F' THEN gender END) AS female,
  count(id) AS total
from users
group by year
order by year;
-- 가로로 펼쳐진 표를 만들고싶을때

### CASE 연습문제
연습문제 1. 주문정보(orders) 테이블에서 order_id, gender, gender_label(gender의 값에 따른 성별을 한글로 표시)을 해주세요.
필드명 : gender_label
gender가 F 이면 '여성'
gender가 M 이면 '남성'
결과로 표시할 필드
order_id
gender
gender_label
정렬순서 : order_id 오름차순

select
	order_id,
	gender,
	case 
		when gender = 'M' then '남성'
		when gender = 'F' then '여성'
	end as gender_label
from orders
order by order_id;

select
	order_id,
	gender,
	case gender
		when 'M' then '남성'
		when 'F' then '여성'
	end as gender_label
from orders
order by order_id;
-- 이런식의 사용도 경우에 따라서 가능함.


연습문제 2. 
회원(users) 테이블에서 다음 정보를 조회하세요.
1) 조회 항목
유저아이디 - id,
가입연도 - year
가입월 - month
가입일 - day
이용경로(traffic_source) 한글 텍스트 -  traffic_source_label
Search → 검색엔진
Organic → 검색결과
Email → 이메일
Display → 디스플레이 광고
Facebook → 페이스북
2) 정렬순서
id 오름차순

select 
	id,
	extract(year from created_at) as year,
	extract(month from created_at) as month,
	extract(day from created_at) as day,
	case
		when traffic_source = 'Search' then '검색엔진'
		when traffic_source = 'Organic' then '검색결과'
		when traffic_source = 'Email' then '이메일'
		when traffic_source = 'Display' then '디스플레이 광고'
		when traffic_source = 'Facebook' then '페이스북'
	end as traffic_source_label
from users
order by id;


연습문제 3.
SQL 연습문제 7-3
회원(users) 테이블에서 가입연도별 이용경로(traffic_source)별 가입자수를 조회하세요.
1) 조회 항목
year
Search
Organic
Email
Display
Facebook
Total
2) 정렬순서
year 오름차순

select 
	extract(year from created_at) as year,
	count(case when traffic_source = 'Search' then 'o' end) as Search,
	count(case when traffic_source = 'Organic' then 'o' end) as Organic,
	count(case when traffic_source = 'Email' then 'o' end) as Email,
	count(case when traffic_source = 'Display' then 'o' end) as Display,
	count(case when traffic_source = 'Facebook' then 'o' end) as Facebook
from users
group by year
order by year;