#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=191631"

htmlText = requests.get(url).text
bsoup = BeautifulSoup(htmlText, "html.parser")
btab = bsoup.find("div", {"class":"score_result"} )
btrs = btab.find("ul").find_all("li")
btdcols = btrs[1].find_all("div", {"class" : "star_score"})

passengers = []

for tr in btrs[1:]  :
    dic = {}
    tds = tr.find_all("div")
    dic['score'] = tds[0].text.strip().replace(' \t', '').replace('\n', '')
    dic['review'] = tds[1].text.strip()
    dic['sympathy'] = tds[2].text.strip()

    passengers.append(dic)

from tkinter import Tk, ttk, Label, Button, Text, END

window = Tk()
window.title("영화평점및댓글프로그램")
window.geometry("1300x400")
window.resizable(0,0)

title = "영화평점및댓글"
title_feature = Label(window, text = title, font = ("Noto Sans KR", 20))
title_feature.pack(padx = 10, pady = 15)

treeTable = ttk.Treeview(window)
treeTable["columns"] = ("score", "review", "sympathy")
treeTable.column("#0", width = 50, anchor = "center")
treeTable.column("score", width = 100, anchor = "center")
treeTable.column("review", width = 800, anchor = "center")
treeTable.column("sympathy", width = 150, anchor = "center")

treeTable.heading("#0", text="No.", anchor = "center")
treeTable.heading("score", text = "평점", anchor = "center")
treeTable.heading("review", text = "리뷰", anchor = "center")
treeTable.heading("sympathy", text = "공감", anchor = "center")


def setTableItem() :
    treeTable.delete(*treeTable.get_children())
    for idx, report in enumerate(passengers) :
        score = report['score']
        review = report['review']
        sympathy = report['sympathy']
        treeTable.insert("", 'end', iid = None, text = str(idx), values = [score, review, sympathy])





setTableItem()
treeTable.place(x = 10, y = 90, width=1200, height=200)



window.mainloop()

