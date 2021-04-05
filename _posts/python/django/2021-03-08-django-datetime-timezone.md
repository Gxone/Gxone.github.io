---
title: "[Django] Datetime, Timezone"
categories: python django
---
## TIME_ZONE
Django에서 기본으로 지정된 Time Zone은 'UTC'이다. 기본 Time Zone을 변경하기 위해서는 ```settings.py```에서  ```TIME_ZONE```옵션을 지정해주어야 한다.  

```py
// TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'
USE_TZ = True 
```

<br>

## USE_TZ
>```True```와 ```False```로 Time Zone 사용을 명시한다. (timezone-aware의 사용 여부)

**True**: default 값이 UTC가 되며 templates, forms의 datetime에만 ```settings.py```에서 설정한 ```TIME_ZONE```을 적용한다.  

**False**:  ```TIME_ZONE```으로 설정한 시간대는 모든 datetime을 저장할 때 사용된다.

시간을 저장할 때 옵션을 ```False```로 지정하여  ```TIME_ZONE```에 지정한 시간대를 기준으로 데이터베이스에 저장할 수 있다. 하지만 장기적으로 보존할 시간은 ```utc```로 저장하고 각 나라의 위치에 맞게 보여주는 것을 권장한다. 

<br>

## Naive Datetime / Aware Datetime
**Naive Datetime**: ```tzinfo```가 없기 때문에 어느 시간대를 기준으로 하는 시각인지 모호하다.  

아래와 같이 ```datetime.now()``` 또는 ```datetime.today()``` 으로 현재 시각을 가져오는 경우 ```TIME_ZONE```설정에 따라 시간 값이 나오지만 ```tzinfo``` 정보가 없는 ```Naive Datetime``` 객체이다. 이 시간 값을 데이터베이스에 저장하면 UTC 기준의 시각으로 저장되어 모델을 통해 시간 값을 읽어올 경우 UTC가 기준인 ```Aware Datetime``` 객체를 가져오게 된다.

```py
from datetime import datetime

now = datetime.now() // time-zone naive datetime
datetime.datetime(2021,11,11,0,58,102020)
```

**Aware Datetime**: ```tzinfo```를 가지고 있다. 기준이 되는 시간대를 포함하고 있어 사용을 권장한다. 
```py
from django.utils import timezone

now = timezone.now() // time-zone-aware datetime
datetime.datetime(2021,11,11,0,58,102020 tzinfo=)
```

같은 ```2021-01-01 00:00:00```이라도 해당 시각이 어느 나라, 어떤 시간대에서 호출했는지 알 수 없기 때문에 기준이 되는 시간대 정보가 필요하다. 
따라서 기준점이 확실한 ```Aware Datetime```을 사용하는 것이 좋다. 


```Naive Datetime```과 ```Aware Datetime```은 서로 **대소 비교와 연산이 불가능**하기 때문에 섞어서 사용하지 못한다. 
따라서 한 가지의 ```Datetime```으로 통일할 필요가 있는데 위에서 언급했듯이 시간대 정보를 포함하고 있는 **```Aware Datetime```**으로 통일하는 것이 권장된다. 

```py
a = python.datetime.now() // Naive Datetime
b = datetime.datetime.now(datetime.timezone.utc) // Aware Datetime
return a - b // TypeError
```
  

```timezone.now()```       | UTC 기준인 aware 객체.
```timezone.localtime()``` | KST 기준인 aware 객체. ```.date()```를 통해 날짜만 얻을 경우 utc 기준으로 얻는 날짜는 하루 전일 수도 있다.
```timezone.make_aware()```| Naive 객체를 Aware 객체로 변환, 부득이 하게 Naive 객체를 사용해야할 때 Aware 객체로 바꿔주기 위해 사용한다.


<br>

---
참고

[https://docs.djangoproject.com/en/3.1/ref/utils/#django.utils.timezone.make_aware](https://docs.djangoproject.com/en/3.1/ref/utils/#django.utils.timezone.make_aware)  

[https://8percent.github.io/2017-05-31/django-timezone-problem/](https://8percent.github.io/2017-05-31/django-timezone-problem/)  

[https://velog.io/@arara90/js-Django-Timezone-%EC%A0%81%EC%A0%88%ED%95%98%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0](https://velog.io/@arara90/js-Django-Timezone-%EC%A0%81%EC%A0%88%ED%95%98%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)