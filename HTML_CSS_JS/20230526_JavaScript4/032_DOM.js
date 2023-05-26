// 얘네들은 트리탐색을 하기때문에 부하가 발생함
// for 문 등에서 쓰는건 자제하는게 좋음. 전역에서 쓰고 넘겨주는식이 좋음.

document.getElementById();
// Id로 접근하기

document.querySelector();
// CSS 선택자로 단일요소에 접근하기

document.querySelectorAll();
// 모든 요소에 접근하기.
// forEach가 존재함

/////////////////////////////////////////////////
// 이벤트 감지

const myBtn = document.querySelector("button");

myBtn.addEventListener("click", function () {
    console.log("hello world!");
});

myBtn.addEventListener("click", () => console.log("hello world!"));

const title = document.querySelector("#one");
const btn_red = document.querySelector("button");
btn_red.addEventListener("click", () => title.classList.toggle("red"));

///////////////////////////////////////////////
// element 생성 및 추가

const sectionTitle = document.createElement("h2");
sectionTitle.innerText = "hello";
document.querySelector("body").appendChild(sectionTitle);
// body에 타이틀 추가

const body = document.querySelector("body");
const myUl = document.createElement("ul");
for (let i = 0; i < 5; i++) {
    const myLi = document.createElement("li");
    myLi.innerText = i + 1;
    myUl.append(myLi);
}
body.appendChild(myUl);
// body에 ul li 추가

///////////////////////////////////////////////
// style
const textColor = target.style.color;
target.style.color = "red";
target.style.fontWeight = "bold";
// font-weight 같은건 카멜표기법으로 바꿔써야함.

///////////////////////////////////////////////
// attribute 제어

// const body = document.querySelector("body");
const myimg = document.createElement("img");
myimg.setAttribute(
    "src",
    "https://img.wendybook.com/image_detail/img159/159599_01.jpg"
);
myimg.setAttribute("alt", "이미지");
body.append(myimg);

///////////////////////////////////////////////
// 요소에 데이터를 저장하도록 도와주는 data속성
// 왜 이런걸?
`
<img
    class="terran battle-cruiser"
    src="battle-cruiser.png"
    data-ship-id="324"
    data-weapons="laser"
    data-health="400"
    data-mana="250"
    data-skill="yamato-cannon"
/>
``<script>`;
console.log(target.dataset);
console.log(target.dataset.shipId);
`</script>`;
// 여기도 카멜인걸 주의

////////////////////////////////////////////
// 이벤트의 정보 알아보기.

const btn = document.createElement("button");
btn.innerText = "눌럿!";
// const body = document.querySelector('body')
body.append(btn);

btn.addEventListener("click", function (event) {
    console.log(event);
    console.log(event.target);
    console.log(event.currentTarget);
    console.log(this);
    // 이벤트를 실행시킨 주체를 지칭함.(화살표함수를 쓰는것과 function 을 쓰는것이 다름)
    // function 을 쓰면 button 을 가리키고, => 를 쓰면 window를 가리킴
});

////////////////////////////////////////////
// submit 의 작동을 중지하고 JS로 제어하기

`
<!-- 앵커의 기본 동작을 중지 -->
<a href="https://www.naver.com" class="link">네이버 링크입니다만..</a>
<script>
    const link = document.querySelector('.link');
    link.addEventListener('click', (event) => {
        console.log('clicked');
        event.preventDefault(); <-
    })
</script>

<!-- submit 의 기본 동작을 중지 -->
<form action="">
    <button type="submit" class="submit">제출</button>
</form>
<script>
    const submit = document.querySelector('.submit');
    submit.addEventListener('click', (event) => {
        console.log('clicked');
        event.preventDefault(); <-
    })
</script>
`;
