---
title: "[Django project] 인증과 인가"
categories: etc
tag: westagram
toc: true
toc_label: "인증과 인가"
---
인증과 인가는 API에서 가장 자주 구현되는 기능 중 하나이며 private한 API와 public한 API도 모두 기본적인 인증과 인가를 요구한다. 
## 인증(Authentication)
인증을 하기 위해선 먼저 유저의 아이디와 비밀번호를 생성할 수 있는 기능도 필요하며 유저의 identification을 확인하는 절차이다. 
### 로그인 절차
1. 유저 아이디와 비밀번호 생성
2. 유저의 비밀번호를 암호화해서 DB에 저장
3. 유저 로그인 시 -> 아이디와 비밀번호 입력
4. 유저가 입력한 비밀번호를 암호화 한 후 DB에 저장된 암호화시킨 비밀번호와 비교
5. 일치 시 로그인 성공
6. 로그인 성공하면 access token 을 클라이언트에게 전송
7. 유저는 로그인에 성공한 이후로는 request 에 <b style="color:#fff; background:#C4D254">access token</b> 을 첨부해서 서버에 전송함으로서 매번 로그인 하지 않아도 된다. 

### 유저 비밀번호 암호화 
유저의 비밀번호를 그대로 DB에 저장하지 않는다. 
-> DB가 해킹 당하면 유저의 비밀번호도 그대로 노출됨.
-> 외부 해킹이 아니더라도 내부 개발자나 인력이 유저의 비밀번호를 볼 수 있음.
따라서, 유저의 비밀번호는 꼭 암호화해서 저장 해야 한다. 

비밀번호 암호에는 단방향 해쉬 함수(one-wqy hash funtion)가 일반적으로 쓰인다. 

> 단방향 해시 함수는 원본 메시지를 변환하여 암호화된 메시지인 다이제스트(digest)를 생성한다. 원본 메시지를 알면 암호화된 메시지를 구하기는 쉽지만 암호화된 메시지로는 원본 메시지를 구할 수 없어서 단방향성(one-way)이라고 한다. 
예를 들어, "test password"를 hash256이라는 해쉬 함수를 사용하면 0b47c69b1033498d5f33f5f7d97bb6a3126134751629f4d0185c115db44c094e 값이 나온다.
만일 "test password2"를 hash256 해쉬 함수를 사용하면 d34b32af5c7bc7f54153e2fdddf251550e7011e846b465e64207e8ccda4c1aeb 값이 나온다. 실제 비밀번호는 비슷하지만 해쉬 함수 값은 완전히 틀린것을 볼 수 있다. 이러한 효과를 avalance라고 하는데 비밀번호 해쉬 값을 해킹을 어렵게 만드는 하나의 요소이다.

### Bcrypt
- 암호화를 위한 라이브러리
- Rainbow table attack : 미리 해쉬 값들을 계산해 놓은 테이블을 Rainbow table 이라고 한다. 해쉬 함수는 원래 패스워드를 저장하기 위해 설계된 것이 아니라 짧은 시간에 데이터를 검색하기 위해 설계된 것이다. 그렇기 때문에 해시 함수는 본래 처리 속도가 최대한 빠르도록 설계 되었고 이러한 속성 떄문에 공격자는 매우 빠른 속도로 임의의 문자열의 다이제스트와 해킹할 대상의 다이제스트를 비교할 수 있다. 이런 방식으로 패스워드를 추측하면 패스워드가 충분히 길거나 복잡하지 않은 경우에는 그리 긴 시간이 걸리지 않는다. 

#### 취약점 보완
- 단방향 해쉬 함수의 취약점을 보완하기 위해 다음과 같이 일반적으로 2가지 보완점들이 사용된다. 
- <b style="color:#fff; background:#52BBD0">Salting</b> : 실제 비밀번호 이외에 추가적으로 랜덤 데이터를 더해서 해시 값을 계산하는 방법
- <b style="color:#fff; background:#52BBD0">Key Stretching</b> : 단방향 해쉬 값을 계산 한 후 그 해쉬 값을 또 해쉬 하고 또 이를 반복하는 것을 말한다. 
- 최근에는 일반적인 장비로 1초에 50억개 이상의 다이제스트를 비교할 수 있지만 키 스트레칭을 적용하여 동일한 장비에서 1초에 5번 정도만 비교할 수 있게 한다. GPU를 사용하더라도 수백에서 수천 번 정도만 비교할 수 있다.  
  
<img src = "https://stackoverflow.com/c/wecode/images/s/84e03dec-a4c9-4bc4-ada4-cffcea75c905.png">
- Salting과 Key Stretching을 구현한 해쉬 함수 중 가장 널리 사용되는 것이 <b style="color:#fff; background:#52BBD0">bcrypt</b>이다. 

