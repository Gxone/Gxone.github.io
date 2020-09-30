---
title: "[1차 프로젝트] CELINE 사이트 클론 02"
categories: python
---
<b style="background: black; color:white">프로젝트 소개</b>  
<b>Celine 사이트 클론</b>  
개발 기간 : 20.08.18 ~ 20.08.28   
개발 인원 : Front-end 4명, Back-end 2명  


<iframe width="560" height="315" src="https://www.youtube.com/embed/dm8tco0wIk0" frameborder="0" allowfullscreen></iframe>

<b style="background: black; color:white">사용된 기술</b>
+ Python, Django
+ Selenium
+ Bcrypt
+ JWT
+ mySql
+ CORS headers

<b style="background: black; color:white">프로젝트 역할 분담</b>: <b style="background:#B7E46E; color:#fff">공통</b>, <b style="background:#5B9AD1; color:#fff">내가 맡은 부분</b>   
<b style="color:#B7E46E">모델링 및 ERD 작성</b>   
<b style="color:#5B9AD1">프로젝트 초기 세팅</b>  
<b style="color:#5B9AD1">상품 정보 크롤링 및 데이터베이스 저장</b>  

<b style="color:#5B9AD1">Product App  
    - products 뷰    
    - product 뷰  
    - category 뷰  
    - runway 뷰</b>  

User App  
    - 회원가입 뷰  
    - 로그인 뷰  
    - 위시리스트 뷰 (CRUD)

<b style="background: black; color:white">잘한 점, 아쉬운 점</b>  
처음 역할 분담을 할 때 Product 앱을 맡았는데 상품 데이터를 보내주는 get 메소드만 구현하다보니 CRUD 를 구현해 볼 수 없었던 것이 아쉬웠다.  

그리고 이렇게 이미 구현된 사이트를 모델링을 해본 건 처음이 었는데 모델링은 빨리 끝내자라는 생각으로 사이트를 대충 휙 훑어보기만 했다 😭 각 상품의 color 옵션을 보긴 했지만 클릭하면 옵션이 선택만 될 것이라 생각했는데 알고보니 해당 색의 상품 url로 이동하는 것 이어서 url 필드가 또 필요했고 공식 홈페이지에는 위시리스트만 존재하고 장바구니나 결제 기능은 따로 없었는데 Location을 international에서 다른 나라로 바꾸면 장바구니와 가격 , 사이즈 정보가 나타났다 😭 이런 비슷한 일이 많아 계속해서 모델을 계속 수정하고 다시 크롤링을하고 뷰를 수정하는 일이 잦았다. 여기서 멘탈이 터지면서 모델링의 중요성을 깨닫게 되었다 .. 

위와 같은 문제로 시간이 많이 부족했는데 여기서 로직의 효율을 생각하지 않고 그냥 내 생각나는대로 무작정 코딩했다.. 리스트 컴프리헨션이나 prefetch 등을 제대로 사용도 못한 것 같은데 다음 프로젝트에서는 어떻게 하면 더 속도가 빠르고 효율이 좋을 지 생각하면서 코딩하고 싶다!

다음으로는 git 을 활용하지 못한 것 같다. 내가 잘못하면 프로젝트 전체가 잘못될까봐 정말 commit, push 만 한 것 같은데 잘못해서 충돌도 내보고 고쳐가면서 배우는 것도 많을 것 같다는 생각이 들었다.  

프로젝트를 하면서 시간이 너무 부족했고 내가 세운 계획에서 틀어질 때 마다 스트레스를 받아서 기분이 너무 안좋았는데 나도 모르게 겉으로 티가 났나보다 😭 예전 인턴할 때도 스트레스 받는 일이 많아서 매일 기분 안좋냐는 소리를 들었는데 이번 프로젝트 할 때도 이런 말을 몇 번 들었다. 고치고 싶은데 쉽지 않은 것 같다 😩 기분이 행동이 되면 안된다고 매번 생각하는데 다음 프로젝트때는 여유도 좀 가지면서 이런 행동은 꼭 고칠 것이다.  

