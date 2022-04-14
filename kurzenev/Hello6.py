def result(agr1, agr2):
    c = []
    for i in agr1:
        for j in agr2:
            if i == j:
                c.append(i)
                break