---
layout: post
title: "[DRF] APIView / GenericAPIView / Mixin / ViewSet"
blog: true
text: true
post-header: false
header-img: ""
category: "TIL"
date: "2024-09-01"
---
🚀 DRF에서는 CBV를 사용한 예제가 많아 새로운 방식도 배워보고자 CBV를 공부해보려고 합니다. 비슷하면서도 차이점이 명확해보여 잊기 전에 정리해보면서 공부한 내용입니다!

[공식 문서](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)

## APIView
이 클래스는 Django의 일반적인 View를 확장하여 API 요청을 처리하도록 돕습니다. `get()`, `post()`, `put()`, `delete()` 같은 HTTP 메서드를 명시적으로 정의하여 사용자가 직접 핸들러를 구현할 수 있습니다.
```
- 가장 기본적인 뷰 클래스.
- HTTP 메서드를 직접 정의해야 함.
- serializer, queryset 등을 수동으로 처리해야 함.
```

```py
class MyAPIView(APIView):
    def get(self, request):
        # GET 요청 처리
    def post(self, request):
        # POST 요청 처리
```

## GenericAPIView
GenericAPIView는 APIView를 확장한 클래스입니다. APIView보다 좀 더 기능을 제공하며 직접적으로 CRUD 기능을 처리하지는 않지만, `queryset`과 `serializer_class`, `lookup_field` 같은 **속성**을 기본으로 설정하여 공통 동작을 구현합니다. 이를 통해 데이터를 좀 더 쉽게 처리할 수 있습니다.
```
- queryset, serializer_class 등의 속성을 기본으로 제공.
- get_object(), get_queryset(), get_serializer() 등의 유틸리티 메서드를 제공하여 객체 조회와 직렬화 작업을 쉽게 할 수 있음.
- 더 구체적인 뷰를 만들 수 있는 기반을 제공.
```

```py
class MyGenericAPIView(GenericAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get(self, request, *args, **kwargs):
        # GET 요청 처리
```

## Mixin
- CreateModelMixin: 객체 생성 처리
- RetrieveModelMixin: 객체 조회 처리
- UpdateModelMixin: 객체 수정 처리
- DestroyModelMixin: 객체 삭제 처리
- ListModelMixin: 객체 리스트 조회 처리

mixin은 GenericAPIView와 함께 사용하며 더 구체적인 동작을 구현할 수 있습니다. mixin는 list, create, retrieve, update, delete 같은 **기능**을 따로 제공해주며 이를 조합하여 필요에 맞는 뷰를 만들 수 있습니다.

```py
class PostListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
    
	def get(self, request, *args, **kwargs):
		return self.list(request)
        
	def post(self, request, *args, **kwargs):
		return self.create(request)
    
class PostDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
    
	def get(self, request, *args, **kwargs):
		return self.retrieve(request)
        
	def put(self, request, *args, **kwargs):
		return self.update(request)
        
	def delete(self, request, *args, **kwargs):
		return self.delete(request)  
```

## concrete generic view
- ListAPIView: 데이터 리스트를 조회할 때 사용
- RetrieveAPIView: 특정 객체를 조회할 때 사용
- CreateAPIView: 데이터를 생성할 때 사용
- UpdateAPIView: 데이터를 수정할 때 사용
- DestroyAPIView: 데이터를 삭제할 때 사용
- ListCreateAPIView: 데이터 리스트 조회 및 데이터를 생성할 때 사용
- RetrieveUpdateAPIView: 특정 객체를 조회하고 수정할 때 사용
- RetrieveDestroyAPIView: 특정 객체를 조회하고 삭제할 때 사용
- RetrieveUpdateDestroyAPIView: 특정 객체를 조회, 수정, 삭제할 때 사용

DRF에서 제공하는 기본적인 제네릭 뷰(generic view)를 좀 더 구체화한(view with specific behavior) 클래스입니다. DRF는 여러 가지 CRUD 작업을 쉽게 수행할 수 있도록 미리 정의된 구체적인 제네릭 뷰들을 제공합니다.

```py
class PostListGenericAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

## ViewSet
ViewSet은 기본적으로 여러 HTTP 메서드(GET, POST, PUT, DELETE 등)에 대한 핸들러를 하나의 클래스에서 처리할 수 있도록 설계된 클래스입니다. ViewSet을 사용하면 더 간결하고 구조화된 코드로 CRUD API를 구현할 수 있습니다.

### ViewSet
ViewSet은 일반적인 APIView와 비슷하지만, 여러 동작을 하나의 클래스에서 처리하도록 설계되었습니다. 일반적인 APIView가 각 메서드(`get()`, `post()` 등)를 오버라이드하는 방식이라면 ViewSet은 그 동작에 맞는 특별한 메서드들(`list()`, `retrieve()`, `create()` 등)을 제공합니다.

#### 주요 메서드
- list(): GET 요청으로 모든 객체를 반환
- retrieve(): 특정 객체를 반환 (상세 조회)
- create(): 새로운 객체를 생성
- update(): 객체를 업데이트
- destroy(): 객체를 삭제

```py
class MyViewSet(viewsets.ViewSet):
    def list(self, request):
        # 리스트 조회 로직
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        # 특정 객체 조회 로직
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
```

### GenericViewSet
Generic ViewSet은 DRF에서 ViewSet과 GenericAPIView의 기능을 결합한 클래스로 기본적으로 ViewSet의 구조를 따르면서도 제네릭 뷰의 유연성을 제공합니다. GenericAPIView의 모든 기능을 상속받으면서 ViewSet의 라우팅 및 처리 기능을 결합한 구조라고 볼 수 있습니다. Generic ViewSet 자체는 CRUD 작업을 직접 제공하지 않기 때문에 필요한 mixin을 결합하여 구현할 수 있습니다.

```py
class MyModelViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

### ModelViewSet
ModelViewSet은 ViewSet의 확장으로 `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()`, `list()` 메서드가 자동으로 구현됩니다. 기본적으로 모델과 연결되어 있으며 `queryset`과 `serializer_class`를 지정하면 자동으로 모든 CRUD 동작이 구현됩니다.
```py
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```
### ReadOnlyModelViewSet
ModelViewSet의 읽기 전용 버전입니다. `list()`와 `retrieve()` 메서드만 제공하며 CRUD 작업은 하지 않습니다.

```py
class MyReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```