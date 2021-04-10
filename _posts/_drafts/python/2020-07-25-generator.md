---
title: "[Python] generator"
categories: python
---
## generator
파이썬에서 보통의 함수는 값을 반환하고 종료하지만 제너레이터 함수는 값을 반환하기는 하지만 산출(yield)한다는 차이점이 있다. 또한 제너레이터는 이터레이터를 생성해주는 함수라고도 볼 수 있으며 함수 안에서 yield 키워드를 사용한다. 제너레이터를 dir로 함수 종류를 확인해보면 이터레이터와는 다르게 ```__iter__```와 ```__next__```함수가 둘 다 들어있다. 

```python
print("dir gen =", end=""), print(dir(generator_squares()))

dir gen =['__class__', '__del__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__',
'__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
```

그래서 이터레이터 처럼 ```__iter__```를 호출한 후에 ```__next__```함수를 호출하지 않아도 ```__next__```를 바로 호출할 수 있다. 
```py
>>> def test_generator():
...     yield 1
...     yield 2
...     yield 3
... 
>>> gen = test_generator()
>>> type(gen)
<class 'generator'>
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
```py
gen = generator_squares()
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

출력결과
0
1
4
Traceback (most recent call last):
  File "generator.py", line 14, in <module>
    print(gen.__next__())
StopIteration
```
위와 같이 생성한 제네레이터는 iterable한 객체가 되며 for문에서 사용할 수 있다. 그리고 제너레이터 함수는 아래와 같이 실행중에 send 함수를 통해서 값을 전달 할 수도 있다. 
```py
def generator_send():
    received_value = 0

    while True:

        received_value = yield
        print("received_value = ",end=""), print(received_value)
        yield received_value * 2

gen = generator_send()
next(gen)
print(gen.send(2))

next(gen)
print(gen.send(3))

출력결과
received_value = 2
4
received_value = 3
6
```

## generator expression
제너레이터 표현식은 lazy evaluation을 위해 사용될 수 있으며 리스트 컴프리헨션 문법과 비슷하지만 대괄호가 아닌 괄호를 사용하며 만든다. 
```py
L = [ 1,2,3]
def generate_square_from_list():
    result = ( x*x for x in L )
    print(result)
    return result
def print_iter(iter):
    for element in iter:
        print(element)

print_iter( generate_square_from_list() )
```
__출력 결과__
```py
<generator object generate_square_from_list.<locals>.<genexpr> at 0x7fca1f930ba0>
1
4
9
```

---
## Lazy Evaluation
Lazy Evaluation은 어떤 값이 실제로 쓰일 때 까지 그 값의 계산을 뒤로 미루는 동작 방식이다.  

1) 장점  
- 실제로 값이 쓰일 경우에만 함수를 수행하므로 연산하고 메모리 할당까지 다 했지만 실제로 데이터를 사용하지 않을 경우 낭비가 발생할 수 있기 다. 따라서 lazy evaluation을 활용할 경우 시간과 메모리를 절약할 수 있는 장점이 있다. 

2) 단점  
- 항상 lazy evaluation을 사용하는 것이 효율적이지는 않다. 출력 시점에 아주 큰 리스트의 계산을 한 번에 수행해야 하는 경우 이미 결과 값을 담아두고 출력할 경우와 비교해 메모리 오버헤드가 발생할 수 있다. 

3) 리스트 컴프리헨션과의 차이점  
```py
import time
L = [ 1,2,3]
def print_iter(iter):
    for element in iter:
        print(element)

def lazy_return(num):
    print("sleep 1s")
    time.sleep(1)
    return num

print("comprehension_list=")
comprehension_list = [ lazy_return(i) for i in L ]
print_iter(comprehension_list)

print("generator_exp=")
generator_exp = ( lazy_return(i) for i in L )
print_iter(generator_exp)
```
__출력 결과__
```
comprehension_list=
sleep 1s
sleep 1s
sleep 1s
1
2
3
-----------------------------------
generator_exp=
sleep 1s
1
sleep 1s
2
sleep 1s
3
```
위 출력 결과를 보면 리스트 컴프리헨션의 경우 lazy_return() 함수를 호출하면 호출되는 즉시 함수를 실행하고 generator 표현식을 통해 만들 경우 lazy_return() 함수를 호출할 때는 sleep() 함수가 바로 실행되지 않는다는 것을 볼 수 있다. 리스트 컴프리헨션의 경우 comprehension_list의 실제 사용 여부와 상관없이 sleep 1s 가 출력 되는 것으로 볼 때 데이터를 미리 만들어 둔다는 것을 알 수 있고 제너레이터 표현식으로 만들 경우 실제로 generator_exp을 사용하는 경우에만 함수를 수행하는 것을 알 수 있다. 
