---
title: "[Django]"
categories: 
---
```
python manage.py shell
```

```
>> from blog.models import *
```
blog App의 모든 모델을 가져온다.

## .objects
Django에서 자동으로 모델 클래스에 기본적으로 추가한 Manager 객체.
이 Manager를 통해 CRUD 수행.


## Query set


https://docs.djangoproject.com/en/2.2/ref/models/querysets/#annotate
http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API