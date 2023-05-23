let a = 10;

// 단항연산자
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Operator_Precedence
// 할당할때만 차이가 있음.
a++; // 선할당 후증가
++a; // 선증가 후할당

for (let i = 0; i < 10; i++) {
  console.log(i);
}
// 출력할때나 할당안할때는 둘다 같음
for (let i = 0; i < 10; ++i) {
  console.log(i);
}

// 할당연산자
a = 10;
a += 5;
a /= 5;

// 삼항연산자
// 조건식 ? 참일떄 : 거짓일때
// 중첩도 가능
a == 10 ? a : 0;

let x = true ? 100 : 200;
let y = false ? 100 : true ? 200 : 300;

// 예제: 에러가 나지 않는 레거시 코드(한글, 영어, 숫자 등등)
var sortedData = jsonData.sort((a, b) =>
  a[key] > b[key] ? -1 : a[key] < b[key] ? 1 : 0
);

// 아래와 같이 변수할당 없이 바로 3항 연산자로 return 가능
function solution(n) {
  return Math.sqrt(n) === Math.floor(Math.sqrt(n)) ? 1 : 2;
}

// 3항 연산자의 예제
// 재귀 함수
const 팩토리얼 = (num) => (num === 0 ? 1 : num * 팩토리얼(num - 1));

// https://school.programmers.co.kr/learn/courses/30/lessons/120853
function solution(s) {
  s = s.split(" ");
  let arr = [];
  for (let v of s) v === "Z" ? (arr.length ? arr.pop() : "") : arr.push(v);
  return arr.reduce((a, v) => a + +v, 0);
}
