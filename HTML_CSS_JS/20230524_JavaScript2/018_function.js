function f(x, y) {
    return x + y;
}

// 즉시실행함수. 함수를 정의하자마자 실행함.
(function () {
    console.log("Hello");
});

// lambda 함수 같은것.
// 코드가 1줄짜리면 return을 생략.
(x, y) => x + y;
let f2 = (x, y) => x + y;

// 중괄호로 여러줄의 코드를 거치려면 return을 넣어야함.
let f3 = (x, y) => {
    let z = x + y;
    return z;
};

// 파라미터가 1개이면 소괄호도 생략 가능
let f4 = (x) => x + x;

// 반지름 구하는 함수
let f5 = (r) => r ** 2 * Math.PI;

// 중괄호 쓰는 형태로
// 여러값이 입력되었을 때 가장 큰 값과 가장 작은 값, 총합을 한꺼번에 출력하는 함수
// 입력 (a,b,c,d) 출력 [max, min, sum]

let f6 = (a, b, c, d) => {
    max = Math.max(a, b, c, d);
    min = Math.min(a, b, c, d);
    sum = a + b + c + d;
    return [max, min, sum];
};

function f7(a, b, c, d) {
    max = Math.max(a, b, c, d);
    min = Math.min(a, b, c, d);
    sum = a + b + c + d;
    return [max, min, sum];
}
