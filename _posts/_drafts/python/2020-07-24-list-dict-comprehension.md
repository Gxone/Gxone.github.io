---
title: "[Python] List Comprehension / Dictionary Comprehension"
categories: python
---
## list comprehension
list comprehension 이란 리스트를 쉽게 생성하기 위한 간단한 표현식이며 리스트와 마찬가지로 대괄호```[,]```를 사용한다. 
>[표현식 for 원소 in 반복 가능한 객체]  
    [표현식 for 원소 in 반복 가능한 객체 if문]

1부터 10까지를 가지는 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 를 만들 때 다음과 같이 리스트를 생성할 수 있다.
```python
new_list = [ x for x in range(1, 11) ]
print(new_list)
``` 
```py
odd_numbers = []
for element in range(1, 11):
    if (element % 2) ==  1:
        odd_numbers.append(element)
```
위와 같은 코드를 다음과 같이 리스트 컴프리헨션으로 간단하게 바꿀 수 있다.
```py
odd_numbers = [element for element in range(1, 11) if (element % 2) == 1]
print(odd_numbers)
```
성능 개선을 하기 위해 리스트 컴프리헨션을 사용하기도 하지만 모든 상황에서 리스트 컴프리헨션이 만등은 아니다. 예를 들어 코드의 가독성을 위해서는 여러 줄의 표현식과 조건문으로 표현하는 것이 이중 for문의 복잡한 리스트 컴프리헨션 한 줄로 코딩하는 것 보다 나은 경우도 있다. 

## Ditionary Comprehension
> {Key:Value for 요소 in 반복 가능한 객체 [if 조건식]}
출력 표현식이 Key:Value Pair로 표현된다는 점이 다르며 결과로 dictionary 가 리턴된다. 

--- 
```py
def test1():
    cities = ["Tokyo", "Shanghai", "Jakarta", "Seoul", "Guangzhou", "Beijing", "Karachi", "Shenzhen", "Delhi"]
    rslt = [i for i in cities if not i.startswith("S")]
    print(rslt)
test1()
```
```py
def test2():
    population_of_city = [('Tokyo', 36923000), ('Shanghai', 34000000), ('Jakarta', 30000000), ('Seoul', 25514000),
                          ('Guangzhou', 25000000), ('Beijing', 24900000),
                          ('Karachi', 24300000), ( 'Shenzhen', 23300000), ('Delhi', 21753486) ]
    dict = {key:val for key, val in population_of_city}
    
    print(dict)

test2()
```