```py
In [40]: import bcrypt

In [41]: bcrypt.hashpw(b"secrete password", bcrypt.gensalt())
Out[41]: b'$2b$12$.XIJKgAepSrI5ghrJUaJa.ogLHJHLyY8ikIC.7gDoUMkaMfzNhGo6'

In [42]: bcrypt.hashpw(b"secrete password", bcrypt.gensalt()).hex()
Out[42]: '243262243132242e6b426f39757a69666e344f563852694a43666b5165445469397448446c4d366635613542396847366d5132446d62744b70357353'
```

## 인가 (Authorization)
인가는 권한 부여라고 할 수 있다. 유저가 요청하는 request를 실행 할 수 있는 권한이 있는 유저인가를 확인하는 절차이다. 
인가 또한 JWT를 통해서 구현 되는데 ```access token``` 을 통해 해당 유저의 정보를 얻을 수 있어 유저가 가지고 있는 권한도 확인 할 수 있다. 

### Authorization 절차
1. ```access token``` 을 생성한다.
2. 유저가 request를 보낼 때 ```access token``` 을 첨부해서 보낸다.
3. 서버는 유저가 보낸 ```access token``` 을 복호화 한다. 
4. 복호화된 데이터를 통해 유저 아이디를 얻는다.
5. 유저 아이디를 통해 DB에서 해당 유저의 권한을 확인한다. 
6. 유저가 충분한 권한을 가지고 있으면 해당 요청을 처리한다. 
7. 유저가 권한을 가지고 있지 않으면 Unauthorized Response(401) 혹은 다른 에러 코드를 보낸다.

### JWT (JSON Web Tokens)
- 로그인에 성공한 후에는 <b style="color:#fff; background:#C4D254">access token</b>이라고 하는 암호화 된 유저 정보를 request header 에 담아 보내게 되는데 JWT 는 <b style="color:#fff; background:#C4D254">access token</b> 을 생성하는 방법 중 하나이다. 
- 유저 정보를 담은 JSON 데이터를 암호화해서 클라이언트와 서버간 주고 받는 것을 말한다. 

---

#### JWT의 구조
<b style="color:#fff; background:Red">aaaaaa</b>.<b style="color:#fff; background:orange">bbbbbb</b>.<b style="color:#fff; background:green">cccccc</b>

<b style="color:red;"> 헤더(header)</b>, <b style="color:orange;">내용(payload)</b>, <b style="color:green;">서명(signature)</b>  

<img src="https://cdn-images-1.medium.com/max/1600/1*jU2iAYGT1FuHN597AiIMuw.png">
<img src="https://cdn-images-1.medium.com/max/1600/1*dYWLrQkc9CjudRZiL7b-BQ.png" width = '400px'>
<img src="https://cdn-images-1.medium.com/max/1600/1*qoHqEPqXYAk9Vf_p5hVhnQ.png" width = '700px'>

+ <b style="color:#fff; background:Red">헤더</b> : <b>토큰의 타입과 해시 알고리즘 정보</b>가 들어간다. 예) {"alg:"HS256", "typ":"JWT"}  
헤더의 내용은 BASE64 방식으로 인코딩 해서 JWT의 가장 첫 부분에 기록된다.   
*인코딩 - 정보의 형태나 형식을 표준화, 보안, 처리 속도 향상, 저장 공간 절약 등을 위해서 다른 형태나 형식으로 변환하는 처리 혹은 그 처리 방식을 말한다.   
*BASE64 - Binary Data를 Text로 바꾸는 인코딩의 하나로 Binary Data 를 Character set에 영향을 받지 않는 공통 ASCII 영역의 문자로만 이루어진 문자열로 바꾸는 인코딩이다. 
+ <b style="color:#fff; background:orange">내용 (payload)</b> : 내용에는 exp와 같이 <b>만료시간을 나타내는 공개 클레임, 그리고 클라이언트와 서버간 협의하에 사용하는 비공개 클레임</b> 두 가지 요소를 조합하여 작성한 뒤 BASE64 인코딩하여 두 번째 요소로 위치한다. 예) {"user-id":1, "exp":1539517391} *단지 BASE64 인코딩한 것이므로 누구나 원본을 볼 수 있으니 개인정보를 보내면 안된다. 유저 아이디와 같이 식별은 가능하지만 다른 사람이 봤을 때 알 수 없는 내용으로!
+ <b style="color:#fff; background:green">서명</b> : JWT가 원본 그대로라는 것을 확인 할 때 사용하는 부분이다. 시그니쳐는 BASE64URL 인코드된 header와 payload 그리고 JWT secret(별도 생성)을 헤더에 지정된 암호 알고리즘으로 암호화하여 전송한다. (복호화 가능) 프론트 엔드가 JWT를 백엔드 API 서버로 전송하면 서버에서는 전송받는 JWT의 서명 부분을 복호화 하여 서버에서 생성한 JWT가 맞는 지 확인한다. 

