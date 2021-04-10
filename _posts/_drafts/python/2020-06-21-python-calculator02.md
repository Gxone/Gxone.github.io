---
title: "200621 Python Calculator 02 - 함수"
categories: python
tag: wecode
---
```py
import tkinter as tkt # 파이썬의 표준 GUI 라이브러리
import math

equa = ""
app = tkt.Tk()
app.title("계산기") # 윈도우의 이름 설정
app.resizable(0, 0)  # 윈도우 크기 고정

equation = tkt.StringVar()
equation.set("숫자를 입력하세요: ") # StringVar()로 정의된 변수는 문자열 변수가 x, 따라서 set메소드 사용.
rst = tkt.Label(app, textvariable=equation).grid(row=2, columnspan=8)

# 이벤트 함수
def btnPress(num): # 버튼을 눌렀을 떄 label에 set
    global equa # 전역 변수 사용 시 함수 밖에서 선언 된 변수 변경 가능
    equa = equa + str(num)
    equation.set(equa)

def equalPress():
    global equa
    if '^' in equa: # '^' 문자열 인덱스 위치 알아낸 후 pow([0] ~ [inx-1], [idx+1] ~ [length-1])
        idx = equa.find('^')
        n1 = equa[0:idx] # idx -1 까지
        n2 = equa[idx+1:]
        total = pow(float(n1), float(n2))
    else:
        total = str(eval(equa)) # 인자에 스트링 값을 넣으면 그대로 계산 결과 출력.
    equation.set(total)
    equa = ""

def tanPress():
    global equa
    total = math.tan(math.pi * float(equa) / 180)
    equation.set(total)
    equa = ""

def cosPress():
    global equa
    total = math.cos(math.pi * float(equa) / 180)
    equation.set(total)
    equa = ""

def sinPress():
    global equa
    total = math.sin(math.pi * float(equa) / 180)
    equation.set(total)
    equa = ""

def sqrtPress():
    global equa
    total = math.sqrt(float(equa))
    equation.set(total)
    equa = ""

def clearPress():
    global equa
    equa = ""
    equation.set("")

# btn GUI
btn0 = tkt.Button(app, text="0", bg='white', command=lambda: btnPress(0), height=2, width=4, relief=tkt.SOLID).grid(column=0, row=6, padx=5, pady=5)
btn1 = tkt.Button(app, text="1", bg='white', command=lambda: btnPress(1), height=2, width=4, relief=tkt.SOLID).grid(column=0, row=3, padx=5, pady=5)
btn2 = tkt.Button(app, text="2", bg='white', command=lambda: btnPress(2), height=2, width=4, relief=tkt.SOLID).grid(column=1, row=3, padx=5, pady=5)
btn3 = tkt.Button(app, text="3", bg='white', command=lambda: btnPress(3), height=2, width=4, relief=tkt.SOLID).grid(column=2, row=3, padx=5, pady=5)
btn4 = tkt.Button(app, text="4", bg='white', command=lambda: btnPress(4), height=2, width=4, relief=tkt.SOLID).grid(column=0, row=4, padx=5, pady=5)
btn5 = tkt.Button(app, text="5", bg='white', command=lambda: btnPress(5), height=2, width=4, relief=tkt.SOLID).grid(column=1, row=4, padx=5, pady=5)
btn6 = tkt.Button(app, text="6", bg='white', command=lambda: btnPress(6), height=2, width=4, relief=tkt.SOLID).grid(column=2, row=4, padx=5, pady=5)
btn7 = tkt.Button(app, text="7", bg='white', command=lambda: btnPress(7), height=2, width=4, relief=tkt.SOLID).grid(column=0, row=5, padx=5, pady=5)
btn8 = tkt.Button(app, text="8", bg='white', command=lambda: btnPress(8), height=2, width=4, relief=tkt.SOLID).grid(column=1, row=5, padx=5, pady=5)
btn9 = tkt.Button(app, text="9", bg='white', command=lambda: btnPress(9), height=2, width=4, relief=tkt.SOLID).grid(column=2, row=5, padx=5, pady=5)
btnPlus = tkt.Button(app, text="+", bg='white', command=lambda: btnPress("+"), height=2, width=4, relief=tkt.SOLID).grid(column=3, row=3, padx=5, pady=5)
btnMinus = tkt.Button(app, text="-", bg='white', command=lambda: btnPress("-"), height=2, width=4, relief=tkt.SOLID).grid(column=3, row=4, padx=5, pady=5)
btnMultiply = tkt.Button(app, text="*", bg='white', command=lambda: btnPress("*"), height=2, width=4, relief=tkt.SOLID).grid(column=3, row=5, padx=5, pady=5)
btnDivide = tkt.Button(app, text="/", bg='white', command=lambda: btnPress("/"), height=2, width=4, relief=tkt.SOLID).grid(column=3, row=6, padx=5, pady=5)
btnEqual = tkt.Button(app, text="=", bg='white', command=equalPress, height=2, width=4, relief=tkt.SOLID).grid(column=2, row=6, padx=5, pady=5)
btnClear = tkt.Button(app, text="C", bg='white', command=clearPress, height=2, width=4, relief=tkt.SOLID).grid(column=1, row=6, padx=5, pady=5)
btnTan = tkt.Button(app, text="tan", bg='white', command=tanPress, height=2, width=4, relief=tkt.SOLID).grid(column=4, row=3, padx=5, pady=5)
btnSin = tkt.Button(app, text="sin", bg='white', command=sinPress, height=2, width=4, relief=tkt.SOLID).grid(column=4, row=4, padx=5, pady=5)
btnCos = tkt.Button(app, text="cos", bg='white', command=cosPress, height=2, width=4, relief=tkt.SOLID).grid(column=4, row=5, padx=5, pady=5)
btnPow = tkt.Button(app, text="x^y", bg='white', command=lambda: btnPress("^"), height=2, width=4, relief=tkt.SOLID).grid(column=4, row=6, padx=5, pady=5)
btnDot = tkt.Button(app, text="dot", bg='white', command=lambda: btnPress("."), height=2, width=4, relief=tkt.SOLID).grid(column=5, row=6, padx=5, pady=5)
btnPi = tkt.Button(app, text="pi", bg='white', command=lambda: btnPress(math.pi), height=2, width=4, relief=tkt.SOLID).grid(column=5, row=5, padx=5, pady=5)
btnMod = tkt.Button(app, text="%", bg='white', command=lambda: btnPress("%"), height=2, width=4, relief=tkt.SOLID).grid(column=5, row=4, padx=5, pady=5)
btnSqrt = tkt.Button(app, text="sqrt", bg='white', command=sqrtPress, height=2, width=4, relief=tkt.SOLID).grid(column=5, row=3, padx=5, pady=5)

app.mainloop()
```
## 결과물  
<img width="350px" src="https://user-images.githubusercontent.com/26542094/86526325-aab84e80-becd-11ea-8b6d-4c6d25b5c770.png">{:.aligncenter}

