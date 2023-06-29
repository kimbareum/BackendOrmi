## JOIN
- 옆으로 붙이는것

### JOIN의 종류
INNER JOIN : A, B 모두 있는것만. 둘다있는 항목이 아니면 보여주지 않음.(회원정보가 삭제되었는데 주문내역이 있는 경우, 주문내역도 보여주지 않음.)

OUTER JOIN
    LEFT JOIN : A에 있는것은 무조건 보여줌 + B에있는것중 A에도 있는것
    RIGHT JOIN : LEFT 의 반대
    FULL OUTER JOIN : 모든 데이터를 전부 JOIN

CROSS JOIN : 두 테이블에서 가능한 모든 조합을 표현해줌
    A   B   => cross join
    1   a      1a 1b 1c 1d
    2   b      2a 2b 2c 2d
    3   c      3a 3b 3c 3d
    4   d      4a 4b 4c 4d

### 업무 데이터의 종류

- 트랜잭션 데이터
    - 일상적인 프로세스를 진행할때 생성되는 데이터(주문정보 등)
    - 계속해서 쌓이고 변경되지 않음.

- 마스터 데이터
    - 트랜잭션에서 참고되는 각종 정보(회원정보, 상품정보 등)

- 분석데이터
    - join하거나 아무튼 가공한 데이터.
    - join할 떄는 보통 트랜잭션에디터 기준으로 마스터데이터를 옆에 붙여나감.


### JOIN 연습문제
```sql
-- 연습문제 1.
-- 회원(users) 테이블과 주문정보(orders) 테이블을 이용하여 모든 주문내역에 회원정보를 표시하세요.
-- - 조회 항목 :
--     - 주문ID(order_id)
--     - 주문한 상품 수량(num_of_item)
--     - 회원 이름(first_name, last_name)
--     - 주소(street_address)
--     - 우편번호(postal_code)
--     - 도시(city)
--     - 국가(country)

select 
	o.order_id,
	o.num_of_item,
	u.first_name,
	u.last_name,
	u.street_address,
	u.postal_code,
	u.city,
	u.country
from orders as o
left join users as u on o.user_id = u.id;
```
연습문제 2.
회원(users) 테이블과 주문정보(orders) 테이블을 이용하여 상품을 주문한 회원의 국가가 ‘United States’이면서 주문 상태가 처리중(Processing)인 정보를 조회하시오. 
- 조회 항목
    - 주문ID(order_id)
    - 회원 이름(first_name, last_name)
    - 주소(street_address)
    - 우편번호(postal_code)
    - 도시(city)
    - 국가(country)
    - 주문한 상품 수량(num_of_item)
- 조건 : 국가가 ‘United States’이면서 주문 상태가 처리중(Processing)

select 
	o.order_id,
	o.num_of_item,
	u.first_name,
	u.last_name,
	u.street_address,
	u.postal_code,
	u.city,
	u.country
from orders as o
left join users as u on o.user_id = u.id
where 
	u.country = 'United States' and 
	o.status = 'Processing'

연습문제 3.
회원(users) 테이블과 주문정보(orders) 테이블을 이용하여 국가별 총 상품 주문주(total_order_count)을 조회하시오.
- 조회 항목 : 국가명(country), 국가별 총 상품 주문주(total_order_count)
- 정렬 : 국가별 총 상품 주문주(total_order_count)이 많은 순으로 정렬

select 
	u.country,
	count(o.order_id) as total_order_count
from orders as o
join users as u on o.user_id = u.id
group by u.country 
order by total_order_count desc;


연습문제 번외.


select 
	p.id,
	p.name as product_name,
	count(oi.id) as order_count
from order_items as oi
left join users as u on oi.user_id = u.id 
left join products as p on  oi.product_id = p.id
where u.age <= 39
group by p.id
order by order_count desc
limit 5
