---
layout: post
title: "Django JWT 관련 라이브러리"
blog: true
text: true
post-header: false
header-img: ""
category: "Django"
date: "2024-09-04"
---

토이 프로젝트를 하면서 인증과 관련하려 JWT를 사용하여 구현을 하려는데 편하게 구현할 수 있는 라이브러리가 몇 가지 있어 찾아보던 중 정리를 해보고 싶어 포스팅 합니다.

## Simple JWT (djangorestframework-simplejwt)
JWT를 사용한 토큰 기반 인증을 쉽게 구현할 수 있으며, 액세스 토큰과 리프레시 토큰을 기본적으로 지원합니다. 로그아웃한 리프레시 토큰을 무효화 할 수 있으며 커스텀 클레임을 추가하고 토큰 만료 시간 설정이 가능합니다. 유지/관리가 잘 되고 있고 확장과 커스터마이징에 용이하지만 기본적인 기능만 제공되어 복잡한 요구사항이 있을 경우 추가 구현이 필요합니다.

```py
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

## Django REST Framework JWT (djangorestframework-jwt)
JWT 기반 인증을 제공하는 초기 라이브러리 중 하나입니다. 기본적인 JWT 발급과 인증 기능을 제공하지만, 최근에는 유지/관리되고 있지 않다고 합니다. 따라서 보안 패치나 새로운 기능 추가가 이루어지지 않고 있기 때문에 새롭게 프로젝트를 시작한다면 다른 라이브러리를 선택하는 것이 좋을 것 같습니다.

```py
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
```

## django-allauth + dj-rest-auth
django-allauth는 Django의 인증 및 소셜 로그인 기능을 제공하는 강력한 라이브러리입니다. 이를 JWT 기반 인증과 통합하기 위해 dj-rest-auth를 함께 사용합니다. dj-rest-auth는 django-allauth에 의존하는 패키지이며 DRF를 위한 API 엔드포인트를 제공해줍니다. 또한 JWT와 소셜 로그인을 지원하는 등 복잡한 인증 시나리오를 다루기 좋은 라이브러리입니다.

이메일 인증과 소셜 로그인, 더해서 비밀번호 초기화, 이메일 인증 등의 기본 인증 기능 외에도 많은 기능을 제공합니다. 따라서 복잡한 인증 과정이 필요한 프로젝트에 적합하고 설정도 다른 라이브러리와 비교했을 때 복잡합니다.

```py
# settings.py

INSTALLED_APPS = [
    'dj_rest_auth',
    'allauth',
    'allauth.account',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}
```

## PyJWT
PyJWT는 JWT 자체를 생성하고 검증하는 데 사용하는 기본 라이브러리로 Django 전용은 아니지만 JWT를 위한 기능을 제공합니다. Django 프로젝트에서 이 라이브러리를 사용해 직접 JWT를 생성하고 검증할 수 있습니다. 가볍고 간단하지만 Django나 DRF와 직접적으로 통합되지 않기 때문에 많은 기능을 직접 구현해야 하는 단점이 있습니다. 따라서 Django나 DRF에 직접 통합하지 않고, JWT 생성과 검증을 직접 구현하고 싶은 경우. 가벼운 프로젝트나 커스터마이징이 많은 프로젝트에 적합할 것 같습니다.

```py
import jwt

token = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
decoded = jwt.decode(token, "secret", algorithms=["HS256"])
```