def arg(a):
    for i in range(len(a)+1):
        b = a[i]
        x = a.index(b)
        print(f"{b}: {x},")