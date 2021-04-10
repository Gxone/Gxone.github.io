---
title: "200702 BeautifulSoup Parser"
categories: python
tag: 
- wecode 
- BeautifulSoup
---
```py
import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    # urllib를 통해서 웹에 있는 소스 가져오기
    url = "http://news.jtbc.joins.com/section/index.aspx?scode=70"
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")

    times = [] # 기사의 날짜를 넣는 배열
    for i in range(0, 20):
        times.append(soup.find_all("span", class_="date")[i].get_text().strip()) # 인자의 조건에 맞는 모든 태그들을 가져온다. Html 문서의 텍스트를 추출한 뒤 문자열 양 끝의 공백 제거.
        print("times" + str(i) + "->" + times[i])

    edited = []
    for i in range(0, len(times)):
        edited.append(times[i][8:10])
        print("edited" + str(i) + "->" + times[i][8:10]) # "2020-06-30 21:31" 문자열에서 일자 부분만 슬라이싱

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0

    for i in range(0, len(edited)):
        if edited[i] == "26":  # 28일 기사 개수 구하기
            count1 = count1 + 1
        elif edited[i] == "28": # 29일 기사 개수 구하기
            count2 = count2 + 1
        elif edited[i] == "29": # 30일 기사 개수 구하기
            count3 = count3 + 1
        elif edited[i] == "30": # 01일 기사 개수 구하기
            count4 = count4 + 1
        elif edited[i] == "01":  # 01일 기사 개수 구하기
            count5 = count5 + 1

    # 파이 차트 그리기
    days = [count1, count2, count3, count4, count5]
    labels = ['26', '28', '29', '30', '01']
    colors = ['red', 'blue', 'green', 'yellow', 'orange']
    plt.pie(days, labels=labels, colors=colors, startangle=90, autopct='%.2f%%')
    plt.show()

if __name__ == "__main__":
    main()
```