생성된 JWT 예시) <b style="color:red;">eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9</b>.<b style="color:orange;">eyJpZCI6MX0</b>.<b style="color:green;">WMlRKTbLJBKLCDXLz2tpIOaDWCuHxlGwmWaVVfE6hKU</b>

---

<b> \<유저 로그인 예시\> </b>
```
POST /auth HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "username": "joe",
    "password": "pass"
}
```
<b>\<access token 예시\></b>
```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E"
}
```
서버에서는 ```access token``` 을 복호화해서 해당 유저 정보를 얻게 된다. 

예) 
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3Nj
QwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E
를 복호화 하면 다음과 같은 정보를 얻게 되고 유저 아이디를 통해 해당 유저가 누군지 알 수 있다. 
```py
{
    user_id = 1 
}
```

<img src = "https://stackoverflow.com/c/wecode/images/s/e3383b10-d296-4790-a8e3-e1c9a2daa41d.png" width = "500">{:.aligncenter} 

---

## Decorator
진행하고 있던 프로젝트에 유저의 권한을 확인하는 로직을 추가했다. 먼저 pyjwt 라이브러리 설치 후 import 해주었고 아래와 같이 별도의 함수를 만들어 호출하여 사용했다. 유저가 특정 기능에 접근하려고 할 때 권한이 있는지 먼저 확인하고 싶은데 이럴 경우 데코레이터를 사용하면 된다. 데코레이터는 보통 ```utils.py```파일을 만들어 관리한다. 

```py
# User/utils.py

import jwt 

def make_token(id):
    access_token = jwt.encode({'id' : id}, SECRET_KEY, algorithm = 'HS256')
    return access_token

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.headers.get('Authorization', None)
        if access_token is not None:
            payload = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
        else:
            JsonResponse({"message": 'INVALID_USER'}, status=401)
        try:
            user = User.objects.get(id = payload['id'])
            request.user = user
        except jwt.DecodeError:
            return JsonResponse({"message" : 'EXPIRED_TOKEN'}, status = 401)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'NO_EXISTS_USER'}, status=404)
        return func(self, request, *args, **kwargs)
    return wrapper
```  
+ make_token  
[1] id 값을 사용해 토큰을 만든다.  
[2] ```SECRET_KEY```는 프로젝트 내에서만 이용해야하기 때문에 공개되어서는 안된다. 따라서 프로젝트시엔 따로 파일을 두고 git에는 공유하지 않는다.  
[3] 딕셔너리를 JSON으로 변환하기 위해서는 일반적으로 string으로 직렬화하여 전달해야하지만 직렬확가 정의되지 않은 byte array로 전달하면 type error가 발생하기 때문에 decode('utf8') 함수를 사용하여 byte array를 string으로 변환하여 수정한다.   

+ login_required  
[1] request의 headers 에서 'Authorization' 을 찾고 만약 토큰이 있다면 access_token에 넣는다.  
[2] access_token의 값이 NULL 이 아니라면 payload 변수에 토큰이 decode 된 값 (encode 시 사용한 ```id```데이터) 을 저장한다. 토큰 값이 NULL 일때는 INVALID_USER 메세지를 보낸다.  
[3] ```except jwt.DecodeError:``` -> 존재하지 않는 토큰 값일 경우  
[4] ```except User.DoesNotExist:``` -> 토큰은 제대로 존재하지만 사용자 정보가 없을 경우


```py
#User/views.py

class Signin(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])
                password = user.password
                input_password = data['password']
                if bcrypt.checkpw(input_password.encode('utf-8'), password.encode('utf-8')):
                    at = make_token(user.id).decode('utf-8')
                    return JsonResponse({'access_token' : at}, status = 200)
                return JsonResponse({'message' : 'INVALID_USER'}, status = 400)
            return JsonResponse({'message' : 'NO_EXISTS_USER'}, status = 404)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

```
+ Signin class  
[1] user 변수에 입력된 email 과 데이터베이스에 저장된 email을 비교해 일치하는 데이터를 가져와 저장한다.   
[2] 데이터베이스에 저장된 password 정보와 입력된 패스워드 정보를 각각 utf-8 로 encode 하여 데이터 타입을 ```Bytes``` 로 바꿔준다. 그리고 ```checkpw``` 메소드를 통해 비교하여 True 값이 반환된다면 토큰을 발급하고 메세지로 넘겨준다. 

+ bcrypt의 암호화 방법  
bcrypt는 str 데이터가 아닌 Bytes 데이터를 암호화하기 때문에 암호화 시엔 bytes 화 해야한다. 파이썬에서는 str을 encode 하면 bytes(이진화)되고 bytes를 decode 하여 str 화 한다. 이 때 우리가 인식 할 수 있는 형태로 변환하기 위해 'UTF-8' 유니코드 문자 규격을 사용한다. 


---

참고 자료) https://effectivesquid.tistory.com/entry/Base64-%EC%9D%B8%EC%BD%94%EB%94%A9%EC%9D%B4%EB%9E%80, https://kibua20.tistory.com/69