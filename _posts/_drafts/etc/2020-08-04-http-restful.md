---
title: HTTP & RESTful HTTP API
categories: etc
---
## HTTP란?
+ HyperText Transfer Protocol
+ HTML 문서를 교환하기 위해 만들어진 통신 규약.
+ 웹 상에서 네트워크로 서버끼리 통신을 할 때 어떤 형식으로 서로 통신을 하자고 규정해 놓은 <b style="color:#fff; background:#52BBD0">통신 형식</b>이라고 보면 된다. 
+ HTTP 는 TCP/IP 기반으로 되어있다. 

### HTTP 핵심 요소
#### [HTTP 통신 방식]
+ HTTP는 기본적으로 requset / response 구조로 되어있다.
+ HTTP는 Stateless 이다. 
    - 요청이 오면 그 요청에 응답할 뿐 여러 요청과 응답끼리는 연결되어 있지 않다. 
    - 그렇기 때문에 여러 요청과 응답의 진행 과정이나 데이터가 필요할 때는 쿠키나 세션등을 사용하게 된다. 

#### [HTTP Request 구조]
+ start line
+ headers
+ body

<b>[Start Line]</b>
+ HTTP Method
    - 해당 requset가 의도한 action을 정의하는 부분.
    - HTTP Methods 에는 GET, POST, PUT, DELETE, OPTIONS 등이 있다. 
+ Requset target
    - 해당 requset가 전송되는 목표 uri.
    - 예를 들어 /login.
+ HTTP Version
    - 1.0, 1.1, 2.0과 같이 사용되는 HTTP 버전. 

```
GET /search HTTP/1.1
```

<b>[Headers]</b>
+ 해당 requset 에 대한 추가 정보를 담고 있는 부분.
+ Key:Value 값으로 되어있다.
+ Headers 도 크게 세 부분으로 나뉘어 있다. 
+ 자주 사용되는 header 정보는 다음과 같다. 
    - Host
        - 요청이 전송되는 target의 host url
    - User-Agent
        - 요청을 보내는 클라인언트에 대한 정보
    - Accept
        - 해당 요청이 받을 수 있는 response 타입
    - Connection
        - 해당 요청이 끝난 후에 클라이언트와 서버가 계속해서 네트워크 커넥션을 유지할 것인지 끊을 것인지에 대해 지시하는 부분
    - Content-Type
        - 해당 요청이 보내는 메세지 body의 타입. 예를 들어, JSON 을 보내면 ```application/json```
    - Content-Length
        - 메세지 body의 길이

```
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/json
Content-Length: 257
Host: google.com
User-Agent: HTTPie/0.9.3
```

<b>[Body]</b>
+ 해당 requset 의 실제 메세지 / 내용.
+ GET requset 들은 대부분 body가 없는 경우가 많다. 

```
POST /payment-sync HTTP/1.1

Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 83
Content-Type: application/json
Host: intropython.com
User-Agent: HTTPie/0.9.3

{
    "imp_uid": "imp_1234567890",
    "merchant_uid": "order_id_8237352",
    "status": "paid"
}
```

#### HTTP Response 구조
Response 도 requset와 마찬가지로 크게 세 부분으로 구성되어 있다.
+ Statuse line
+ Headers
+ Body

<b>[Statuse Line]</b>
+ Response 의 상태를 간략하게 나타내주는 부분.
+ 세 부분으로 구성되어 있다. 
    - HTTP 버전
    - Status code : 응답 상태를 나타내는 코드. 예를 들어 ```200```
    - Status text : 응답 상태를 간략하게 설명해주는 부분. 예를 들어 ```Not Found```

```
HTTP/1.1 404 Not Found
```

<b>[Headers]</b>
+ Response 의 headers 와 동일하다. 
+ 다만 response 에서만 사용되는 header 값들이 있다. 예) ```User-Agent``` 대신에 ```Server``` 헤더가 사용된다. 

<b>[Body]</b>
+ Response 의 body와 일반적으로 동일하다. 
+ Requset 와 마찬가지고 모든 response 가 body 가 있지는 않다. 데이터를 전송할 필요가 없을 경우 body가 비어있게 된다. 

```
HTTP/1.1 404 Not Found

Connection: close
Content-Length: 1573
Content-Type: text/html; charset=UTF-8
Date: Mon, 20 Aug 2018 07:59:05 GMT

<!DOCTYPE html>
<html lang=en>
  <meta charset=utf-8>
  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
  <title>Error 404 (Not Found)!!1</title>
  <style>
    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}
```

---

## RESTful API
[REpresentational State Transfer]
웹상에서 사용되는 여러 리소스를 HTTP URL로 표현하고 그 리소스에 대한 행위를 HTTP Method 로 정의하는 방식.
즉, HTTP URI 로 정의된 리소스를 어떻게 한다를 HTTP Method+Payload 로 구조적으로 표현하는 것.

예를 들어 삼성전자 주식 정보를 받기 위한 HTTP 요청:
```HTTP GET https://api.trueshort.com/stock/005930```

유저의 보유 주식 종목들을 DB 에 저장하는 HTTP 요청:
```
HTTP POST https://api.trueshort.com/user/portfolio

{
    "user_id" : 1,
    "stocks": [ 
        "005930",
        "298730",
        "378900"
    ]
}
```

### RESTful API 의 장점
+ self-descriptiveness
+ RESTful API는 그 자체만으로도 API의 목적이 쉽게 이해가 된다.

### RESTful API 를 개발할 때 유의할 점
+ ```/``` 는 계층 관계를 나타낼 때 사용한다. 
+ URL 에 ```_``` 는 주로 포함하지 않고 영어 대문자보다 소문자를 쓴다. 또한 가독성을 위해 너무 긴 단어는 사용하지 않는다. 
+ 동사는 HTTP Method를 통해 표현하기 때문에 URL에는 명사를 사용한다. 