## 함수
##### btnPress() 함수  
버튼을 눌렀을 때 label에 계산식을 추가하기 위한 함수이다. command 옵션을 통해 각 버튼을 눌렀을 때 실행되는 함수를 설정할 수 있고 <i style="background:#dbc6eb; color: #fff">lambda 함수를 통해 인자 (숫자 및 문자열)</i> 를 넘길 수 있다. 
```py
def btnPress(num): # 버튼을 눌렀을 떄 label에 set
    global equa # 전역 변수 사용 시 함수 밖에서 선언 된 변수 변경 가능
    equa = equa + str(num)
    equation.set(equa)
```
##### equalPress() 함수  
제곱한 값을 구하기 위해서 <i style="background:#dbc6eb; color: #fff"> label의 문자열에 '^'가 포함되어 있다면 pow 함수를 호출</i>하도록 했다. 그렇지 않다면 eval 함수를 통해 계산식의 결과를 문자열로 형 변환해 total 변수에 넣도록 한다. 
```py
def equalPress():
    global equa
    if '^' in equa: # '^' 문자열 인덱스 위치 알아낸 후 pow([0] ~ [inx-1], [idx+1] ~ [length-1])
        idx = equa.find('^')
        n1 = equa[0:idx] # idx -1 까지
        n2 = equa[idx+1:]
        total = pow(float(n1), float(n2))
    else:
        total = str(eval(equa)) # 인자에 스트링 값을 넣으면 그대로 계산 결과 출력.
    equation.set(total)
    equa = ""
```
##### tanPress() 함수
tan, sin, sqrt 와 같은 함수는 math 모듈을 import 한 뒤 사용할 수 있다. 
```py
def tanPress():
    global equa
    total = math.tan(math.pi * float(equa) / 180)
    equation.set(total)
    equa = ""
```
