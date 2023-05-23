// python 과는 달리 key 값이 자동으로 string으로 변환되서 들어감. 변수취급을 안함.
let user = {
  id: "licat",
  pw: "1234",
  name: "leehojun",
  email: "name@gmail.com",
  active: false,
};

// 둘다 접근 가능.
user["id"];
user.id;
// obj.'id' 이건 에러

let a = 10;
let b = 10;
let c = 10;
let e = { a, b, c };
// 이런 선언도 가능.

// 유사배열 객체 => 배열과 유사하지만 배열은 아닌것.
let txt = {
  0: "h",
  1: "e",
  2: "l",
  3: "l",
  4: "o",
};
txt[0]; // 배열과 접근방법이 동일. 근데 왜씀?

// value의 값으로 문자열 외에 다른 값을 넣었을 경우
let test = {
  one: sum,
  two: console.log,
  three: window.innerWidth,
  four: [10, 20, 30],
  five: "10",
  six: 100,
};
console.log(test);
test.two("호준!!");

// key 와 value
// user.keys 처럼 사용하지 못함.
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));
// => 그래서 map이라는 자료형이 나왔음.
