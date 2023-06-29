## 필터링
### WHERE : 필터를 걸기

SELECT * FROM users WHERE first_name = 'Michael'

### 논리연산자
=
>
<
>=
<=
!=
<>

AND, OR, NOT

SELECT * 
FROM users 
WHERE age > 30 
and country = 'Brasil'

괄호
SELECT * 
FROM users 
WHERE first_name = 'David'
and (age < 20 or age > 60)


### BETWEEN A AND B 
(A와 B 사이, 이상 이하 관계.)

select * 
from users
where age>=20 and age<=30

select * 
from users
where age between 20 and 30

select *
from users
where created_at between '2020-01-01' and '2020-01-31'
(날짜에서도 사용 가능한데, 이렇게 쓰면, 뒤에 있는날의 00시 기준으로 끊겨서 이 경우 1월 30일까지만 잡힘)


### IN : 파이썬의 in과 같음.

select * 
from products
where brand in ('Onia', 'Hurley', 'Matix');


### LIKE : 해당 문자열이 포함된 레코드를 조회. 정규표현식 사용 가능.
% => 개수제한없이 모든 문자
_ => 한글자짜리 모든 문자.

select * 
from products
where name like '%Young%'
=> name에 Young이 들어있기만 하면 조회

select * 
from products
where name like 'Hurley%';
=> name이 Hurley로 시작하는 애만 조회

select * 
from products
where name like '%T-shirt';
=> name이 T-shirt로 끝나는 애만 조회

select distinct first_name
from users
where first_name like 'Da___'
=> Da로 시작하고 총 5글자인 애를 조회.


### IS NULL : 값이 비어있는지 확인. false가 아니라 아예 할당이 되지 않은거만 찾음.
IS NOT NULL.


### 필터링 연습문제
연습문제 1. 상품정보(products) 테이블에서 카테고리(category)가 ‘Swim’ 인 레코드의 모든 항목를 조회하세요.

select *
from products
where category = 'Swim';

연습문제 2. 상품정보(products) 테이블에서 브랜드(brand)가 ‘2EROS’인 레코드의 id, 비용(cost), 브랜드(brand)를 조회하세요.

select id, cost, brand
from products
where brand = '2EROS';

연습문제 3. 상품정보(products) 테이블에서 비용(cost)이 30이하이고 상품대상, 구분, 분야(department)이 ‘Men’인 모든 레코드를 10개를 조회하세요.

select *
from products
where cost <= 30 and department = 'Men'
limit 10

연습문제 4.상품정보(products) 테이블에서 판매가격(retail_price)이 40이상인 레코드들의 카테고리(category) 속성값을 중복제거(distinct)하여 조회하세요.

select distinct category
from products
where retail_price >= 40;

연습문제 5. 상품정보(products) 테이블에서 비용(cost)이 50이상이고 70이하인 모든 레코드들 조회하세요.

select *
from products
where cost between 50 and 70

연습문제 6. 상품정보(products) 테이블에서 상품명(name)에 ‘Men’과 ‘Sport’ 두 단어가 들어간 모든 레코드들 조회하세요.

select *
from products
where 
name like '%Men%' and 
name like '%Sport%';

연습문제 7.상품정보(products) 테이블에서 브랜드(brand)가 ‘TYR’이 아니고, 이름(name)에 ‘Suit’가 포함되고, 할인율이 50이상인 모든 레코드와 할인율을 조회합니다. 할인율의 컬럼 이름은 sale_price로 표현합니다.
할인율 : (비용/판매비용)*100

select 
    *,
    (cost/retail_price)*100 as sale_price
from products
where
    brand != 'TYR' and
    name like '%Suit%' and
    (cost/retail_price)*100 >= 50;



## 집계함수

### 일반 계산
COUNT : 데이터의 갯수를 반환.

select count(id)
from users;
=> 아이디의 개수를 반환. 종류의 개수가 아님.

select count(*)
from users;
=> NULL 값을 포함해서 세줌. *이 아니라 특정 칼럼을 넣으면 NULL은 제외하고 세줌.

select count(distinct city)
from users;
=> city의 종류의 개수를 반환

SUM : 합계를 반환.
AVG : 평균을 반환.
MAX : 최대값을 반환.
MIN : 최소값을 반환.
VARIANCE : 분산을 반환.
STDDEV: 표준편차를 반환.

select sum(retail_price)
from products;
=> products에서 판매가격의 합계를 구함



### GROUPBY : 특정 항목을 기준으로 그룹화하여 조회.(쪼갠다?)

select country, count(id) 
from users
group by country;
=> 각 country의 id의 개수를 반환. country 와 group by id 로우의 갯수가 같으니까 select 할 수 있음.

select country, city, count(id) 
from users
group by country, city;
=> 각 country의 city의 id의 개수를 반환. grouping 한 값만 select에 넣을 수 있음.

select 
	category, 
	sum(retail_price) as sum_retail_price  
from products
group by category
=> 카테고리 별 상품 판매가 합계


### 연습문제

연습문제 1. 회원(users) 테이블에서 전체 유저의 평균연령을 조회하세요.

select avg(age) as avg_age
from users;

연습문제 2. 회원(users) 테이블에서 여성 유저의 평균연령을 조회하세요.

select avg(age) as female_avg_age
from users
where gender = 'F';

연습문제 3. 회원(users) 테이블에서 국가별 가입자수를 조회하세요.

select
	country,
	count(id) as country_user_count
from users
group by country;

연습문제 4. 회원(users) 테이블에서 남성 유저의 국가별 가입자 수를 조회하세요.

