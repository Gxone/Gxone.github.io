---
layout: post
title: "인가 (Authorization)"
blog: true
text: true
post-header: true
header-img: "img/header.jpg"
category: "WEB"
date: "2021-07-04"
---
# 인가 
<b class='post-subtitle'>Authorization</b>
> request를 실행할 수 있는 권한이 있는 유저인지 확인하는 절차

HTTP는 ```stateless protocol```에 속합니다. 프로토콜이 상태 정보를 저장할 경우 매우 복잡해지고 overhead가 발생할 수 있어 stateless protocol에서 서버는 클라이언트의 상태 정보를 유지하지 않습니다. 하지만 웹 서비스를 개발하다 보면 여러 요청에 대한 이전 상태의 정보가 필요한 경우가 있습니다. 예를 들어, 최초 로그인 이후에도 로그인 인증 정보가 유지되어 새로운 유저가 아닌 로그인된 유저로 인식되도록 하거나 유저마다 다른 정보를 제공하는 등의 stateful 한 통신이 필요합니다. 이러한 기능을 위해 세션, 쿠키 또는 웹 스토리지를 활용하여 상태 정보를 저장하고 서버가 클라이언트를 판별할 수 있도록 합니다.  

## 세션 기반 인증
![세션 기반 인증](img/session.png)
1. 로그인
2. 서버는 유저 정보 확인 후 세션 생성
3. 서버는 그 세션의 세션 ID를 쿠키 형태로 클라이언트에게 전송
4. 클라이언트는 세션 ID를 브라우저에 저장
5. 클라이언트는 세션 ID를 HTTP 요청과 함께 전송
6. 서버는 세션 ID를 통해 유저 정보 확인
7. HTTP 응답  

세션 기반 인증 방식에서 브라우저에는 유저에 해당하는 세션 ID만을 저장하고 개인 정보 등은 저장하지 않습니다. 서버의 세션에는 해당 유저 ID, 로그인 상태, 마지막 로그인 시간, 만료 기한 등의 정보를 저장합니다.

### 세션 기반 인증 방식의 장단점
- 장점
    - 서버에서 데이터를 관리하기 때문에 상대적으로 안전  
    
- 단점
    - 세션 ID를 모든 서버에서 접근 할 수 있도록 하기 위해서는 redis와 같은 중앙 세션 저장소가 필요
    - 세션 저장소에 장애가 일어나면 시스템 전체에 문제가 발생
    - 서버에서 세션을 관리하며 overhead 발생

## 토큰 기반 인증
![JWT](img/token.png)
1. 로그인
2. 서버는 유저의 정보를 secret key로 JWT 생성
3. 서버는 생성한 JWT를 클라이언트에게 전송
4. 클라이언트는 JWT를 브라우저에 저장
5. 클라이언트는 JWT를 HTTP 요청과 함께 전송
6. 서버는 secret key를 사용하여 JWT을 decode하여 유저 정보 확인
7. HTTP 응답

### 토큰 기반 인증 방식의 장단점
- 장점
    - 추가 저장소가 필요 없어 서버 부하가 없고 서버를 확장하기에 유리
- 단점
    - 토큰의 payload 부분을 decode 하여 사용자의 개인 정보를 탈취할 수 있어 보안 측면에서 세션 기반 인증 방식보다 위험
    - 이미 발급된 토큰은 유효기간이 만료될 때까지 삭제 불가능

<br>

