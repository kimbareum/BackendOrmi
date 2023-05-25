///////////////////////////////////////////////
// rest 문법 (파이썬이 아규먼트받을때 * 쓰는 느낌)
// 전개구문을 파라미터에 쓰면 남은 모든 값을 배열에 넣음
// 하나만 존재할수있고 맨뒤에 존재해야함

function 함수1(a, b, ...c) {
    console.log(c);
    return Math.max(...c);
}

함수1("hello", "world", 10, 20, 30, 40);

function 함수2([a, b], ...c) {
    console.log(a);
    console.log(b);
    console.log(c);
}

함수2([1, 2], 10, 20, 30, 40);

////////////////////////////////////////////////
// 매개변수 초기화

function 함수3(a = 10, b = 20, c = 30) {
    return a + b + c;
}
console.log(함수3());

////////////////////////////////////////////////
// 스코프 체이닝

// 전역스코프 : 외부
// 함수스코프 : 함수내부
// 블록스코프 : 중괄호 내부
// 자기안에 없으면 상위스코프로 올라가면서 탐색함.
// 상위스코프의 값도 수정이 가능.(파이썬과 다름.)
// 상위스코프에서는 하위스코프의 값을 참조못함 (var는 지멋대로 다함. 쓰지말아야하는 이유.)

///////////////////////////////////////////////
// 콜백 함수
// 함수에 매개변수로 전달되어 실행되는 함수
// 함수에 아규먼트로 전달.

// 이런것
function sum(x, y) {
    return x + y;
}
function custom(x, y, func) {
    return func(x, y) * 2;
}
custom(10, 20, sum);

// 이미 이런식으로 써왔음
arr = [1, 2, 3];
arr.sort(콜백함수);
arr.filter(콜백함수);
arr.map(콜백함수);

///////////////////////////////////////////////
// 함수의 호이스팅(끌어올리기)
// 밑에서 선언된 함수도 사용가능한 것 (파이썬에서는 안됨.)
// let, const, class 를 이용한 선언문은 일시적 사각지대(Temporal Dead Zone) 을 만들어서 호이스팅이 안된것처럼 작동하게 함.
// var 키워드는 선언과 함께 undefined로 초기화
// let과 const는 초기화 되지 않는 상태로 선언했다는 사실만 메모리에 저장

console.log(add1(10, 20)); // 30
console.log(add2(10, 20)); // 30
console.log(mul1); // undefined. undefined로 초기화 되었음
// console.log(mul1(10, 20)); // not a function. 아직은 undefined 인 상태이기 때문에 함수로 실행은 못함
// console.log(mul2); // Cannot access 'mul2' before initialization. 초기화가 안된 상태.
// console.log(mul2(10, 20)); // 위와 같은 애러

function add1(x, y) {
    return x + y;
}

function add2(x, y) {
    return x + y;
}

var mul1 = function (a, b) {
    return a * b;
};

let mul2 = function (a, b) {
    return a * b;
};

///////////////////////////////////////////////////////
// 재귀함수

function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

console.log(factorial(5));

///////////////////////////////////////////////////////
// 클로저. 폐쇄된 공간 안의 데이터에 접근하기 위한 테크닉.

function one(x) {
    function two(y) {
        return x ** y;
    }
    return two;
}

let power2 = one(2);
let power3 = one(3);

console.log(power2(3), power3(3));

///////////////////////////////////////////////////////
// 생성자 함수. class와 비슷한 함수.
// 단순히 찍어내는 용도로는 class가 더 유용
// 기능적인 부분이 추가되는 경우 생성자 함수로 만들기도 함.
// 동일 property를 가지는 객체를 생성.
// prototype을 이용하여 메모리 효율을 높일 수 있음. (가볍게 쓸 수 있음.)

function Book(bookName, bookPrice, author, date) {
    this.bookName = bookName;
    this.bookPrice = bookPrice;
    this.author = author;
    this.date = date;
}

// new 라는 키워드는 object를 반환함.
// 함수내에 this = {} 를 만들고
// 요소를 업데이트한 후
// return this 를 하는것 처럼 작동함.
let book1 = new Book("Python", 1000, "hojun", "2023.05.25");
console.log(book1);
