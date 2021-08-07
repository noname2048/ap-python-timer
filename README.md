## 알고리즘 시간을 측정할때, 3가지 방법
1. 함수내부에서 datetime.datetime 이용하기
2. 데코레이터 + datetime
3. timeit (with callale)

## 기타 tips
- `print(f"{0.3234:.f}")`에서 f와 } 사이에 공간이 있으면 Invalid forma specifier가 나온다.
- 또한, f와 F는 같은 역할을 한다. 자세히 살펴보려면 python의 "printf 스타일 문자열 포매팅" 을 살펴보자
- timeit 을 데코레이터로 감싸는데 실패했다. (argument 넘길방법을 찾기 어려웠다.)
- `1.`의 대안으로 `timeit.default_timer()` 구문을 사용해도 괜찬다. (`time.time()`도 있다.)
