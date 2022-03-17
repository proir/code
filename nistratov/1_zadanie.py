def merge_lists(a, b):
    c = []
    for i in range(len(a)):
        c.append([a[i], b[i]])
    return c
    
    
a = [1, 2, 3]
b = [11, 22, 33]
c = merge_lists(a, b)
print(c)