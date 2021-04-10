---
title: "[TIL] 210315 /ORM"
categories: django
---

## Django Shell에 접속하여 import
```
python manage.py shell
```

```
>> from blog.models import *
```
```blog```의 모든 모델을 가져온다.

<br>

## .objects
Django에서 자동으로 모델 클래스에 기본적으로 추가한 Manager 객체.  
모델과 DB 사이의 인터페이스 역할을 하며 이 Manager를 통해 CRUD 수행.

<br>

## Query set
```object```를 사용하여 다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체가 Query set.

<br>

## Query set이 Evaluate될 때 
```
people_qs = People.objects.filter(active=True)
```
위 처럼 쿼리셋을 변수에 할당하여도 쿼리셋이 아래 예시와 같이 무언가 하기 전까지는 쿼리가 실행되지 않는다.(DB hit X)   
단순히 쿼리셋을 가져왔을 때 쿼리를 날리지 않고 쿼리셋의 정보가 필요하여 쓰이게 될 때 쿼리를 날린다.

> -쿼리셋을 처음 반복(iterate)할 때    
-슬라이싱 할 때, Pizza.objects.all()[:3]  
-pickle 하거나 cache 할 때  
-repr() 이나 len()을 호출 할 때  
-list()를 명시적으로 호출할 때  
-bool(), or, and, if 와 같은 문장에서 사용될 때  

쿼리셋은 평가가 되기 전까지 데이터베이스에 직접 영향을 주지 않으며 쿼리셋이 평가될 때 SQL 쿼리를 데이터베이스에서 실행하게 된다.

```py
a = Drink.objects.prefetch_related('allergy_drink')

for i in a: # for 문에서 처음 쿼리셋(a)이 반복될 때 데이터베이스 히트
    name = a.name
```
---

## Query set을 반환하는 메소드
### all()

```
In  : Post.objects.all()
Out : <QuerySet [<Post: one>, <Post: two>]>
```

### filter()
```
In : Question.objects.filter(id=1)
```

### exclude()
```py
Person.objects.exclude(age=18)
```
```sql
WHERE age != 18;
```

### values(*fields, **expressions)
__rtype__: Dictionary 형태의 Queryset
__fields__: 클래스 속성들(역참조도 가능)
__expression__: 장고 expression(e.g. Count)

```py
Drink.objects.values()

Drink.objects.values('id', 'name', 'category')
```

### value_list(*fields, flat=False, named=False)
__rtype__: Tuple(하나 혹은 여러개)이 담겨져 있는 List

```py
In  : Category.objects.filter(name='브루드커피').values_list()
Out : <QuerySet [(3, '브루드커피', datetime.datetime(2020, 9, 8, 5, 43, 30, 4068, tzinfo=<UTC>), datetime.datetime(2020, 9, 8, 5, 43, 30, 21801, tzinfo=<UTC>)), (4, '브루드커피', datetime.datetime(2020, 9, 8, 5, 43, 30, 4068, tzinfo=<UTC>), datetime.datetime(2020, 9, 8, 5, 43, 30, 21801, tzinfo=<UTC>))]>
```
```values()``` 는 dictionary를 반환한다면 ```value_list()``` 는 tuple을 반환한다. 
출력할 필드를 지정 가능하다.

### select_related(*fields) 
__rtype__: 지정된 *fields가 추가된 queryset
__param__: OnetoOneField, ForeignKey

쿼리가 실행될 때 related 객체를 추가로 sql문 select 안에 모두 담아 원하는 결과를 한 번에 가져온다. (관계가 복잡해질 경우 SELECT에 너무 많은 내용이 들어가기 때문에 n:m은 불가능하다.)
```py
from django.db import models

class City(models.Model):
    # ...
    pass

class Person(models.Model):
    # ...
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

class Book(models.Model):
    # ...
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
```
```py
# Hits the database with joins to the author and hometown tables.
b = Book.objects.select_related('author__hometown').get(id=4)
p = b.author         # Doesn't hit the database.
c = p.hometown       # Doesn't hit the database.

# Without select_related()...
b = Book.objects.get(id=4)  # Hits the database.
p = b.author         # Hits the database.
c = p.hometown       # Hits the database.
```