> 세션 기반 인증 방식과 토큰 기반 인증 방식을 비유해서 표현하자면 세션은 ```신용카드 또는 체크카드```, 토큰은 ```신분증```에 비유할 수 있습니다.
신용카드나 체크카드의 경우 분실했을 때 카드사에서 정지시킨다면 분실된 카드를 악용하려는 행위를 방지할 수 있습니다. 따라서 카드는 분실하였지만 실제로 내가 아닌 타인이 돈을 인출하거나 원치 않은 곳에서 쓰는 등의 손해를 보지 않을 가능성이 높습니다. 세션 기반 인증 방식의 경우에도 세션 ID가 유출되는 등의 문제가 발생했을 때 서버에서 세션을 통제할 수 있어 세션 ID를 통한 공격자의 악의적인 접근을 막을 수 있게 되고 더는 문제가 발생하지 않습니다. <br><br>
마찬가지로 신분증을 분실했을 경우를 생각해봅니다. 신분증은 신용카드 또는 체크카드와는 다르게 분실한 신분증에 대해 취할 방법이 없습니다. 개인 정보는 만료일이 존재하지 않고 언제나 같기 때문에 한 번 노출이 되면 계속해서 악용될 가능성이 높습니다. 이와 유사하게 토큰의 경우에도 제3자에 의해 토큰 내부에 담겨 있는 유저의 정보가 탈취당하는 경우에 클라이언트나 서버 모두 노출된 개인 정보에 대해 손쓸 방법이 없습니다. 따라서 토큰에는 민감한 정보는 담지 않고 유출된다 해도 피해를 최소화 할 정보만 담아 이를 방지하도록 해야합니다. 

# JWT
JWT<small class='additional-text'>(JSON Web Token)</small>는 ```access token```을 만드는 방법 중 하나이며 그렇게 만들어진 토큰을 의미합니다.
유저가 누구인지 식별 할 수 있는 정보를 토큰에 저장해 클라이언트가 가지고 있습니다.
![JWT](img/JWT.png)
JWT의 구조는 다음과 같습니다.
- **header** : 암호화 알고리즘 정보와 토큰의 타입에 대한 정보가 담겨있습니다.
- **payload** : 유저의 인증 정보, 최소한의 필요한 정보만 담겨있어야 합니다. Base64로만 인코딩되기 때문에 탈취당할 경우 쉽게 유저의 데이터를 알아낼 수 있습니다. 따라서 사용자를 판별할 수 있으면서도 고유한 값인 유저의 ID나 토큰의 유효 기간 등의 정보만 넣습니다.
- **signature** : header와 payload를 Base64 인코딩하여 (.) 구분자로 연결합니다. 그리고 지정한 암호화 알고리즘<small>(일반적으로 HS256 또는 RS256)</small>과 secret key를 사용하여 암호화를 합니다. 
이후 토큰을 탈취하여 payload의 내용을 변경하더라도 변경되기 전의 payload 데이터로 signature에 암호화해두었기 때문에 토큰의 위변조를 감지할 수 있습니다. 예를 들어, 제3자가 payload의 유저 id를 '123'에서 '456'으로 바꾸었다고 하더라도 signature의 값은 서버만 알고 있는 secret key로 암호화를 해두었기 때문에 변경할 수 없습니다. 따라서 변조된 access token으로 서버에 요청하면 서버는 Base64로 인코딩되어있는 header와 변조된 payload를 가져와 다시 지정한 알고리즘과 secret key로 해싱하여 signature를 생성합니다. payload가 바뀌었기 때문에 기존 토큰의 signature와 값이 일치하지 않게 되고 유효하지 않다고 판단하여 요청을 거부하게 됩니다. 

