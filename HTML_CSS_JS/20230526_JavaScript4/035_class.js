// javascript 의 class 는 ES6 부터 나온 문법.
// 이전에는 생성자 함수를 사용했음.

let myArr = new Array(1, 2, 3);
// python에서 마치 클래스로 인스턴스를 만들어내듯 찍어내는 것
// Array 생성자함수. 마치 파이썬의 instance 처럼 prototype을 공유함.
let myArr2 = new Array(4, 5, 6);

myArr2.length;
myArr.length;

myArr.forEach((item) => {
    console.log(item);
});

myArr2.forEach((item) => {
    console.log(item);
});

////////////////////////////////////////////
// 커스텀 생성자 만들어보기

function Factory() {}
function NewFactory(name) {
    this.name = name;
    this.sayYourName = function () {
        console.log(`삐리삐리. 제 이름은 ${this.name}입니다. 주인님.`);
    };
}
let robot1 = new Factory();
let robot2 = new NewFactory("브랜든");
// => 그런데 이러면 객체를 만들때마다 새로운 함수를 만들고있는것.

function Parent() {
    this.name = "재현";
}

Parent.prototype.rename = function (name) {
    this.name = name;
};

Parent.prototype.sayName = function () {
    console.log(this.name);
};

let 부모1 = new Parent();
부모1.rename("호준");
부모1;

function Child() {
    Parent.call(this);
}

Child.prototype = Object.create(Parent.prototype);
Child.prototype.canWalk = function () {
    console.log("now i can walk!!");
};

Child.prototype.rename("호돌");
Child.prototype.sayName();

// 생성자 함수를 만들게 되면 위에서 child가 parent를 상속받았기 떄문에
// child가 parent의 메서드나 멤버를 사용할 수 있음.
let 자식1 = new Child();
자식1.rename("호돌돌");
자식1.sayName();

////////////////////////////////////////////////
// class

class Robot {
    // 파이썬의 __init__
    constructor(name) {
        this.name = name;
    }

    // 앞에 function을 붙이지 않음.
    sayYourName() {
        console.log(`삐리삐리. 제 이름은 ${this.name}입니다. 주인님.`);
    }
}

class BabyRobot extends Robot {
    constructor(name) {
        super(name);
        this.ownName = "아이크";
    }

    sayBabyName() {
        //상속을 받게되면 this로 부모의 메서드에 접근 할 수 있음.
        this.sayYourName();
        console.log("Suceeding you, Father!");
    }
}

let one = new Robot("one");
let two = new BabyRobot("two");
