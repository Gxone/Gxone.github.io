---
title: "[TIL] 210325"
categories: django
---
## ArrayField
> class ArrayField(base_field, size=None, **options)

PostgreSQL 의 model field 중 하나이다.

### base_field 
ArrayField 에 들어가는 하위 클래스를 지정해주어야 하며 *필수 인자*이다.

### size
*option*  

---
[공식 문서](https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/fields/)