///////////////////////////////////////////////////////
// Map
// 키와 쌍을 가지는 자료형

let m = new Map();

// Map에 값을 넣기
// 모든 타입의 key가 가능. object는 문자열만 key로 가질 수 있음
m.set("하나", "1");
console.log(m);
m.set(1, "하나");
console.log(m);
m.set(true, 1);
console.log(m);
m.set(false, 0);
console.log(m);

// Map의 값에 접근하기
console.log(m.get("하나"));
console.log(m.get(true));

// Map의 값이 있는지 확인하기
console.log(m.has("하나"));

// Map의 값을 제거하기
console.log(m.delete("하나"));
console.log(m.has("하나"));
console.log(m);

// Map의 크기를 확인하기
// Object는 길이값을 따로 가지고 있지 않음. 순회로 찾아야함.
console.log(m.size);

// let mm = new Map()
// mm.set('하나', m)
// Map(1) {'하나' => Map(3)}
// mm.set('하나', {'one':1, 'two':2})
// Map(1) {'하나' => {…}}

// for of 문으로 순회를 돌면 entries 로 순회를 돌 수 있음
// [key, values]
// object 는 iterable 하지 않음. in으로 순회돌아야함.
for (const i of m) {
    console.log(i);
}

// 이렇게 바로 쓰는것도 가능.
console.log(m.keys());

// 메서드 체이닝으로 추가등도 가능.
const data = new Map().set("name", "hojun").set("age", 10).set("height", 180);

console.log(data);

// object 자료형의 변환
let temp2 = new Map(Object.entries({ one: 1, two: 2 }));

console.log(temp2);

// 반대의 경우
const temp3 = Object.fromEntries(temp2);
console.log(temp3);

///////////////////////////////////////////////////////
// Set
// 키와 쌍을 가지는 자료형
// 메서드가 별로없어서 굳이 쓸 이유가..

let s = new Set("abcdeeeeeeeee");
console.log(s);
console.log(s.size);

// Set에 값을 추가하기
s.add("f");
console.log(s);

// Set을 순환하기
for (let variable of s) {
    console.log(variable);
}

// 값이 배열인 경우
let ss = new Set("abcdeeeeeeeee".split(""));
console.log(ss);

// Set의 값을 제거하기
ss.delete("b");

// Set의 값을 확인하기
console.log(ss.has("a"));

// Set의 모든 값을 제거하기
ss.clear();
console.log(ss);

let a = new Set("abc");
let b = new Set("cde");
// 교집합
let cro = [...a].filter((value) => b.has(value));
console.log(cro);
// 합집합
let union = new Set([...a].concat(...b));
console.log(union);
// 차집합
let dif = [...a].filter((x) => !b.has(x));
console.log(dif);
