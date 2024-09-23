---
layout: post
title: "동기 프로그래밍 / 비동기 프로그래밍"
blog: true
text: true
post-header: false
header-img: ""
category: "TIL"
date: "2024-09-20"
---
비동기 프로그래밍에서 ```await``` 키워드를 통해 비동기 작업이 완료될 때까지 현재 함수 실행이 일시 중지되고 그 사이 다른 비동기 작업들이 실행된다고 하는데 동기 프로그래밍과의 차이가 조금 헷갈려 정리하게 되었습니다 🤓

## 동기 프로그래밍
동기 프로그래밍에서는 한 번에 하나의 작업만 처리됩니다. 코드가 위에서 아래로 순차적으로 실행되며 이전 작업이 완료될 때까지 다음 작업이 대기합니다.

### 예시
```py
import time

def task1():
    print("Task 1 started")
    time.sleep(2)  # 2초 대기
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    time.sleep(1)  # 1초 대기
    print("Task 2 finished")

def main():
    task1()
    task2()

main()
```

### 실행 결과
```
Task 1 started
(2초 대기)
Task 1 finished
Task 2 started
(1초 대기)
Task 2 finished
```

## 비동기 프로그래밍
비동기 프로그래밍에서는 여러 작업을 동시에 처리할 수 있습니다. 특정 작업이 완료될 때까지 기다리는 동안 다른 작업을 수행할 수 있습니다. 이는 CPU를 효율적으로 사용하고 대기 시간 동안 자원을 낭비하지 않게 합니다.

### 예시
```py
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # 2초 대기 (비동기적)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)  # 1초 대기 (비동기적)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

### 실행 결과
```
Task 1 started
Task 2 started
(1초 대기)
Task 2 finished
(1초 대기)
Task 1 finished
```

```await```키워드는 비동기 함수 내부에서 비동기 작업의 완료를 기다리는 동안 현재 함수의 실행을 일시 중지하고 이벤트 루프에 제어권을 반환합니다. 비동기 작업이 끝날 때까지 현재 함수 실행을 일시 중지하지만, 프로그램 전체를 멈춘다는 의미가 아니라 그동안 이벤트 루프는 멈추지 않고 다른 비동기 작업을 처리합니다.

여기서 이벤트 루프란 비동기 함수들을 관리하고 실행 순서를 조정하는 역할을 합니다. 
1. 이벤트 루프는 비동기 함수(task1, task2)를 실행합니다.
2. 비동기 함수 내부에서 ```await``` 키워드를 만나면 함수 실행이 일시 중지됩니다.
3. 이벤트 루프는 대기 중인 다른 비동기 함수(task2)를 실행합니다.
4. ```await```한 작업이 완료되면 함수 실행이 재개되어 ```await``` 다음의 코드가 실행됩니다.

동기 프로그래밍과 달리 task1과 task2는 동시에 시작되고 task1이 대기 하는 동안 task2는 1초 후 완료되고 1초 후 task1도 끝나게 됩니다. 동기 프로그래밍과 달리 여러 작업을 겹처서 실행할 수 있어 I/O 바운드 작업에서 성능을 크게 향상 시킬 수 있습니다.