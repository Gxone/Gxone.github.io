---
title: "[replit] Django"
categories: python django
---
## Django
- views.py : 로직을 담당하는 파일이다. 앞으로 장고 프로젝트를 진행하면서 제일 많이 다루게 될 파일이다.  
- migrations 디렉토리 : model.py 파일에 정의한 테이블 구조를 manage.py의 makemigration 옵션을 통해 생성되는 파일이 저장되는 디렉토리이다.  
- models.py : 장고의 핵심 기능 중 하나인 ORM과 관련되어 있는 파일이다. 단순하게는 데이터베이스의 테이블을 정의하는 파일이라고 생각하면 된다.  
- settings.py : 프로젝트 관련 모든 설정 정보를 담고 있는 파일이다.  
- urls.py : url 경로에 대한 파일이다. 
- Json(JavaScript Object Notation) : 데이터 타입  
 
### views.py
```python
import json
from django.views import View
from django.http import JsonResponse

class MainView(View):
    def get(self, request):
		    return JsonResponse({"Hello":"World"}, status=200)
```
View 클래스는 장고 프레임 워크에 내장된 클래스를 상속받아 사용한다. View 클래스 안에는 다양한 메소드가 존재하며 이는 장고를 사용하게 쉽게 해준다. 
JsonResponse는 서버의 요청에 대한 응답을 Json으로 응답하기 위해 사용한다. 
def get 함수는 View 클래스에 내장된 메소드이다. 
이 함수는 HTTP 통신 메소드 중 GET 메소드로 오는 호출에만 응답하게 되어있다. 

### urls.py
```python
from django.urls import path
from .views  import MainView

urlpatterns = [
    path('', MainView.as_view()) 
]
```
1. 장고에서 url 경로를 처리하기 위한 모듈을 import하는 코드
2. views 파일 안에 있는 MainView 클래스를 임포트 하는 코드
4. 장고에서 경로를 명시할 때 항상 urlpatterns 와 같은 리스트 안에 경로를 저장하고 읽어 들인다.
as_view() 메소드는 현재 주소인 나를 호출하면 그 호출을 한 http 메소드가 GET, POST, DELETE, PUT 인지 등을 판별해 그에 맞는 함수를 실행시켜준다.

### models.py
장고에서는 SQLite3 라는 파일 기반의 경량화된 DB를 기본 제공하고 있다. 따라서 장고를 설치해서 사용하는 것 만으로도 사용할 수 있는 DB가 존재하고 이를 장고에서 컨트롤 하기위해 ORM이라는 것을 제공한다. 
### ORM (Object Relational Mapping, 객체-관계 매핑)
> 객체와 관계형 데이터베이스의 데이터를 자동으로 연결해주는 것을 말한다. 객체 지향 프로그래밍은 클래스를 사용하고, 관계형 데이터베이스는 테이블을 사용한다. 객체 모델과 관계형 모델 간에 불일치가 존재한다. ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하여 불일치를 해결한다. 
데이터베이스의 데이터 <--매핑--> Object 필드
객체를 통해 간접적으로 데이터베이스 데이터를 다룬다.
