---
layout: post
title: "Message System"
blog: true
text: true
post-header: false
header-img: ""
category: "TIL"
date: "2024-09-05"
---
메시지 분산 처리 시스템은 여러 개의 프로세스나 애플리케이션이 **메시지(데이터)**를 주고받을 수 있도록 설계된 시스템으로 메시지를 분산 처리하고 비동기적으로 처리할 수 있습니다. 이 시스템은 대규모 애플리케이션에서 데이터 처리량을 효율적으로 분산시키고 시스템의 안정성과 확장성을 높이는 데 주로 사용됩니다.

🚀 메시지 시스템을 이해하는데 필수적인 개념들이 있습니다.
- 메시지(Message): 데이터 또는 작업 요청을 나타내는 단위입니다.
- 큐(Queue): 메시지를 일시적으로 저장하는 저장소입니다. 큐에 메시지를 추가하고 메시지를 꺼내어 처리합니다.
- 프로듀서(Producer) or (Publisher): 메시지를 생성하여 큐에 넣는 역할을 합니다. 예를 들어, 웹 애플리케이션에서 사용자의 요청을 메시지로 큐에 넣을 수 있습니다.
- 컨슈머(Consumer): 큐에서 메시지를 읽고 처리하는 역할을 합니다. 하나의 컨슈머가 여러 메시지를 처리할 수 있으며 여러 컨슈머가 메시지를 병렬로 처리할 수도 있습니다.
- 브로커(Broker): 프로듀서와 컨슈머 간의 메시지를 중개하는 시스템입니다. 브로커는 큐를 관리하고 메시지가 컨슈머에게 전달되도록 조율합니다. 대표적인 메시지 브로커로는 RabbitMQ, Kafka, Redis 등이 있습니다.
- 비동기 처리: 메시지 분산 처리 시스템은 일반적으로 비동기 방식을 사용하여 메시지를 처리합니다. 프로듀서가 메시지를 큐에 넣으면 컨슈머가 나중에 해당 메시지를 처리합니다. 이를 통해 애플리케이션의 응답 시간을 줄일 수 있습니다.

~ 추가 작성 중 ~