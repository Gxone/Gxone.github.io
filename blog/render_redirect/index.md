---
layout: post
title: "render / redirect"
blog: true
text: true
post-header: false
header-img: ""
category: "Django"
date: "2022-02-23"
---
## render
```py
render(request, template_name, context=None, content_type=None, status=None, using=None)
```
```render()```는 주어진 템플릿을 ```context```와 결합하여 렌더링 된 ```HttpResponse``` 객체를 반환합니다.
```render()```의 필수 인자 값은 ```request```와 ```template_name```이며 나머지는 옵션입니다.

```py
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('pages/index_page.html')

    context = {
        'title': 'HOME',
        'description': 'hello world!'
    }
    body = template.render(context, request)
    return http.HttpResponse(body, content_type=None)
```
과거 템플릿에 context를 넘겨주기 위해서는 위와 같이 작성해야 했습니다. 하지만 ```render()```를 사용하여 더 간결하게 표현할 수 있습니다.
```py
from django.shortcuts import render

def index(request):
    context = {
        'title': 'HOME',
        'description': 'hello world!'
    }

    return render(request, 'pages/index_page.html', context)
```

## redirect
```py
redirect(to, *args, permanent=False, **kwargs)
```
다른 페이지로 redirect 할 때 사용합니다. render와 redirect의 차이점은 render는 템플릿을 불러오는 것이라면 redirect는 URL로 이동하는 것이기 때문에 URL에 해당하는 view에 GET 요청을 보내게 됩니다. 따라서 form에서 POST 요청을 하고 난 후 결과 페이지를 보여 줄 때 ```render```가 아닌 ```redirect```를 사용해야 사용자가 새로 고침을 하면 한 번 더 POST 요청을 보내는 것을 방지할 수 있습니다.  
```to```에는 URL name, 상대 URL, 절대 URL을 모두 인수로 넘길 수 있습니다. ```redirect()```는 URL로 이동하는 것이기 때문에 context를 넘길 수는 없으며 ```HttpResponseRedirect``` 객체를 반환합니다.
```py
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect(reverse('blog:detail'))
```
위와 같이 URL name을 사용하는 경우에는 ```reverse()``` 함수를 호출해야 했지만, ```redirect()```는 내부적으로 ```reverse()``` 함수를 호출하여 굳이 감싸줄 필요가 없고 더욱 간단히 표현할 수 있습니다. 하지만 GET 파라미터를 사용해야 하는 경우에는 ```reverse()``` 함수를 호출해주어야 합니다.
```py
def my_view(request):
    ...
    return redirect('blog:detail', post_id='1')  # 내부에서 resolve_url()을 호출
    # <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/blog/detail/1/">

    return redirect(reverse('blog:detail') + '?post_id={}'.format(request.POST['post_id'])
```
```py
from django.shortcuts import redirect

def my_view(request):
    ...
    return redirect('/blog/detail/1')
```
```py
def my_view(request):
    ...
    return redirect('https://example.com/blog/detail/1')
```