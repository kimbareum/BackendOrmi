////////////////////////////////////////////////////////////////
// 전개구문
const 과일들 = ["사과", "파인애플", "수박"];
const 생선들 = ["조기", "갈치", "다금바리"];
const 합치면 = [...과일들, ...생선들];

console.log(합치면);

const 위니브1 = { 개리: 1, 빙키: 2 };
const 위니브2 = { 라이캣: 3 };
const 위니브3 = { ...위니브1, ...위니브2 };

console.log(위니브3);

const 위니브4 = {
    ...위니브3,
    라이캣: 100,
};

////////////////////////////////////////////////////////////////
// 디스트럭쳐링
// 파이썬의 unpacking
`
let food1, food2, food3;

const categories = { food1: "과일", food2: "채소", food3: "육류" };

food1 = categories.food1;
food2 = categories.food2;
food3 = categories.food3;

console.log(food1, food2, food3);
`;
// 이걸 더 편하게
// 키와 변수명이 같아야만 들어감...
const categories = { food1: "과일", food2: "채소", food3: "육류" };
let { food1, food2, food3 } = categories;
console.log(food1, food2, food3);

// 배열의 디스트럭쳐링
// function도 동일한 구조로 사용 가능

for (const [a, b] of [
    [1, 2],
    [3, 4],
    [5, 6],
]) {
    console.log(a, b);
}
