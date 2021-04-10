---
title: "[Python] Function Parameters"
toc: true
toc_label: "Funtion Parameters"
categories: python
---

## 1. default value parameter와 non-default value parameter
### default value parameter와 non-default value parameter의 순서

+ <b style="weight:60px">default value parameter를 non-default value parameter 앞에 정의 하면 안되는 이유</b>

<img src="https://user-images.githubusercontent.com/26542094/88037471-e87cce80-cb7f-11ea-8240-78ecfc21ba50.png" width="500px">
```py
def love_you(my_name = "정우성", your_name): 
    print(f"{my_name} loves {your_name}") 
```

```py  
> Traceback (most recent call last):   
    File "python", line 1 
SyntaxError: non-default argument follows default argument
```

 매개 변수가 있는 함수를 호출할 때 인수를 넘겨준 순서대로 처리 하게 되는데 만약 위 코드와 같이 default value parameter가 non-default value parameter 앞에 위치 할 경우 default value parameter를 인수로 넘기지 않을 경우 어떤 인수가 non-default인지 나머지 인수들의 순서를 알 수 없기 때문에 기본 값이 없는 인자가 앞에 위치해야 하고 default value parameter를 마지막에 두어야 하는 것 같다.


## 2. 가변 인수
```py
def functionname([formal_args,] *var_args_tuple ):
"function_docstring"
function_suite
return [expression]
```
- 가변 인수는 함수가 몇 개의 인자를 받을 지 정해지지 않은 경우 사용한다. 
- 인수의 앞에   ```*```가 들어가면 해당 인수는 가변 인수를 받는 다는 것을 의미한다.
  
1) <b style="weight:20px">수정 전 코드</b>
```py
def func_param_with_var_args(name, *args, age): 
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
func_param_with_var_args("정우성", "01012341234", "seoul", 20)
```
 ```*args``` 는 <b>임의의 개수의 positional arguments를 받음</b>을 의미한다. 여러 개의 인자를 받은 경우 함수 내부에서는 인수를 튜플로 받은 것 처럼 인식하며 사용자가 몇 개의 인수를 입력 할 지 모르는 상황에서 사용하기 때문에 <i style="background:#dbc6eb; color: #fff"> 인수 목록 중 가장 오른쪽에 한 번만 사용 가능</i>하다.  
위의 코드에서는 age에 20을 할당하기 위해 파라미터를 넘길 때 키워드를 지정해주고 ```age```의 위치를 맨 뒤로 위치하도록 수정하였다.


2) <b style="weight:20px">수정 후 출력 결과</b>
```py
def func_param_with_var_args(name, *args, age):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
func_param_with_var_args("정우성", "01012341234", "seoul", age=20)
```

```py
name=정우성
args=('01012341234', 'seoul')
age=20
```


## 3. 가변 키워드 인수 
```py
def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)
    print('type: ', type(kwargs))
func_kwargs(key1=1, key2=2, key3=3)
# kwargs:  {'key1': 1, 'key2': 2, 'key3': 3}
# type:  <class 'dict'>
```

- 키워드 인수를 이용해서 함수를 호출할 때 <b>미리 정의 되어 있지 않은 키워드 인수를 받으려면</b> 함수를 정의할 때 인수에 ```**```를 사용하여 기술해준다. <b style="background:#BDBDBD; color: #fff">*정해지지 않은 수의 키워드로 이루어진 인자</b>

### 사용 시 주의 사항
```py 
def func_param_with_kwargs(name, age, **kwargs, address=0):
    print("name=",end=""), print(name)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)
func_param_with_kwargs("정우성", "20", mobile="01012341234", address="seoul")
```
```py
Traceback (most recent call last):
  File "python", line 1
    def func_param_with_kwargs(name, age, **kwargs, address=0):
                                                    ^
SyntaxError: invalid syntax
``` 

매개 변수 ```**```는 매개 변수 목록의 가장 오른쪽에만 정의 할 수 있다. 그렇지 않을 경우 위와같이 ```SyntaxError``` 발생. <b style="background:#dbc6eb; color: #fff">kwargs를 마지막에 위치시키도록 수정</b>해준다.

<b style="weight:20px">수정 후 출력 결과</b>
```py
name=정우성
age=20
kwargs={'mobile': '01012341234'}
address=seoul
```

## 4. 가변 인수와 키워드 가변 인수의 위치
1) <b style="weight:20px">수정 전 코드</b>
```py
def mixed_params(name="아이유", *args, age, **kwargs, address):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)
mixed_params(20, "정우성", "01012341234", "male" ,mobile="01012341234", address="seoul")
```
위 수정 전 코드에서 인자 목록 중 ```age```와 ```address```는 <b>위치 인자</b>이며 ```name```은 인수의 <b>defalut 값</b>이 정해져 있다. 위치 인자들은 앞으로 옮기고 ```*args```와 ```**kwargs```는 인자 목록 중 맨 마지막에 위치 해야 할 것 같다. 
```py
def mixed_params(age, address, name="아이유", *args, **kwargs):
....
mixed_params(20, "정우성", "01012341234", "male" ,mobile="01012341234", address="seoul")
```
따라서 위와 같이 수정해 보았는데 또 다시 에러가 발생한다. 이유를 살펴보면, 파라미터를 넘길 때 ```address```는 인수로 <b>"seoul"을 defalut 값</b>으로 넘겨주고 있다. keyword-only arguments는 가변 변수와 가변 키워드 변수의 사이에 위치 해야하기 때문에 <b>위치를 *args 의 뒤에 있도록 수정</b>해주었다.

-> ```age```, ```name="아이유"```, ```*args```, ```address```, ```**kwargs ``` 의 순서로 수정.

2) <b style="weight:20px, font-weight: bold">수정 후 코드</b>
```py
def mixed_params(age, name="아이유",  *args, address, **kwargs ):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)
mixed_params(20, "정우성", "01012341234", "male" ,mobile="01012341234", address="seoul")
```
*참고) https://getkt.com/blog/python-keyword-only-arguments/

