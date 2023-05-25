// JSON.parse() : JSON 문자열을 자바스크립트 객체로
// JSON.stringify() : 자바스크립트 객체를 JSON 문자열로

const json = '{"result":true, "count":42}';
// const json = '[1, 2, 3]';
const obj = JSON.parse(json);
console.log(obj);

const json2 = { result: true, count: 42 };
const s = JSON.stringify(json2);
console.log(typeof s);

// JSON을 이용한 깊은 복사
let l = [10, 20, 30];
let a = JSON.parse(JSON.stringify(l));
a[0] = 1000;

console.log(l);
