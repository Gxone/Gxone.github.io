---
title: "[Django] 프로젝트 초기 세팅"
categories: python django
---
## 1. 가상 환경
1. 가상 환경은 매 프로젝트마다 필요한 환경이 조금씩 다를 수도 있기 떄문에 프로젝트마다 하나씩 생성하는 것을 추천한다. 이 환경에서는 파이썬 3.8 버전이 설치된다.
```
conda create -n 가상환경이름 python=3.8
```
2. 가상환경 활성화
```
conda env list 
```
```
conda activate 가상환경이름
```

## 2. Django 설치
1. 실행시킨 가상환경에 django 를 설치한다. 
```
pip install django
```
이 외에도 ```jango-cors-headers```, ```selenium```, ```PyJWT```, ```bcrypt```, ```mysqlclient``` 등이 필요하다면 설치한다. 

2. django 를 설치했다면 프로젝트를 생성한다. 
```
django-admin startproject 프로젝트이름
```

## 3. 기본 설정 
1. INSTALLED_APP 에서 사용하지 않을 앱 삭제
```py
# (프로젝트이름/settings.py)
INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    ...
]
```

2. MIDDLEWARE에서도 csrf관련 요소와 auth관련 요소를 주석 처리 한다.
```py
MIDDLEWARE = [
    ...
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
]
```

3. ALLOWED_HOSTS 추가
```
ALLOWED_HOSTS = ['*']
```

4. INSTALLED_APPS와 MIDDLEWARE 에 corsheaders 추가
프론트엔드와 통신 할 때는 서로 다른 port 로 접속을 시도한다. 이를 허용해주기 위해 corsheaders 를 추가한다. 
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]
```
```py
  MIDDLEWARE = [
	...
		'corsheaders.middleware.CorsMiddleware',
]
```
5. CORS 관련 허용 사항 추가  
```py
##CORS
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
		#만약 허용해야할 추가적인 헤더키가 있다면?(사용자정의 키) 여기에 추가하면 된다.
)
```

6. urls.py  
admin 을 사용하지 않을 경우 [1]과 [2] 코드를 제거한다. 
```py
from django.contrib import admin ----- [1]
urlpatterns = [
    path('admin/', admin.site.urls), - [2]
]
```


## 4. .gitignore  
[https://www.toptal.com/developers/gitignore](https://www.toptal.com/developers/gitignore)   
소스를 공유하기 위해 깃을 사용하고 싶지만 올리고 싶지 않은 것과 올려서는 안되는 것들을 구분하기 위해 깃이 설치된 디렉토리에 ```.gitignore```파일을 생성해서 관리해야 한다. 위 사이트에서 사용하는 환경에 해당하는 키워드를 입력하면 자동으로 파일에 정의할 요소들을 생성해준다.  
python, django, pycharm, vscode, vim, macos 등
```
cd '프로젝트 폴더명'
touch .gitignore
vi .gitignore
```
또한 이 후 보안을 위한 설정을 위해 ```my_settings.py```와 ```secrets.json``` 파일 또한 깃에 공유하지 않도록 추가한다.
```py
### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
db.sqlite3-journal
media
.idea/
my_settings.py
secrets.json
```

## 5. requirements.txt
협업 시 동일한 환경 구성을 위해 정보를 전달해야 한다. 아래 명령어는 현재 로컬 환경에 설치된 파이썬 모듈 정보를 보여주는 명령어이며 ```> requirements.txt``` 를 통해 파일에 저장한다. 
```
pip freeze > requirements.txt
```

## 6. 보안을 위한 설정  
장고 설정에 존재하는 내용 중 ```SECRET_KEY```,  ```DATABASE``` 등은 소스로서 공유해야하는 내용이 아니다. 따라서 ```settings.py``` 에 그냥 기록되는 것은 지양하고 별도의 파일 또는 환경 변수로서 관리하는 것이 좋다. 

my_setting.py 파일을 생성하고 settings.py 에 있던 정보를 옮겨 작성한다. 이때 해싱 알고리즘에 관한 정보 또한 드러나면 안되는 정보이다.
```py
# my_settings.py
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'airbnb',
        'USER': 'root',
        'PASSWORD': 'qweasd123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
ALGORITHM = 'HS256'
```
```py
# settings_py
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
SECRET_KEY = get_secret("SECRET_KEY")
...
# SECURITY WARNING: keep the secret key used in production secret!
ALGORITHM_KEY = my_settings.ALGORITHM
...
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = my_settings.DATABASES
```


## 7. 추가 사항
1. 지역과 시간을 바꿔준다.
```py
# settings.py
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
```

2. 프로젝트의 urls.py 에 ```/``` 없을 경우 생기는 경고를 더 이상 띄우지 않게 해준다.
```py
# settings.py
#REMOVE_APPEND_SLASH_WARNING
APPEND_SLASH = False
```

## 8. Git
프로젝트 폴더에서 깃 저장소를 만들고 원격 저장소와 연결한다. 
```
git init
git remote add ..
git branch -M master
git add .
git push origin master
```
