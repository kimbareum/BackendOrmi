// if (조건) 행동; 한줄로 쓸수는 있는데 가독성 떨어짐.

if (false) {
    console.log("hello1");
} else if (false) {
    console.log("hello2");
} else if (false) {
    console.log("hello3");
} else {
    console.log("hello4");
}

///////////////////////////////////////////////////
// switch (표현식){
//     case 값1:
//         행동
//         break;
//     case 값1:
//         행동
//         break;
//     case 값1:
//         행동
//         break;
//     default:
//         행동
//         break;
// }

// break 빼면 맞는쪽부터 다 실행함. 이용도 가능.
switch (2) {
    case 1:
        console.log(1);
        break;
    case 2:
        console.log(2);
        break;
    default:
        console.log("default");
        break;
}

///////////////////////////////////////////////////

// for (let index = 0; index < arr.length; index++) {}

// for (const key in arr) {}

// for (const iterator of arr) {}

// while (condition) {}
arr = [10, 20, 30];

// range for 문
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

// 딕셔너리 순회처럼 key로 순회도는 for문
for (const i in arr) {
    console.log(i, arr[i]);
}

// for i in arr 구문
for (const i of arr) {
    console.log(i);
}

let x = 0;
while (x < 10) {
    console.log(x++);
}
