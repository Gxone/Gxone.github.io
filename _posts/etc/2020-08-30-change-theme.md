---
title: "jekyll 테마 변경 및 검색 도구 추가"
categories: etc
---
처음 깃헙 블로그를 만들고 쭉 써오던 테마를 바꿨다. 이유는 먼저 레이아웃과 줄 간격이 마음에 들지 않았고 한글 폰트 가독성이 좋지 않았다. 또 다른 이유는 프로젝트를 시작하면서 블로그 쓸 시간이 많이 줄었는데 테마가 마음에 들지 않다 보니 블로깅할 마음이 들지 않아 다시 새로운 마음으로 시작하기 위한 것도 있었다. 찾아본 테마로는  ```plain-text``` 와 ```the-plain```가 있다.

+ [plainwhite-jekyll](https://github.com/samarsault/plainwhite-jekyll)
+ [the-plain](https://github.com/heiswayi/the-plain)

심플한 테마를 써보고 싶어서 후자를 택했지만, 나중에 포스트가 많아지기 전에 태그나 카테고리 기능을 추가해야 할지도 모르겠다. 

먼저 검색 기능이 필요한 것 같아 구글링을 하던 중 [tipue-search](https://github.com/jekylltools/jekyll-tipue-search) 라는 것을 알게되었다. 플러그인이 필요하지 않고 제이쿼리를 활용하여 만들었다고 한다. 

## Tique Search 설치
1. 위 github repository 에 접속하여 jekyll-tipue-search-master.zip 를 다운받았다.
2. search.html 을 블로그가 있는 최상위 디렉토리에 복사한다. 
3. ```assets``` 폴더 안에 있는 ```tiquesearch``` 폴더를 내 블로그 디렉토리의 ```assets``` 아래에 복사한다. 

## Tique Search 환경 설정
+ ```_includes/head.html``` 파일에 아래의 코드를 추가힌다. 

```html
<link rel="stylesheet" href="{{ "/assets/tipuesearch/css/normalize.css" | relative_url }}">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="{{ "/assets/tipuesearch/tipuesearch_content.js" | relative_url }}"></script>
<link rel="stylesheet" href="{{ "/assets/tipuesearch/css/tipuesearch.css" | relative_url }}">
<script src="{{ "/assets/tipuesearch/tipuesearch_set.js" | relative_url }}"></script>
<script src="{{ "/assets/tipuesearch/tipuesearch.min.js" | relative_url }}"></script>
```

+ 복사한 ```search.html``` 에 다음의 코드를 추가한다.  

```html
<form action="{{ page.url | relative_url }}">
  <div class="tipue_search_left"><img src="{{ '/assets/tipuesearch/search.png' | relative_url }}" class="tipue_search_icon"></div>
  <div class="tipue_search_right"><input type="text" name="q" id="tipue_search_input" pattern=".{3,}" title="At least 3 characters" required></div>
  <div style="clear: both;"></div>
</form>
<div id="tipue_search_content"></div>
<script>
$(document).ready(function() {
  $('#tipue_search_input').tipuesearch();
});
</script>
```

+ 마지막으로 검색 창을 붙일 파일을 열어 예) ```_includes/footer.html```  
다음의 코드를 원하는 위치에 추가한다. 

```html
<form action="/search">
   <div class="tipue_search_left">
     <img src="/assets/tipuesearch/search.png" class="tipue_search_icon">
   </div>
   <div class="tipue_search_right">
     <input type="text" name="q" id="tipue_search_input" pattern=".{1,}" title="At least 1 characters" required></div>
   <div style="clear: both;"></div>
 </form>
 ```

 이 때 serch.html 에서는 검색 input 에 css 가 적용되지만 main 페이지의 footer 에는 적용되지 않아 다음과 같이 맨 위에 link 태그로 path를 지정해주어 css 파일을 찾아가도록해 주었다.
 ![script](https://user-images.githubusercontent.com/26542094/91661428-f88cb400-eb16-11ea-8dcb-8d16eb4aabaa.png)