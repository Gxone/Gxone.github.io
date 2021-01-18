---
title: "[Java] 오버라이딩(overriding), 오버로딩(overloading)"
categories: Java
---

## 오버라이딩 (overriding)
오버라이딩은 <b>슈퍼클래스에 있는 메소드를 서브클래스에서 다른 작업을 하도록 동일한 함수 이름으로 재정의</b>하는 것이다. 

```java
class Employee {
    public void work() {
        System.out.println("\tEmployee \""+nama + "\" does his best.");
    }
}

class Manager extends Employee {
    public void work() {
        System.out.println("Manager \""+name +"\" works hard with his subordinates in "+dept+" dept.");
    }
}
```
```Employee``` 클래스와 ```Manager``` 클래스는 서로 하는 일이 다르기 때문에 ```work()``` 메소드를 다르게 정의해주어야한다. 이때 ```Manager``` 클래스에서 ```Employee``` 클래스의 ```work()``` 메소드를 오버라이드해서 <b>재정의</b>해준다!
<br><br>
## 오버로딩 (overloading)
오버로딩은 한 클래스 내에서 <b>함수의 이름은 동일하지만 함수의 매개 변수(매개 변수의 수, 타입)가 다른 경우</b>를 말한다.
```java
int = int + int;
float = float + float;
```
위와같이 동일한 연산자가 자료의 타입에 따라 다른 작업을 하는 것은 연산자 오버로딩이라고 한다.
연산자와 마찬가지로 함수도 오버로딩을 할 수 있는데 내부적으로는 다른 작업을 하더라도 의미가 같다면 같은 함수 이름을 사용할 수 있다.
하지만 함수의 매개 변수는 달라야 한다.  
함수 이름, 매개 변수의 수, 매개 변수의 타입을 <b>시그내쳐(signature)</b>라고 한다. 프로그래머가 동일한 함수 이름을 사용하면 컴파일러가 시그내쳐를 이용해서 다른 이름으로 변경하여 컴파일 한다. 따라서 함수 이름은 같은데 시그내쳐도 동일하다면 컴파일러가 구분 할 수 없어 컴파일 에러가 발생한다! (함수의 리턴 타입은 시그내쳐에 포함되지 않는다.)

```java
class Overloading {
    public void said() {
        System.out.printlm("Hellp ?");
    }

    public void say (String msg) {
        System.out.printlm(msg);
    }

    public void say(String msg, int n) {
        for(int i = 0; i <n; i++>) {
            System.out.println(msg);
        }
    }

    public static void main (String args[]) {
        Overloading a = new Overloading();
        a.say();
        a.say("How are you ?");
        a.say("I am fine.", 3);
    }
}
```
---
참고 자료: 프로그래머를 위한 JAVA2