let x = true;
let y = false;

// && 논리 곱(and)
// || 논리 합(or)
// ! 부정(not)

x && y;
x || y;
!x;
!y;
!!"hello"; // 실무에서 bool 타입으로 간단하게 변환해버리는 방법.

!!NaN; // false
!!null; // false
!!undefined; // false

// 그렇다고 Number.isNaN 보다 유용한가? [], {}같은거에선 Number.isNaN이 유용

//단락평가

let name1 = "";
let name2 = "hello";

function defaultName(name) {
  return name || "이름이 입력되지 않음";
}
defaultName(name1); // '이름이 입력되지 않음'
defaultName(name2); // 'hello'

// 보통은 3항연산자 + 단락평가로 사용함.
let isLogin = true;
LoginPage = isLogin && "<h1>환영합니다. 고객님</h1>";
document.write(LoginPage);

let pw = "";
pw = pw || "패스워드가 입력되지 않았습니다.";
