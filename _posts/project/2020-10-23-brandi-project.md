---
title: "Brandi Internship Review"
categories: project
tags: internship
---

# Brandi
![](https://user-images.githubusercontent.com/26542094/97079044-cb96e200-162b-11eb-80e9-87bf0d6072e7.png)
브랜디는 2014년에 설립하여 '남들이 못하는 것을 하자.' 는 철학을 가지고 지금까지 세상에 없던 '최고의 쇼핑 경험'을 만들고 있는 패션 테크 기업입니다.

여성 고객을 타겟으로 한 <b>'브랜디'</b>와 남성 고객을 타겟으로 한 <b>'하이버'</b>, 판매자들의 운영상 어려움까지 해결해주는 <b>'헬피'</b> 를 만들어 운영 중에 있습니다. 

<br>

## 프로젝트 목표
<b>기간</b>: 2020.09.14 - 2020.10.15 <i>(5weeks)</i>   
<b>목표</b>: 프론트엔드 5명, 백엔드 5명이 한 팀이 되어 일반 유저가 사용하는 <b>서비스</b>, 판매자가 사용하는 <b>백오피스</b>를 개발하는 것이 주어진 과제였습니다!  

<br>

## 팀 구성 
<b>Service</b>: 프론트엔드 3명 / 백엔드 2명  
<b>B/O</b>: 프론트엔드 2명 / 백엔드 3명  
(백오피스 팀원의 중간 이탈로 서비스와 백오피스 파트 모두 백엔드로 참여했습니다.)

<br>

## 사용 기술
Python, Flask / Mysql / AWS EC2, RDS / Git

<br>

## 깃헙
- <a href='https://github.com/Wecode11-Brandi-Team2/Service-backend'> Service-backend </a>  
- <a href='https://github.com/Wecode11-Brandi-Team2/BO-backend'> B/O-backend </a>

<br>

## 모델링
- <a href='https://aquerytool.com:443/aquerymain/index/?rurl=684cffa4-5742-4925-abbd-1fb90558f5e1'> Modeling </a> (비밀번호: 8fk52g)

<br>

## 담당 구현 기능
처음 팀 회의를 하며 <b>서비스 파트의 product 관련 API 와 QnA API</b> 를 맡기로 하였습니다. 이후에는 백엔트 팀원 한 명이 그만두게되어 <b>백오피스 파트의 product API</b> 도 맡아 구현하였습니다.

<b>Service API</b>:  
-product 리스트 전달  
-product 상세 데이터 전달  
-카테고리 리스트 전달  
-seller 리스트 전달  
-QnA 리스트 전달  

<b>B/O API</b>:  
-product 리스트 전달  
-product 상세 데이터 전달  
-product 등록   
-product 수정  
-product 정보 엑셀 다운로드  
-product 수정 이력 전달  
-seller 리스트 전달  
-1, 2차 카테고리 전달  

<br>

## 코드 리뷰
5 주간 매주 이틀에 한 번 씩 코드 리뷰 시간이 있었습니다.  
각자 이전 코드 리뷰에서 받은 피드백을 반영한 내용과 새로 구현한 내용에 대해 발표를 하고 이에 대한 피드백을 받을 수 있었습니다. 자기가 구현한 부분에 대해 완벽히 이해하고 그걸 설명해야한다는 것이 부담이 되기도 했지만, 현업에서는 어떤 방식으로 작업을 하는 지, 작업하며 어떤 것에 초점을 두고 구현하는 지 알 수 있어 정말 좋은 기회였고 그 동안 프로젝트를 하며 생각치 못한 트래픽과 보안과 관련된 부분까지 생각하고 작업한다는 사실도 알 수 있었습니다 🙂!

<br>

### 기억에 남는 코드 
<b>[이미지 파일 업로드]</b>  

```py
image_urls = list()

# s3 서버 연결 및 이미지 업로드
s3_resource = get_s3_resource()

for image in images:
    # 허용된 jpg, jpeg 확장자인지 확인한다.
    message = allowed_file(image.filename)

    # jpg, jpeg 확장자가 아닐 경우 에러 메세지가 반환된다.
    if message:
        return message

    # s3 서버에 이미지 업로드
    s3_resource.put_object(Body = image, Bucket = 'brandi-images', Key = f'{product_code}_{image.filename}', ContentType = 'image/jpeg')

    # 데이터베이스에 저장할 이미지 url 을 리스트에 추가한다.
    image_url = f'https://brandi-images.s3.ap-northeast-2.amazonaws.com/{product_code}_{image.filename}'
    image_urls.append(image_url)

return image_urls
```
셀러가 상품을 등록할 때 이미지를 업로드 하는 기능이 있었습니다. 로컬이 아닌 이미지 url을 얻기 위해 AWS S3에 이미지를 업로드 하여 상품 코드 + 이미지 파일 이름의 조합으로 이미지 url을 생성하도록 하였습니다!
```py
# allowed_file(image.filename)
# 이미지 파일 업로드 가능한 확장자
ALLOWED_EXTENSIONS = ('jpg', 'jpeg')

def allowed_file(filename):
    if '.' in filename and filename.rsplit('.', 1)[1] not in ALLOWED_EXTENSIONS:
        return jsonify({'message': 'INVALID_EXTENSION'}), 400
```
업로드 시 ```jpg``` 확장자만 업로드를 할 수 있는 제한 사항이 있었는데 이를 위해 허용된 확장자가 아닐 경우 에러를 반환하도록 해주었습니다!  
위의 코드를 추가해 준 결과 아래와 같이 S3 버킷에는 ```jpg``` 확장자만 업로드 된 것을 확인 할 수 있었습니다 😎!  

![](https://user-images.githubusercontent.com/26542094/97068417-5c58c800-1602-11eb-9aed-f86679ef02f3.png)  

--- 

<b>[S3 서버의 이미지 삭제]</b>  

```py
# product_controller.py
#...(생략)
    return jsonify({'message': 'SUCCESS'}), 200

except KeyError:
    return jsonify({'message': 'KEY_ERROR'}), 400

except exc.IntegrityError:
    return jsonify({'message': 'INTEGRITY_ERROR'}), 400

except exc.InvalidRequestError:
    return jsonify({'message': 'INVALID_REQUEST'}), 400

except exc.ProgrammingError:
    return jsonify({'message': 'ERROR_IN_SQL_SYNTAX'}), 500

except Exception as e:
    return jsonify({'message': f'{e}'}), 500

finally:
    if is_success is False:
        session.rollback()
        delete_image_in_s3(image_urls, None)
    session.close()
```
위 코드와 같이 에러가 발생할 경우 에러 메세지를 반환하도록 하고 세션을 롤백 시키도록 해주었습니다. 이때 데이터베이스에 에러가 발생한 상품 데이터는 저장되지 않지만 서버에 업로드된 이미지에 대한 처리는 없어 S3에는 에러가 발생한 상품에 대한 이미지가 그대로 남아있는 상태인 것을 발견하게 되었습니다. 따라서 <b>에러 발생 시 세션 롤백과 함께 S3 서버의 이미지를 삭제하는 로직</b>을 구현해주었습니다.
```py
# 에러 발생 시 S3 서버에 업로드된 이미지를 삭제하는 메소드
def delete_image_in_s3(images, new_images):
    s3_resource = get_s3_resource()

    if new_images:
        for new_image in new_images:
            if new_image not in images:
                # 이미지 url 에서 파일 이름을 가져온다.
                file_name = re.findall('https:\/\/brandi-images\.s3\.ap-northeast-2\.amazonaws\.com\/(.*)', new_image)
                s3_resource.delete_object(Bucket='brandi-images', Key=f'{file_name[0]}')
    else:
        for image in images:
            # 이미지 url 에서 파일 이름을 가져온다.
            file_name = re.findall('https:\/\/brandi-images\.s3\.ap-northeast-2\.amazonaws\.com\/(.*)', image)
            s3_resource.delete_object(Bucket='brandi-images', Key=f'{file_name[0]}')
```
상품 등록 시에는 등록하려는 모든 이미지 url 에 대해 버킷에서 삭제해주면 됐지만 상품 수정 시에는 기존 이미지는 그대로 유지하고 추가하려는 이미지만 삭제하도록 해야했습니다.  
그래서 수정 시에는 ```new_images``` 리스트를 인자로 넘겨주어 상품 등록 시 삭제하는 경우와 구분해주었고 기존 이미지는 삭제하지 않고 새로 업로드하려는 이미지만 삭제하도록 구현해주었습니다.

<br>

## 느낀 점
5주간 거의 이틀에 한 번 있는 코드리뷰와 마지막 주에는 발표 리허설과 최종 발표까지 코딩 외에도 준비해야할 게 정말 많았고 한달 간 정말 바쁘게 보낸 것 같습니다. 

먼저 <b>아쉬운 점</b>은 이것저것 모두 물어보는 성격이 아니라 혼자 머릿속으로 생각하고 이해하는 것을 선호해 현직자에게 많은 것들을 물어보지 못했다는게 돌아보고나니 너무 아쉬웠습니다. 다음에는 눈치보지말고 이것저것 물어봐야겠다는 생각이 들었어요 🤓. 그리고 몇몇 API 는 UI가 나오지 않아 포스트맨으로만 시연할 수 있었다는 것도 아쉬웠습니다. 아무래도 프론트엔드와 맞춰보다보면 내가 신경쓰지못하고 지나친 부분에서 에러가 뜰 경우도 있어 이런 것들을 해결하면서 배우는 것도 많았기 때문에 이런 점에선 아쉽기도 했어요.

<b>잘한 점</b>은 새로운 프레임워크를 사용하며 초반에는 공부하는 시간이 많아 속도가 느릴까봐 걱정했었지만 sql 문에 익숙해지면서 속도가 빨라져 목표로 잡은 추가 구현 사항뿐만아니라 빈 자리가 생기며 API 가 나오지 못할 뻔한 백오피스의 상품 관련 API까지 끝낼 수 있었다는게 뿌듯하고 잘한 점이라고 생각합니다. 

또한 10명이 한 팀으로 작업하며 처음에는 구현해야하는 기능도 많고 서비스와 백오피스가 테이블을 공유하기 때문에 모델링을하며 일주일을 보냈는데 결국에는 추가 구현사항까지 모두 완성했고, 팀원들 모두 뒤처지지 않고 열정적으로 해줘서 너무 멋있고 고마웠습니다. 매주 회의하며 아쉬웠던 발표에 대해 뒤돌아보며 부족한 것들을 정비하는 시간도 가지고 각자 해줘야하는 역할들을 너무 잘해준 것 같아요!  

매 주 있던 코드 리뷰에서는 초반에 내가 작성한 코드를 말로 설명하고 발표하는 것이 익숙하지 않아 끝나고 나면 팀원들에게 혹시 부족한 점이 있었나 물어보고 다음 리뷰때 반영했습니다. 그리고 2주차, 3주차가 되어서는 프론트엔드 팀원분께 가장 듣기 쉽게 설명해서 집중하게 된다는 칭찬도 들을 수 있었고 마지막 발표에서도 팀원들에게 잘했다는 칭찬을 받아서 기분이 좋았어요 🥳.