아쉬웠던 점은 참 많은 데 잘한 일은 좀처럼 생각나지 않는다 😅 한 가지 있다면 지금까지 팀프로젝트를 하면서 나는 항상 누군가를 의지하기만 했었다. 이렇게 내가 낸 아이디어가 선정되고 PM이 되어서 팀원들과 같이 회의하고 내가 맡아서 발표하고 그만큼 바쁘기도 했지만 뿌듯한 경험인 것 같다. 이번 기회를 계기로 앞으론 누군가를 의지하기 보다 의지할 수 있을 만큼 실력도 갖추고 같이 일하고 싶은 사람이 되고 싶다.

<b style="background: black; color:white">해결 / 개선 방법</b>  
다음 프로젝트에서는 프론트엔드 팀원들과 사이트를 찬찬히 보면서 같이 모델링을 하려고 한다. 아무래도 프론트엔드에서는 직접 구현할 부분이라 내가 놓친 부분까지 더욱 자세히 훑어 볼 것 같고 모델링을 잘못해서 시간, 노력을 낭비하는 것 보다 처음부터 모델링에 시간을 더 많이 투자해도 괜찮을 것 같다는 생각이 들었다. 

<b style="background: black; color:white">기록하고 싶은 코드 / 힘수 / 로직</b>  

```py
#product/views.py
class ProductView(View):
    def get(self, request):
        global image
        q = request.GET.get('q', '')
        if Product.objects.filter(id = q):
            product = Product.objects.prefetch_related('product_color', 'image_set').get(id = q)
            color_names = [i['name'] for i in product.product_color.values()]
            color_images = [i['color_image'] for i in product.product_color.values()]
            urls = [img['image_url'] for img in product.image_set.values()]
            body = {
                "id"           : product.id,
                "name"         : product.name.name,
                "img"          : urls,
                "description"  : product.description,
                "price"        : product.price,
                "color_names"  : color_names,
                "color_imgs"   : color_images,
                "urls"         : product.product_url
            }
        return JsonResponse(body, status=200)
```

```py
#product/views.py
class ProductsView(View):
    def get(self, request):
        q = request.GET.get('q', '')
        if q:
            body = {
                "products" : []
            }
            product_names = ProductName.objects.filter(name__icontains = q)
            rst_id = [name.id for name in product_names]
            for i in rst_id:
                rst_products = Product.objects.filter(name = i)
                for j in rst_products:
                    list = {
                        "id"    : j.id,
                        "name"  : j.name.name,
                        "img"   : [img.image_url for img in Image.objects.filter(product = j)],
                        "url"   : j.product_url,
                        "price" : j.price
                    }
                    body["products"].append(list)
            return JsonResponse(body, status = 200)
```

<b>200930</b>  
이 위까지는 프로젝트 끝나고 바로 작성했었는데 시간이 없어서 기억하고 싶은 코드 부분만 넣어놓고 블로그 커밋도 못하고 코드에 대한 설명은 나중에 하려고 잠시 미뤄놨었는데 한 달이나 지나버렸다. 이때도 자랑하고 싶어서 기억하고 싶은 코드에 넣었던 게 아니라 좀 더 개선하고 싶은 부분이어서 넣었던 걸로 기억한다. 리스트 컴프리헨션도 손에 익지않아서 잘 쓰지도 않았었고 효율은 생각해보지도 않았었는데 이렇게 기록해놓으니 지금도 물론 잘하는 건 아니지만 한 달보다는 정말 발전했다는 걸 느꼈다 ㅎㅎ 다른 사람이랑 비교하지 않고 어제의 나보다 발전했는지 항상 생각해보려고 했었다. 하지만 쉽지 않았고 달라진게 없는 것 같아서 스스로에게 실망했었던 적이 많았다. 하지만 이렇게 시간이 꽤 흐르고 나니 발전하긴 했나보다. 이제 위코드도 한 달도 남지 않았는데 남은 시간도 하루하루가 후회되지 않도록 열심히 공부해야겠다 !!!