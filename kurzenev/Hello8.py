max = 1000
arg2 = []
def sort(arg):
    for i in range(len(arg)):
        for j in range(len(arg)):
            if arg[j] <= min:
                b = j
                min = arg[j]

            if n == len(arg) - 1:
                c = arg[b]
                arg[b] = arg[i]
                arg[i] = c
                j = j + 1 