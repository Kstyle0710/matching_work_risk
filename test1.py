import pandas as pd

works = pd.read_excel("./source/작업행동.xlsx")
risks = pd.read_excel("./source/표준 위험요인.xlsx")

for t, work in enumerate(works["형태소"]):
    work = str(work).split(",")
    target = []
    for i in work:
        i = i.strip(" ")
        target.append(i)
    print(t)

    for n, k in enumerate(target):
        print("--------------------------")
        # print(n)
        print(k)
        for p, risk in enumerate(risks["키워드"]):
            risk = str(risk).split(",")
            compare = []
            for a in risk:
                a = a.strip(" ")
                compare.append(a)
            print(p)
            print(compare)

            if k in compare:
                print('matching')
            else:
                print('not matching')