**prefetch_related(*lookups)**  
prefetch는 SELECT안에 포함시키는 방법이 아니라 각각의 테이블에서 select 해온 후 파이썬에서 Join 을 시켜서 한 쿼리로 만든다.

```py
# from django docs
class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by', on_delete=models.CASCADE)
```
```py
#1 using only prefetch_related
Restaurant.objects.prefetch_related('best_pizza__toppings')
#2 using prefetch & selected
Restaurant.objects.select_related('best_pizza').prefetch_related('best_pizza__toppings')
```
1번의 경우 총 3번의 히트, 2번의 경우 2번의 히트

**annotate()**  

### order_by()
```py
Drink.objects.order_by('nutrition__sodium_mg')
```
다른 모델의 필드로 정렬하기 위해선 ```(__)```를 사용하여 정렬할 수 있다.  
```py
Drink.objects.order_by('name', '-nutrition__sodium_mg')
```
위 처럼 여러 필드를 기준으로 정렬도 가능하다. 위 결과는 ```name``` 필드를 기준으로 오름차순, ```nutrition``` 테이블의 ```sodium_mg``` 필드를 기준으로 내림차순으로 정렬하게 된다.
```py
Drink.objects.order_by('id').order_by('name')
```
```order_by()``` 호출은 이전 ```order_by()``` 를 clear 하여 위의 결과는 id 가 아닌 name 으로 정렬된다.  
```py
Drink.objects.order_by('nutrition')

Drink.objects.order_by('nutrition__id')
```
위 두 가지 쿼리의 결과는 동일하다.
<br>

---

## Query set을 반환하지 않는 메소드

**create()**  
**get()**  
### update()
```py
Entry.objects.update(blog__name='foo') # Won't work!
```
```update()``` 를 사용할 때에는 모델의 메인 테이블만 수정 가능하며 참조 테이블은 수정 불가하다.

**delete()**  
**save()**  
### exist()
```filter()```와 함께 사용하여 조건에 맞는 데이터가 있는 지 조회한 후, 존재하면 ```True```, 존재하지 않으면 ```False```를 반환한다. 
**get_or_create()**
### bulk_create()  
리스트로 한번에 데이터를 입력. 
```
Drink.objects.bulk_create([
     Author(name='아메리카노'),
     Author(name='카페라뗴'),
     Author(name='티'), ])
```
**count()**  
**first()**  
**last()**  
**aggreate()**  

<br>

--- 

## get_object_or_404  
상세 페이지 view에서는 ```get()```을 사용하여 ```try-catch```블록으로 예외처리를 하는 대신 사용하며 인자로는 모델과 해당 모델에서 몇 번째 객체를 가져올 지 결정하는 (ex. pk) 인자를 받고 객체가 존재하지 않을 때 404error를 발생시킨다. 

<br>

## ObjectDoesNotExist
모든 모델에서 사용가능

<br>

## DoesNotExist
특정 모델에게만 사용가능

```py
def ex():
    try:
        return 
    except:
        raise
```

___

## Lookup Filter
```py
Model.objects.filter(필드이름__lookup = value )
```
### __contains

### __icontains

### __startwith
### __endwith
### __gt
지정한 필드 값이 조건 값보다 큰 튜플을 반환한다.  
### __lt
지정한 필드 값이 조건 값보다 작은 튜플을 반환한다.
### __exact
필드 값이 일치하는 튜플을 반환한다. 
### __iexact
대소문자 구별없이 필드 값이 일치하는 튜플을 반환한다. 
### __isnull
### __in
필드 일치 조건을 List 형식으로 입력한다. 

```py
Author.objects.filter(name__in=['spike', 'tyke'])
```
```sql
WHERE name in ('spike', 'tyke');
```

<br>

---

## Q object
[helpful Q object blog](http://www.michelepasin.org/blog/2010/07/20/the-power-of-djangos-q-objects/)

<br>
<br>

---

[https://docs.djangoproject.com/en/2.2/ref/models/querysets/](https://docs.djangoproject.com/en/2.2/ref/models/querysets/)
[http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API](http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API)
[https://wayhome25.github.io/django/2017/07/25/tsd7-django-query-database/](https://wayhome25.github.io/django/2017/07/25/tsd7-django-query-database/)