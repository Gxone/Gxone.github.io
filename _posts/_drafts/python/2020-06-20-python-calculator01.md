---
title: "200620 Python Calculator 01 - GUI"
categories: python
tag: wecode
---

```py
import tkinter as tkt # 파이썬의 표준 GUI 라이브러리

equa = ""
app = tkt.Tk()
app.title("계산기") # 윈도우의 이름 설정
app.resizable(0, 0)  # 윈도우 크기 고정
equation = tkt.StringVar()
equation.set("숫자를 입력하세요: ") # StringVar()로 정의된 변수는 문자열 변수가 아니기 떄문에 set메소드 사용.
rst = tkt.Label(app, textvariable=equation).grid(row=2, columnspan=8)

btn0 = tkt.Button(app, text="0", height=2, width=4, relief=tkt.SOLID).grid(column=0, row=6, padx=5, pady=5)
btn1 = tkt.Button(app, text="1", height=2, width=4, relief=tkt.SOLID).grid(column=0, row=3, padx=5, pady=5)
btn2 = tkt.Button(app, text="2", height=2, width=4, relief=tkt.SOLID).grid(column=1, row=3, padx=5, pady=5)
btn3 = tkt.Button(app, text="3", height=2, width=4, relief=tkt.SOLID).grid(column=2, row=3, padx=5, pady=5)
btn4 = tkt.Button(app, text="4", height=2, width=4, relief=tkt.SOLID).grid(column=0, row=4, padx=5, pady=5)
btn5 = tkt.Button(app, text="5", height=2, width=4, relief=tkt.SOLID).grid(column=1, row=4, padx=5, pady=5)
btn6 = tkt.Button(app, text="6", height=2, width=4, relief=tkt.SOLID).grid(column=2, row=4, padx=5, pady=5)
btn7 = tkt.Button(app, text="7", height=2, width=4, relief=tkt.SOLID).grid(column=0, row=5, padx=5, pady=5)
btn8 = tkt.Button(app, text="8", height=2, width=4, relief=tkt.SOLID).grid(column=1, row=5, padx=5, pady=5)
btn9 = tkt.Button(app, text="9", height=2, width=4, relief=tkt.SOLID).grid(column=2, row=5, padx=5, pady=5)
btnPlus = tkt.Button(app, text="+", height=2, width=4, relief=tkt.SOLID).grid(column=3, row=3, padx=5, pady=5)
btnMinus = tkt.Button(app, text="-", height=2, width=4, relief=tkt.SOLID).grid(column=3, row=4, padx=5, pady=5)
btnMultiply = tkt.Button(app, text="*", height=2, width=4, relief=tkt.SOLID).grid(column=3, row=5, padx=5, pady=5)
btnDivide = tkt.Button(app, text="/", height=2, width=4, relief=tkt.SOLID).grid(column=3, row=6, padx=5, pady=5)
btnEqual = tkt.Button(app, text="=", height=2, width=4, relief=tkt.SOLID).grid(column=2, row=6, padx=5, pady=5)
btnClear = tkt.Button(app, text="C", height=2, width=4, relief=tkt.SOLID).grid(column=1, row=6, padx=5, pady=5)
btnTan = tkt.Button(app, text="tan", height=2, width=4, relief=tkt.SOLID).grid(column=4, row=3, padx=5, pady=5)
btnSin = tkt.Button(app, text="sin", height=2, width=4, relief=tkt.SOLID).grid(column=4, row=4, padx=5, pady=5)
btnCos = tkt.Button(app, text="cos", height=2, width=4, relief=tkt.SOLID).grid(column=4, row=5, padx=5, pady=5)
btnPow = tkt.Button(app, text="x^y", height=2, width=4, relief=tkt.SOLID).grid(column=4, row=6, padx=5, pady=5)

app.mainloop()
```
##### Tkinter
tkinter는 파이썬의 표준 GUI 라이브러리로써 표준으로 설치되어있다. 

##### StringVar
텍스트를 저장하는 변수. 변수의 값이 변하면 GUI 화면의 내용도 변경된다. textvariable 옵션으로 연결.

##### Grid 레이아웃
계산기의 모양을 구현하기 위해 그리드 레이아웃을 사용하여 각각의 버튼을 column과 row 옵션을 통해 배치한다. 