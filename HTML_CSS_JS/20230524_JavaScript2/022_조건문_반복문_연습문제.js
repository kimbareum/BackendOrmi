///////////////////////////////////////////////////////////////
// 1에서 100까지 더하기
let sum1 = 0;
for (let i = 1; i <= 100; i++) {
    sum1 += i;
}

let sum2 = 0;
let i = 0;
while (i < 101) {
    sum2 += i;
    ++i;
}
console.log(sum2);

// range 구현하기
// 개인프로젝트 할때 쓰면 편함. 단체는 남이 보면 코드를 몰라서 문제가될수있음.
let range = (len) => new Array(len).fill(1).map((_, i) => i);
let sum = (iterable) => iterable.reduce((a, b) => a + b, 0);

let s = 0;
for (const i of range(101)) {
    s += i;
}

range(101).reduce((a, b) => a + b, 0);

///////////////////////////////////////////////////////////////
// 1에서 100까지 짝수만 더하기

sum(range(101).filter((v) => v % 2 === 0));

let sum3 = 0;
for (let i = 0; i < 101; i += 2) {
    sum3 += i;
}

let sum4 = 0;
let i2 = 0;
while (i2 < 101) {
    sum4 += i2;
    i2 += 2;
}

//////////////////////////////////////
// 5보다 작은값
let data1 = [10, 5, 4, 7, 9, 3, 2, 5, 4, 7, 4, 2, 1];

data1.filter((v) => v < 5).reduce((a, c) => a + c, 0);

let sum5 = 0;
for (const i of data1) {
    if (i < 5) {
        sum5 += i;
    }
}

let sum6 = 0;
for (const i of data1.filter((v) => v < 5)) {
    sum6 += i;
}

data1.map((v) => (v < 5 ? v : 0)).reduce((a, c) => a + c, 0);

data1.reduce((a, c) => (c < 5 ? a + c : a), 0);

let sum7 = 0;
data1.forEach((v) => v < 5 && (sum7 += v));
sum7;

// [10, '5', 4, '7', 9, '3', 2, '5', 4, '7', '4', '2', '1']에서 모든 숫자를 다 더해주세요.

data2 = [10, [10], 4, "7", 9, "3", 2, "5", 4, "7", "4", "2", "1"];
data2.reduce((a, c) => (c === parseFloat(c) ? a + c : a), 0);
data2.reduce((a, c) => (typeof c == "number" ? a + c : a), 0);

let sum8 = 0;
for (const i of data2) {
    if (typeof i === "string") {
        sum8 += i;
    }
}

// 타입체크 함수
function typeCheck(value) {
    return Object.prototype.toString.call(value).slice(8, -1);
}
typeCheck(123);

///////////////////////////////////////////////////////////////
// 모음제거

my_string = "nice to meet you";

function solution(my_string) {
    let answer = "";
    Array.from("my_string").filter(
        (v) => ["a", "e", "i", "o", "u"].includes(v) || (answer += v)
    );
    return answer;
}

///////////////////////////////////////////////////////////////
// 용돈은 매년 2배씩 오름.
// 올해 받은 용돈은 10000원
// 나이는 8살
// 30만원 이상이 되면 용돈이 더이상 오르지 않습니다

let sum9 = 0;
let money = 10000;
for (let i = 8; i < 36; i++) {
    sum9 += money;
    if (money > 300000) {
        continue;
    }
    money *= 2;
}

function solution(my_string) {
    return Array.from(my_string)
        .filter((v) => !isNaN(v))
        .map((v) => parseInt(v))
        .sort((a, b) => a - b);
}

solution("p2o4i8gj2");

/////////////////////////////////////////////////////////
// advanced 문제
fetch("http://test.api.weniv.co.kr/mall")
    .then((data) => data.json())
    .then((data) => {
        average = data.reduce((a, c) => a + c.price, 0) / data.length;
        console.log(`갯수 : ${data.length}, 평균 : ${average.toFixed(2)}`);
    });

///////////////////////////////////////////////////////////
// https://codingdojang.com/scode/393?answer_mode=hide
// str(list(range(10001))).count('8')
// 이 코드는 알고리즘 문제 풀이할 때만 쓰세요.
".".repeat(99);
".".repeat(99).split(".");
"."
    .repeat(99)
    .split(".")
    .map((v, i) => i + 1);
"."
    .repeat(99)
    .split(".")
    .map((v, i) => i + 1);
"."
    .repeat(99)
    .split(".")
    .map((v, i) => i + 1)
    .join("")
    .split("")
    .filter((v) => v === "8").length;

let s2 = "";
for (let i = 0; i < 101; i++) {
    s2 += i;
}
s2.split("").filter((v) => v === "8").length;

Array(100)
    .fill(0)
    .map((v, i) => "" + i);

Array(101)
    .fill(0)
    .map((v, i) => "" + i) // 안에서 메서드 체이닝을 한 번 더 할 수 있지만 복잡도만 상승할 것 같아 실행하지 않았습니다.
    .join("")
    .split("")
    .filter((v) => v === "8").length;

/////////////////////////////////////////////////////////////
// 9. 가장 거리가 짧은 점

// zip 구현
const zip = (a, b) => a.map((v, i) => [v, b[i]]);

let s1 = [1, 3, 4, 8, 13, 17, 20];

zip(s1, s1.slice(1)).sort((a, b) => a[1] - a[0] - (b[1] - b[0]))[0];

let answer = [0, Infinity];
for (let i = 0; i < s1.length; i++) {
    if (answer[1] - answer[0] > s1[i + 1] - s1[i]) {
        answer = [s1[i], s1[i + 1]];
    }
}
console.log(answer);

/////////////////////////////////////////////////////////////////
//

let weight = [60, 50, 55, 60, 77, 88, 56, 67, 89, 45];
let max_weight = 500;
let total_weight = 0;
let count = 0;
for (const i of weight.sort((a, b) => a - b)) {
    if (total_weight + i > max_weight) {
        break;
    }
    total_weight += i;
    count += 1;
}
console.log(count);

// map 구현
const map = (func, iter) => {
    result = [];
    for (const i of iter) {
        result.push(func(i));
    }
};