[pyJWT](https://pyjwt.readthedocs.io/en/latest/)의 결과 값은 버전에 따라 ```bytes``` 타입<small>(ver. 1.7)</small> 또는 ```str``` 타입<small>(ver. 2.0 이상)</small>입니다.  

```py
access_token = jwt.encode({'email': user.email}, secret_key['SECRET_KEY'], algorithm = ALGORITHM)
```
위에서 발급한 access token은 프론트엔드에게 전달하고 프론트엔드에서는 사용자 정보가 필요한 API를 호출할 때 access token을 함께 보냅니다.

```py
access_token = request.headers.get('Authorization', None)
payload = jwt.decode(access_token, secret_key['SECRET_KEY'], algorithm = ALGORITHM)
```
여기서 payload의 값은 token을 만들 때 넘겨주었던 ```{'email': user.email}```입니다.

## Refresh Token
로그인을 장기간 유지하기 위해서는 토큰의 유효 기간을 길게 늘이거나 설정하지 않을 수도 있습니다. 하지만 이럴 때 토큰이 탈취당하게 된다면 유효 기간 동안 제3자가 인증된 유저의 행위를 할 수 있게 됩니다. 이는 보안에 있어 큰 취약점이 됩니다. 반대로 토큰의 유효 기간을 짧게 설정할 경우 유효 기간이 끝날 때마다 유저는 로그인 해야 하기 때문에 불편함을 느낄 수 있습니다. 이러한 문제점들은 access token과 함께 ```Refresh Token```을 사용하여 보완할 수 있습니다. 
1. 서버는 유저에게 access token과 함께 refresh token을 발급합니다.
2. 클라이언트는 access token, refresh token과 함께 API를 호출합니다.
3. 서버가 만료된 access token을 받았을 경우 클라이언트에게 access token 재발급과 함께 응답을 보냅니다. 
(또는 요청 전에 클라이언트가 payload를 통해 유효 기간이 만료됨을 감지하고 서버에게 access token 재발급을 요청할 수도 있습니다.)
4. 서버는 먼저 access token의 signature 조작 여부를 판단합니다. 그리고 payload의 유저 정보를 통해 데이터베이스에 접근하여 서버가 가지고 있던 유저의 refresh token을 가져옵니다. **서버의 refresh token**과 **클라이언트의 refresh token**을 비교하여 만약 일치하고 유효 기간이 남아있다면 클라이언트에게 새로운 access token을 발급하고 refresh token이 만료되었다면 로그인을 요청합니다.
 
 위 refresh token 발급 과정은 정해진 것이 아니기 때문에 개발자마다 구현 상세는 다를 수 있습니다. 예를 들어, API 요청 시 access token만 보내도록 구현할 수도 있습니다. 그렇게 된다면 refresh token의 유효 기간이 끝났더라도 access token이 유효하다면 그 동안은 인가된 유저의 행위를 지속할 수 있게 됩니다.  

### Refresh Token이 필요한 이유 ✍️
위에서 access token의 유효 기간을 이유로 refresh token의 필요성을 언급했었습니다. 이를 포함하여 refresh token을 사용해야 하는 이유를 크게 두 가지로 나누어 볼 수 있습니다. 
- access token의 유효 기간을 짧게 유지 가능
- 서버에서 각 유저의 세션 유지 기간을 인지하고 통제 가능  

첫 번째로 access token 유효 기간의 길이에 따른 보안적 이유로 인해 refresh token이 사용됩니다. 사용자의 편의를 위해 access token의 유효 기간을 아주 길게 설정한다면 탈취당했을 때 유효 기간 동안 제3자는 자유롭게 토큰을 사용할 수 있습니다. 이를 보완하기 위해 유효 기간을 아주 짧게 설정해볼 수 있습니다. 그러면 탈취한 토큰을 가지고 있는 제3자는 짧은 유효 기간 내에 원하는 공격을 수행해야 하기 때문에 공격에 실패할 확률이 높아져 보안은 강화될 수 있습니다. 그러나 유저는 유효 기간이 끝날 때마다 다시 로그인 해야 하기 때문에 큰 불편함을 느끼게 됩니다. 이러한 이유로 refresh token 사용을 권장하고 있습니다.  
두 번째는 서버의 토큰에 대한 통제 가능 여부입니다. refresh token은 access token과는 다르게 서버에 저장됩니다. access token처럼 클라이언트에 저장되도록 구현할 수 있겠지만 굳이 서버에서 이를 저장하고 관리하는 이유는 유저의 세션에 문제가 발생할 경우 이를 인지하고 통제하기 위함입니다. refresh token을 브라우저에 저장할 경우 서버는 브라우저에 저장되어있는 토큰을 제어할 수 있는 능력이 없어 유저의 토큰이 탈취당하더라도 취할 방법이 없습니다. 그렇기 때문에 refresh token은 서버에서 관리하도록 하여 유저의 토큰이 탈취당했을 때 해당 유저의 refresh token이 만료되도록 해주면 탈취당한 access token을 무효화시켜 공격을 방어할 수 있습니다. 