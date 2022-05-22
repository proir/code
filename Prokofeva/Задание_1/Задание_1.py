def reverse(arg):
    result = []
    for i in arg:
        result.insert(0, i)
    return result

def srLength(arg):
    count = 0
    sum = 0
    for i in arg:
        word = i
        count += 1
        sum += len(word)
    return sum / count

def numWord(arg):
    dict = {}
    for i in arg:
        if i in dict:
            continue
        else:
            num = []
            count = -1
            for k in arg:
                count += 1
                if k == i:
                    num.append(count)
            dict[i] = num
    return dict

def similarEl(arg1, arg2):
    result = []
    for i in arg1:
        for k in arg2:
            if k == i and i not in result:
                result.append(i)
    return result

def countWord(arg):
    result = {}
    for i in arg:
        if i in result:
            continue
        else:
            count = 0
            for k in arg:
                if k == i:
                    count += 1
            result[i] = count
    return result

def lengthSort(arg):
    result = arg
    for i in range(0, len(result) - 1):
        for k in range(0, len(result) - i - 1):
            if len(result[k]) > len(result[k+1]):
                result[k], result[k+1] = result[k+1], result[k]
    return result