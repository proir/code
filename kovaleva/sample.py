def average_length(a):
    total_length = 0
    for word in a:
        total_length = total_length + len(word)

    return total_length / len(a)


x = ['abc', 'dgfj', 'jhfh', 'fgj']
result = average_length(x)
print(result)