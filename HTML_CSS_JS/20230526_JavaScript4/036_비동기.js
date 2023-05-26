// 동기 : 순차적
// 비동기 : 비순차적
// callback 지옥 : callback 함수가 계속해서 쌓여가는것.

///////////////////////////////////////////////////////
// Promise : 비동기프로그래밍을 할 수 있게 해주며, 위에서 언급된 콜백지옥을 어느저도 탈출할 수 있게 만들어주는 것.
// 앞에서 썼던 fetch 같은곳에서 썼던 then.

// resolve(value) - 작업이 성공적으로 마무리되면 호출, 결과는 value에 담김.
// reject(error) - 작업이 실패했을때 호출, 결과는 error에 담김.
// 꼭 이름이 이거일필요는 없음. resolve에 해당되는 값이 나오면 성공이고, reject에 해당되는 값이 나오면 실패인것.

let p1 = new Promise(function (resolve, reject) {
    resolve("hello world");
})
    .then((메시지) => {
        alert(메시지);
        return 메시지.split(" ")[0];
    })
    .then((메시지) => {
        alert(메시지);
        return 메시지[0];
    })
    .then((메시지) => {
        alert(메시지);
    });

///////////////////////////////////////////
let p2 = new Promise(function (resolve, reject) {
    // resolve('hello world');
    reject("hello world");
})
    .then((메시지) => {
        alert(메시지);
        return 메시지.split(" ")[0];
    })
    .then((메시지) => {
        alert(메시지);
        return 메시지[0];
    })
    .then((메시지) => {
        alert(메시지);
    })
    .catch((메시지) => {
        alert("catch 실행!! :" + 메시지);
    });

fetch("http://testtttt.api.weniv.co.kr/mall")
    .then((data) => data.json())
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        // console.log(error)
        alert("서버가 멈췄습니다. 최대한 빠르게 복구하도록 하겠습니다.");
        document.write(
            "서버가 멈췄습니다. 최대한 빠르게 복구하도록 하겠습니다."
        );
    });

//////////////////////////////////////////////
new Promise((resolve, reject) => {
    //코드
})
    .then(() => {
        //코드
    })
    .catch(() => {
        //코드
    })
    .finally(() => {
        //코드
    });
