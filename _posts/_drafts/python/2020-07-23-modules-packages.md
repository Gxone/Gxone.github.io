---
title: "[Python] Modules and Packages"
toc: true
toc_label: "Modules and Packages"
categories: python
---
## How import statement finds modules and packages
### 1. sys.modules 와 sys.path의 차이점
#### 1) sys.modules  
파이썬이 모듈이나 패키지를 찾기 위해 __가장 먼저 확인 하는 곳__ 이다. sys.modules는 <b>dictionary 이며 이미 import된 모듈과 package들을 저장</b>하고 있다. 따라서 새로 import하는 모듈은 sys.modules에서 찾을 수 없으며 한 번 import된 모듈과 패키지들은 또 다시 찾지 않아도 된다.  

#### 2) sys.path  
__sys.path는 list이며 string 요소들을 가지고 있다.__ 아래와 같이 각 string 요소들은 경로를 나타낸다. 파이썬은 list의 각 경로를 하나씩 확인하며 해당 경로에 import 하려는 패키지가 있는지 확인한다. 
```
['',
'/Users/song-eun-u/anaconda3/bin',
'/Users/song-eun-u/anaconda3/lib/python36.zip',
'/Users/song-eun-u/anaconda3/lib/python3.6',
'/Users/song-eun-u/anaconda3/lib/python3.6/lib-dynload',
'/Users/song-eun-u/anaconda3/lib/python3.6/site-packages',
'/Users/song-eun-u/anaconda3/lib/python3.6/site-packages/aeosa',
'/Users/song-eun-u/anaconda3/lib/python3.6/site-packages/IPython/extensions',
'/Users/song-eun-u/.ipython']
```
#### 3) built_in modules
파이썬에서 제공하는 __파이썬 공식 라이브러리들__ 이다. Built-in 모듈들은 이미 파이썬에 포함되어 나오므로 파이썬이 쉽게 찾을 수 있다.
> 파이썬은 import하고자 하는 모듈과 패키지를 찾을 때 먼저 sys.modules를 보고, 없으면 built-in 모듈을 확인하고 마지막으로 sys.path에 지정되어 있는 경로들을 확인해서 찾는다. sys.path에서도 못찾으면 ModuleNotFindError를 리턴한다. 

### 2. sys 모듈의 위치
sys 모듈은 파이썬에 이미 내장되어있는 모듈 중 하나이다. 따라서 bulit-in 모듈에 존재하고 있다. 
sys를 import 하고 sys.modules를 출력하면 다음과 같이 built-in 된 모듈 인 것을 알 수 있다. 
```py
{'sys': <module 'sys' (built-in)>
...
```

### 3. Absolute path와 Relative path의 차이점
```
└── my_app
    ├── main.py
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── package2
        ├── __init__.py
        ├── module3.py
        ├── module4.py
        └── subpackage1
            └── module5.py
```
#### 1) Absolute path
import를 하는 파일이나 경로에 상관없이 항상 경로가 동일하다. 
위 경로에서 package1과 package2를 import하면 다음과 같다. 
```py
from package1 import module1
from package1.module2 import function1
from package2 import class1
from package2.subpackage1.module5 import function2
```
이미 my_app 프로젝트 안에 있으므로 my_app은 생략된다. 
프로젝트 내에서는 어느 파일, 위치 에서 import 하던지 경로가 항상 위와 같이 동일히다. 
일반적으로 로컬 패키지를 import할 때 절대 경로를 사용하면 된다. 하지만 이 때 경로가 길어질 수 있어 이를 보완하기 위해 relative path를 사용할 수 있다. 

#### 2) Relative path
Relative path는 absolute path와 다르게 최상단이 아닌 import하는 위치를 기준으로 한다. 일반적으로 로컬 패키지 안에서 다른 로컬 패키지를 import 할 때 사용된다.
```py
# package2/module3.py (현재 위치)
from . import class1
from .subpackage1.module5 import function2
```
```.```은 import가 선언되는 파일의 현재 위치이다. ```..```로 표현할 경우엔 현재 위치에서 상위 디렉토리로 가는 경로이다.
상대 경로는 경로의 길이를 줄여주는 장점이 있지만 파일 위치가 변경되면 경로도 수정해주어야 하는 단점이 있다.
*웬만한 경우 절대 경로 사용을 권장

### 5. main module에서의 import
__main.py__
```py
# absoulte path
#from calculator.add_and_multiply import add_and_multiply 
# relative path
from .calculator.add_and_multiply import add_and_multiply

if __name__ == '__main__':
    print(add_and_multiply(1,2))
```

__add_and_multiply.py__
```py
from .multiplication import multiply
# from calculator.multiplication import multiply
def add_and_multiply(a,b):
    return multiply(a,b) + (a+b)
```

__multiplication.py__
```py
def multiply(a,b):
    return(a*b)
```
위 ```main.py``` 파일을 run하면 다음과 같은 에러가 발생한다. 
```py
Traceback (most recent call last):
  File "/Users/gxone/djangoPrac/calculator/main.py", line 5, in <module>
    from .calculator.add_and_multiply import add_and_multiply
ValueError: Attempted relative import in non-package
```
이유를 찾아보면 상대 경로는 현재 모듈의 이름에 기반하지만 메인 모듈의 이름은 항상 ```__main__```이기 때문에 절대 경로를 사용해야 한다고 한다. 파이썬은 최초로 시작하는 스크립트 파일과 모듈의 차이가 없어 어떤 스크립트 파일이든 시작점도 될 수 있고, 모듈도 될 수 있어 ```if __name__ == '__main__':```처럼 ```__name__```변수의 값이 \'__main\_\_\'인지 확인하는 코드는 현재 스크립트 파일이 메인 프로그램으로 사용 될 떄와 모듈로 사용될 때를 구분하귀 위해 프로그램의 시작점이 맞는지 판단하는 작업이라고 한다. 따라서 ```__name__```이 import 하는 위치의 기준이 되는데 main.py에서는 ```__name__```이 ```__main__```이 되기 때문에 경로를 찾지 못하는 것 같다. 다음과 같은 예를 보면,

__hello.py__
```py
print('hello 모듈 시작')
print('hello.py __name__:', __name__)    # __name__ 변수 출력
print('hello 모듈 끝')
```
__main.py__
```py
import hello    # hello 모듈을 가져옴
 
print('main.py __name__:', __name__)    # __name__ 변수 출력
```
__실행 결과__
```
hello 모듈 시작
hello.py __name__: hello
hello 모듈 끝
main.py __name__: __main__
```
hello 모듈과 main 모듈에서 각각 __name__을 출력해 보았을 때 hello 모듈의 경우 "hello" 그대로 출력 되지만 main 모듈의 경우엔 \"__main\_\_\"으로 출력되는 것을 볼 수 있다. 

### 6. \_\_init\_\_.py 
__init\_\_.py 파일은 파이썬 패키지를 생성하면 자동으로 생성되는 파일이다. 이 파일의 역할은 이 파일이 존재하는 디렉터리는 패키지의 일부임을 알려주는 역할이다. 따라서 __init\_\_.py 파일이 없을 경우 디렉터리는 패키지로 인식되지 않는다. 
