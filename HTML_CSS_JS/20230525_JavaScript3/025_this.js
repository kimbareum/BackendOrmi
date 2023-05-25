// 파이썬의 self와 유사함
// 하지만 this는 예외사항이 너무많아서
// 논리적으로 이해하는 것이 거의 불가능함....??
// JS는 뭘까..

/////////////////////////////////////////
// 보통은 자기자신을 호출한 것이 this 임.

// a를 호출한게 window 이기 때문에 window를 출력함.
function a() {
    console.log(this);
}
a();

// 이 경우는 myObj 가 func1을 호출했으니까
// myObj를 출력함.
let myObj = {
    val1: 100,
    func1: function () {
        console.log(this);
    },
};
myObj.func1();

//////////////////////////////////////////////////
// 027_this.html (버튼액션)

//////////////////////////////////////////////////
// 기본적으로는 타고타고올라가서 window 바로 아래 있는걸 부르는 느낌.

function sayName() {
    console.log(this.name);
}
var name = "Hero";

let peter = {
    name: "Peter Parker",
    sayName: sayName,
};

let bruce = {
    name: "Bruce Wayne",
    sayName: peter.sayName,
};

bruce.sayName();

/////////////////////////////////////////////////
// 대충 정리

`
1. 전역공간의 this 는 window 를 가리킴
2. 메서드로 호출한 경우 this는 멤버 접근 연산자 앞의 객체
3. 함수로 호출할 경우 this 는 window
4. 화살표 함수의 경우 this는 상위스코프
5. 생성자 함수의 경우 this는 인스턴스
6. 콜백 함수는 this가 다르게 동작할 수 있음.
`;
