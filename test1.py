'''
작업행동에서 추출한 형태소와 표준 위험요인의 키워드를 순차적으로 비교하여
매칭될 경우, 작업표준 파일에 위험요인의 id를 맵핑하는 코드
'''

import pandas as pd

works = pd.read_excel("./source/작업행동.xlsx")
risks = pd.read_excel("./source/표준 위험요인.xlsx")

for t, work in enumerate(works["형태소"]):
    work = str(work).split(",")
    target = []
    for i in work:
        i = i.strip(" ")
        target.append(i)
    # print(t)
    print("작업행동 id : {}".format(works["id"][t]))
    basket = []

    for k in target:

        print("--------------------------")
        print(k)
        for p, risk in enumerate(risks["키워드"]):
            risk = str(risk).split(",")
            compare = []
            for a in risk:
                a = a.strip(" ")
                compare.append(a)
            print(compare)

            if k in compare:
                print('matching : {}'.format(risks["id"][p]))
                if risks["id"][p] not in basket:
                    basket.append(risks["id"][p])
        print(basket)
    print(t)
    print(works["위험_id"][t])
    if basket != []:
        works["위험_id"] = works["위험_id"].astype('object')
        works.at[t, "위험_id"] = basket
    print(works["위험_id"][t])

works.to_excel('./result/result3.xlsx')




