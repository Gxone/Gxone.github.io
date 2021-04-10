---
title: "[TIL] 210309 /striftime, striptime, timedelta"
categories: python django
---
## strftime / strptime

 strftime | strptime
 -- | --
**datetime** to **str**|  **str** to **datetime** 
```strftime(format)``` | ```strptime(str, format)```
date, time, datetime | datetime

## timedelta
>class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

```date```, ```time```, ```datetime``` 객체를 대상으로 ```timedelta```를 통해 날짜 및 시간 계산이 가능하다. ```timedelta``` 클래스의 생성자는 주, 일, 시, 초, 분, 마이크로초, 밀리초를 인자로 받는다. 
모든 인자는 기본 값이 0이며 선택적이다. 정수, 부동소수점, 양수, 음수가 올 수 있다.

또한 *days, seconds, microseconds*만 내부적으로 저장되기 때문에 인자는 이 단위로 변환된다. 

```py
 from datetime import timedelta
 delta = timedelta(
     days=50,
     seconds=27,
     microseconds=10,
     milliseconds=29000,
     minutes=5,
     hours=8,
     weeks=2
 )

 # Only days, seconds, and microseconds remain
 >>> delta
datetime.timedelta(days=64, seconds=29156, microseconds=10)
```


<br>

---
참고

[https://docs.python.org/ko/3/library/datetime.html#strftime-strptime-behavior](https://docs.python.org/ko/3/library/datetime.html#strftime-strptime-behavior)