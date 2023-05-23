// https://ko.javascript.info/nullish-coalescing-operator
// 나온지 얼마 안됐음. (IE는 지원하지 않음.)
// null 과 undefined 만 걸러주는 문법
// '' 나 0 같은건 안걸러지고 반환함.

let firstname = null;
let lastname;
let nickname = "licat";

// 앞에 있는거부터 검사해서 나오면 반환하고 뒤에껀 검사안함.
name1 = firstname ?? lastname ?? nickname ?? "anonymous";

let height = 0;
height || 100; // 100
height ?? 100; // 0 (0은 null 이나 undefined가 아니니까)
