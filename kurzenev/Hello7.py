i = 0
N = 1
def shet(arg):
    for i in range(len(arg)):
        for j in range(len(arg)):
            if arg[i] == arg[j]:
                N = N + 1
                continue
            if j == len(arg) - 1:
                return(arg[i]+N)