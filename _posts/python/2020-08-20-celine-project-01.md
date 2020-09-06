---
title: "[1차 프로젝트] CELINE 사이트 크롤링 01"
categories: python project
---
1차 프로젝트로 CELINE 사이트를 클론하게 되었다. 먼저 shoes 카테고리만 구현하기로하여 shoes 데이터만 크롤링하기로 했고 이를 기반으로 모델링을 하였다. 

![Modeling](assets/img/celine-modeling.png)

각각 세 가지의 카테고리로 나뉘며 제품 테이블과 제품의 이미지, 색상 테이블이 있으며 제품과 색상은 n:m 관계이기 때문에 중간 테이블이 필요하다. 

## 메뉴 및 상품 데이터
![Modeling](https://user-images.githubusercontent.com/26542094/91656733-f36b3d00-eaf5-11ea-86c2-29de6e99e11d.png)
위는 셀린느 홈페이지의 nav bar 이다.
 여기서 첫 번째 카테고리가 ```main menu```, 두 번째 카테고리가 ```categories```, 세 번째 카테고리가 ```sub_categories``` 테이블 이다. 
![Modeling](https://user-images.githubusercontent.com/26542094/91656736-f5350080-eaf5-11ea-8e97-cb6df1219ad4.png)
위와 같이 카테고리 별로 제품을 보여주는 페이지가 있어 카테고리 테이블을 통해 제품이 어떤 카테고리에 속해 있는지 알 수 있어야 한다. 
![Modeling](https://user-images.githubusercontent.com/26542094/91656738-f6662d80-eaf5-11ea-9398-0adff4173354.png)
![Modeling](https://user-images.githubusercontent.com/26542094/91656821-dc791a80-eaf6-11ea-90e6-60b24125e5f5.png)
![runway](https://user-images.githubusercontent.com/26542094/91657021-be141e80-eaf8-11ea-92bf-a3b289eac9dc.png)
상품의 정보를 보여주는 상세 페이지에 상품의 이미지와 이름, 설명, 색상과 각 상품이 속하는 카테고리까지 알 수 있어 한 페이지에서 모두 크롤링 할 수 있었다. 
런웨이 룩스의 경우에는 하나의 테이블을 만들어 image-url을 모두 크롤링하였고 프론트 엔드에는 하나의 리스트로 보내주었다. 

### 크롤링
크롤링은 ```selenium``` 을 사용하였다. 

처음 생겼던 문제는 브라우저를 띄웠을 때 쿠키 허용에 관한 알림이 위 쪽에 뜨는 데 이를 허용하지 않으면 알림창에 다른 요소들이 가려져 제대로 크롤링 할 수가 없어 처음에 허용 버튼을 클릭하는 로직을 넣어주어야 했다. 
```py
# 쿠키 허용 하기
cookie_btn = driver.find_element_by_css_selector("#root > div.Sticky.js-cel-Sticky > div > div > div > div.grid__right > div > div > button")
cookie_btn.click()
```

처음 상품의 상세 데이터를 크롤링할 때 카테고리 -> 각 제품 상세 페이지로 매번 클릭해서 들어가도록 구현을 했었다. 그런데 클릭을 통해 크롤링을 할 경우 페이지 로드를 기다리는데 시간이 너무 오래 걸리기도 하고 오류가 자주 발생해 이를 url을 통해 페이지가 바뀌도록 바꾸었다. 

![shoes](https://user-images.githubusercontent.com/26542094/91657366-54e1da80-eafb-11ea-882f-b053c2f453d2.png)

여기서 item 은 위의 BOOTS, SANDALS .. 와 같은 카테고리이며 이를 기반으로 해당 카테고리에 속하는 신발의 url 을 가져온다. 이 후 각 상품(url) 별로 카테고리 정보도 필요하기 때문에 url은 딕셔너리의 키, 카테고리는 value 에 저장했다. (아래 딕셔너리를 사용한 좀 더 자세한 이유가 있다.)
```py
 driver.get("https://www.celine.com/en-int/celine-women/shoes/" + item)
        # 스크롤 높이 가져온다.
        last_height = driver.execute_script("return document.body.scrollHeight")
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        # 페이지 로드 기다리고 태그 모두 가져온다.
        a_tags = driver.find_elements_by_xpath('/html/body/div[1]/main/div[2]/div[3]/div[2]/div/div/div[2]/ul/li/article/a')
```

a_tags url을 하나씩 돌며 상품의 이름과 설명, 색상 등을 크롤링 하여 각각 리스트에 저장했다. 
```py
for prod in prod_dict.keys():
    print(prod)
    driver.get(prod)
    # 이름
    shoes_name = driver.find_element_by_css_selector("div#product-details-main > main > div.grid__right > section > div.o-product__product > form > h1").text
    shoes_name_list.append(shoes_name)
    # print(shoes_name)
    # 설명
    description = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/section/div[2]/form/p[2]").text
    description_list.append(description)
    # print(description)
    # --- 색상 크롤링 ---
    color_click = driver.find_element_by_css_selector("#ddt-productColour")
    color_click.click() # colors 드롭 다운 클릭
    # 컬러
    color_name_list = []
    color_names = driver.find_elements_by_xpath("/html/body/div[1]/main/div[2]/section/div[2]/form/fieldset/ol/li[1]/div/div/fieldset/div/ol/li/div/a")
    for item in color_names:
        color_name_list.append(item.text)
```
 
![shoes](https://user-images.githubusercontent.com/26542094/91657584-14835c00-eafd-11ea-8d33-bf491ead0e59.png)
![shoes](https://user-images.githubusercontent.com/26542094/91657586-164d1f80-eafd-11ea-8f28-63cae7433929.png)

크롤링을 하며 고민했던 부분은 위와 같이 각각 상품이 속한 카테고리 들을 크롤링하는데 new 상품인 경우에는 4번째에 카테고리 명이 있지 않고 new 가 위치해 있는다. 따라서 4번째에 new 가 있을 경우에는 딕셔너리의 value를 가져와 카테고리에 대신 넣어주도록 하였다. 더 좋은 방법이 있을 지도 모르지만 이 땐 이 방법밖에 생각나지 않았다 😭
```py
 # 첫 번째 카테고리
    first_category = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/section/nav/ul/li[2]/a").text
    # 두 번째 카테고리
    second_category = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/section/nav/ul/li[3]/a").text
    try:
        # 세 번째 카테고리
        third_category = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/section/nav/ul/li[4]/a").text
        # 네 번째 카테고리
        forth_category = prod_dict[prod]
    except:
        pass
```

## 아쉬웠던 점
배포를 기준으로 깃헙에 코드를 올리기 때문에 데이터와 관련된 파일을 깃헙에 따로 올리지 않아 크롤링에 관련된 코드는 피드백을 받을 수 없었다. 지금 내가 봐도 코드가 정말 엉망인데 리스트 컴프리헨션에 익숙하지 않아 사용하지도 않았고 시간에 쫓겨 효율은 생각하지도 않고 짰다. 사이트도 복잡한데 느리기도 해서 크롤링하는데 정말 애 먹었던 기억이 있는데 이 경험을 토대로 다음에는 좀 더 빠르고 가독성 좋게 코딩을 하고 싶다 😂