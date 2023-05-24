const babaYaga = {
    name: "John Wick",
    age: 53,
    from: "벨라루스",
    askingHim: function () {
        console.log("Yeah, I'm thinking I'm back!");
    },
};

// 새로운 문법으로function 선언없이도 사용 가능
const babaYaga2 = {
    name: "John Wick",
    age: 53,
    from: "벨라루스",
    askingHim() {
        console.log("Yeah, I'm thinking I'm back!");
    },
};

// 최신문법으로 이런식으로도 생성가능
const a = "hello";
const b = "world";
const data = {
    a,
    b,
    c: "!!",
    d: [10, 20, 300],
};

// CRUD(Create, Read, Update, Delete)
// 데이터 추가(append), 데이터 업데이트(update)
const human = {
    name: "hojun",
    age: 98,
};
human.height = 250;
// human[height] = 250 (동일함)

// 전개구문 사용해서 update 하기
const human2 = {
    ...human,
    age: 10,
};

// delete 는 그냥 Null값 넣어줌
human.age = Null;

// human.keys() 식으로는 못씀.
// Object를 상속받고있어서 저런식으로 건드리면 전부 건드리게되버림
// JS 란 뭘까..
Object.keys(human);
Object.values(human);
Object.entries(human);
