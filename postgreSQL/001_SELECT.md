DB = > 데이터의 집합
DBMS => Database Management System : 데이터베이스 관리 소프트웨어
관계형 데이터베이스 -> 데이터를 표 형태로 관리하는 데이터베이스.
RDBMS = > 관계형 데이터베이스 관리 시스템
SQL => RDBMS를 다루기 위한 스토리지 언어의 표준.

SQL 명령어의 분류.
- 데이터 조작어(DML)
    - **SELECT**
    - **INSERT**
    - **UPDATE**
    - **DELETE**
- 데이터 정의어(DDL)
    - **CREATE DATABASE**
    - **CREATE TABLE**
    - **CREATE INDEX**
    - **ALTER DATABASE**
    - **ALTER TABLE**
    - **DROP TABLE**
    - **DROP INDEX**
    - RENAME
    - TRUNCATE
- 데이터 제어어(DCL)
    - GRANT : 권한 부여
    - REVOKE : 권한 제거
- 트랜젝션 제어어(TCL)
    - COMMIT
    - ROLLBACK
    - SAVEPOINT


## SQL

- DBeaver 기반으로 sql 사용. (DBeaver는 커서위치를 실행함)

### 데이터 조작어

- SELECT
    - 데이터 조회. SELECT 2+5; 같은 계산도 가능함
    - 문자열은 ' ' 로 감싸줘야함.
    - DBeaver에서는 문자열 더하기를 || 로 함. (select 'hello' || 'world';)
    - concat 함수도 존재함. (select concat('hello', 'world');)

    - select * from users => users 테이블에 있는 모든 데이터를 조회
    - select id, first_name from users => users 테이블에서 id와 first_name 만 조회

- SELECT 연습문제
    1. users 테이블의 모든 데이터 조회 : select * from users;
    2. users 테이블의 email 정보를 조회 : select email from users;
    3. users 테이블에서 first_name, last_name, email, country 정보 조회 : select first_name , last_name , email , country  from users;
    4. 3번문제에서 fullname까지 만들어서 조회 : select id, first_name , last_name , concat(first_name, ' ', last_name) , email , country  from users;
    5. 상품정보(products) 테이블의 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost)을 조회하세요. : select id, category, name, retail_price, cost from products;
    6. 상품정보(products) 테이블의 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost), 판매이익(판매가격 - 비용)을 조회하세요. : select id, category, name, retail_price, cost, (retail_price - cost) from products;

- AS, LIMIT, DISTINCT
    AS : 행이나 테이블의 이름 지정
    LIMIT : 가져올 갯수 제한.
    ```
    select 
        id as product_id,
        category as product_category, 
        name as product_name, 
        retail_price as product_retail_price, 
        cost as product_cost, 
        (retail_price - cost) as product_profit 
    from products as p
    limit 10;
    ```

    DISTINCT : 중복제거. 묶으면 조합의 중복을 제거함(A, B 와 A, C는 서로 다른걸로 판정).
    ```
    select
        distinct city
    from users;

    select 
        distinct country, city
    from users;
    ```

    6. 상품정보(products) 테이블에서 5개 레코드만 조회하세요. : select * from products limit 5;

    7. 주문정보(orders) 테이블에서 상태정보(status)를 중복제거하여 조회하세요. : select distinct status from orders;

    8. 상품정보(products) 테이블에서 카테고리(category)를 중복제거하여 조회하세요. : select distinct category from products;

    9. 상품정보(products) 테이블에서 카테고리(category), 브랜드(brand)를 중복제거하여 30개 조회하세요. 각 결과 컬럼의 이름은 다음과 같이 지정하세요. 카테고리 → product_category, 브랜드 → product_brand : select distinct category as product_category, brand as product_brand from products limit 30;

    10. 상품정보(products) 테이블에서 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost), 판매이익(판매가격 - 비용), 수익율((판매가 - 비용) / 비용 x 100)을 조회하세요.
    각 컬럼의 이름은 다음과 같이 표현합니다.
    id → product_id
    카테고리 → product_category
    상품명 → product_name
    판매가격 → product_price
    비용 → product_cost
    판매이익 → product_profit
    수익율 → product_profit_rate
    : 
    select 
        id as product_id, 
        category as product_category, 
        name as product_name, 
        retail_price as product_price, 
        cost as product_cost, 
        (retail_price - cost) as product_profit,
        (retail_price - cost)/cost*100 as product_profit_rate
    from products