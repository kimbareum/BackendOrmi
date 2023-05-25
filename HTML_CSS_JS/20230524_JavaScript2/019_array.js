const arr1 = [];
const arr2 = [1, 2, 3];
const arr3 = new Array(4, 5, 6);

const arr = [[10, 20], 2, 3, 4, 5];
arr[0];
arr[0][0];
arr.length;
// 무조건 마지막값만 꺼냄. 안에 파라미터는 보지도않음.
arr.pop();
arr.push(6);
////////////////////////////////////////////////////
const arr4 = [1, 2, 3, 4, 5];
// popleft
arr4.shift();
// appendleft(여긴 순서대로 들어감.)
arr4.unshift(100, 200);

////////////////////////////////////////////////////

const arr5 = [10, 20, 30, 40, 50, 60];
arr5.slice(2, 5);

////////////////////////////////////////////////////

const arr6 = [1, 2, 3, 4, 5];
// splice는 배열의 요소를 추가, 제거 또는 교체함
// splice(시작인덱스, 삭제할개수, 추가할요소들)

// insert(1,100)
arr6.splice(1, 0, 100);
// pop(1)
arr6.splice(1, 1);
// index 1을 삭제하고 7을 추가
arr6.splice(1, 1, 7);
// index 1을 삭제하고 6, 7을 추가
arr6.splice(1, 1, 6, 7);

////////////////////////////////////////////////////

const arr7 = [1, 11, 2, 3, 7, 8, 22, 5];
// 사전식으로 정렬함
arr7.sort();
// 숫자로 정렬하려면 함수를넣어야함
// 오름차순
arr7.sort((a, b) => a - b);
// 내림차순
arr7.sort((a, b) => b - a);
// 에러가 날수 있으니까 이런거 써야함...
arr7.sort((a, b) => (a[key] > b[key] ? -1 : a[key] < b[key] ? 1 : 0));

////////////////////////////////////////////////////

const arr8 = [1, 11, 2, 3, 7, 8, 22, 5];
// array 내부에서 반복만 하는 메서드
// 새로운 array를 만들고싶다면 map을 써야함.
// index와 arr는 생략도 가능
arr8.forEach((value, index, arr) => {
    console.log(value);
    console.log(index);
    console.log(arr);
});

// map 을 이용해 가공하기.
let power_arr = arr8.map((v) => v ** 2);
// 데이터 뽑아내기
[
    {
        name: "hojun",
        age: 10,
    },
    {
        name: "gildong",
        age: 20,
    },
].map((x) => x.age);

const arr9 = [1, 11, 2, 3, 7, 8, 22, 5];
arr9.forEach((value) => {
    console.log(value);
});

// 이런 느낌으로 쓸수 있음.
const arr10 = [1, 11, 2, 3, 7, 8, 22, 5];
arr10.forEach((v, i) => {
    const tag = document.getElementById(i);
    tag.innerHTML = v;
});

////////////////////////////////////////////////////

const arr11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const newArr = arr11.filter((el) => el % 2 === 0);

console.log(newArr);

////////////////////////////////////////////////////

// reduce((누적값, 가산값) => 할 일, 초기값)
[1, 2, 3, 4].reduce((a, b) => a + b, 0);

[1, 2, 3, 4].reduce((a, b) => {
    console.log(a, b);
    return a + b;
}, 0);
// 1, 2 / 3,3 / 6,4

////////////////////////////////////////////////////

const arr12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// 값이 있는지 찾음.
arr12.includes(10); // true
arr12.includes(1000); // false
// in 문법은 index(key) in arr 로 써서 index나 key가 arr안에 존재하는지 판별함
1 in arr12; // true
10 in arr12; // false(인덱스가 0-9까지 존재)
d // true

////////////////////////////////////////////////////

const arr13 = ["hello", "world", "hojun"];
arr13.join("!"); // hello!world!hojun
// 데이터를 이어붙이고 싶을땐 전개구문 활용 가능.
const arr14 = ["1", "2", "3"];
const arr15 = [...arr13, "이어붙임", ...arr14];

//arr13 + arr14 는 안됨. 문자열로 붙여버림 arr13 + ['',''] + arr14 는 되긴하네오

////////////////////////////////////////////////////

Array.from("string");
// list('string')