select
	country,
	count(id) as country_male_count
from users
where gender = 'M'
group by country;

연습문제 5. 회원(users) 테이블에서 가입기간(created_at)이 2020년도 1월인 유저의 국가별 가입자 수 (country_user_count)를 조회하세요.

select
	country,
	count(id) as country_user_count
from users
where created_at between '2020-01-01' and '2020-02-01'
group by country;

연습문제 6. 회원(users) 테이블에서 가입기간(created_at)이 2020년도 1월인 유저의 국가별 성별 가입자 수(country_gender_user_count)를 조회하세요.

select
	country,
	gender,
	count(id) as country_gender_user_count
from users
where created_at between '2020-01-01' and '2020-02-01'
group by country, gender;

연습문제 7. 주문정보(orders) 테이블에서 주문생성일이 2022년도인 주문중에서 주문 상태가 환불(Returned)상태인 주문을 기준으로 유저 아이디(user_id)별 총 주문 아이템(num_of_item)의 합계를 조회하세요.

select
    user_id,
    sum(num_of_item) as sum_of_items
from orders
where 
	status = 'Returned' and 
	created_at between '2022-01-01' and '2023-01-01'
group by user_id;


### HAVING
GROUP BY 에 조건을 부여

select 
  country, 
  count(id) as user_count
from users
group by country
having count(id) >= 4000;

=> country에 따라 그룹화 한 후, 그룹내 row의 갯수가 4000개 이상인것만 필터링.

### ORDER BY
출력 결과 정렬. 기본값은 오름차순.

select * 
from users
order by age asc;
=> 나이 오름차순 정렬

select * 
from users
order by age desc;
=> 나이 내림차순 정렬

select * 
from users
order by age desc, id asc;
=> 1차로 나이 내림차순, 2차로 id 오름차순 정렬

select * 
from users
order by age asc
limit 3;
=> 나이가 제일 어린 3명의 유저 정보 조회

### HAVING, ORDER BY 연습문제

연습문제 1. 회원 테이블(users)에서 국가별 유저수를 조회하세요. 
- 조회 항목 : 국가명(country), 국가별 유저수(user_count)
- 조건 : 국가의 유저수가 3000명 이상인 국가
- 정렬 : 국가별 유저수 많은순으로 정렬

select 
	country,
	count(id) as user_count
from users
group by country 
having count(id) >=  3000
order by user_count desc;

연습문제 2. 상품정보(products) 테이블에서 여성 스웨터중 판매가격이 제일 저렴한 5개를 조회하세요.
- 조건
    - category : Sweaters
    - department : Women
- 정렬 : 판매가격(retail_price)이 낮은 순
- 갯수제한 : 5개

select *
from products
where 
	category = 'Sweaters' and 
	department = 'Women'
order by retail_price
limit 5;

연습문제 3. 상품정보(products) 테이블에서 여성 스웨터의 브랜드별 평균 판매가격이 100이하인 브랜드의 브랜드 이름과 여성스웨터 평균판매가격을  조회하세요.
- 조건
    - category : Sweaters
    - department : Women
- 그룹조건 : 평균 판매가격이 100 이하
- 정렬순서 : 평균 판매가격이 낮은 순

select 
	brand,
	avg(retail_price) as avg_ratail_price
from products
where 
	category = 'Sweaters' and 
	department = 'Women'
group by brand 
having avg(retail_price) <= 100
order by avg_ratail_price;


연습문제 4. 상품정보(products) 테이블에서 각 제품의 id, 이름, 카테고리, 브랜드, 비용(cost), 판매가(retail_price), 이익금액(profit), 이익율(profit_rate)을 조회하세요.
- 이익금액(profit) : 판매가(retail_price) - 비용(cost)
- 이익율(profit_rate) : (판매가(retail_price) - 비용(cost)) / 판매가(retail_price) * 100

select 
	id, 
	name, 
	category, 
	brand, 
	cost, 
	retail_price,
	retail_price - cost as profit,
	(retail_price - cost) / retail_price * 100 as profit_rate
from products;


연습문제 5. 상품정보(products) 테이블에서 수영카테고리 제품의 각 브랜드별 최소이익율, 최대 이익율, 평균 이익율을 조회하세요.
- 조건
    - category : Swim
- 이익율(profit_rate) : (판매가(retail_price) - 비용(cost)) / 판매가(retail_price) * 100

select
	brand,
	min((retail_price - cost) / retail_price * 100) as min_profit_rate,
	max((retail_price - cost) / retail_price * 100) as max_profit_rate,
	avg((retail_price - cost) / retail_price * 100) as avg_profit_rate
from products
where category = 'Swim'
group by brand;


연습문제 6. 연습문제 5의 데이터에서 평균이익율이 높은 TOP 5 브랜드와 평균이익율을 조회하세요.

select
	brand,
	avg((retail_price - cost) / retail_price * 100) as avg_profit_rate
from products
where category = 'Swim'
group by brand
order by avg_profit_rate desc
limit 5;

연습문제 7. 상품정보(products) 테이블에서 카테고리 별 남성 제품의 수를 조회하세요. 단, 카테고리 중 ‘Sport’가 들어가지 않은 카테고리만 조회하시오.

select 
	category,
	count(id) as men_product_count
from products
where 
	department = 'Men' and
	category not like '%Sport%'
group by category 

select 
	category,
	count(id) as men_product_count
from products
where department = 'Men'
group by category 
having category not like '%Sport%'


## 쿼리문의 작성 순서.

1. from
2. where
3. group by
4. having
5. select
6. order by
7. limit