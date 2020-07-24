def reverseWords(s: str) -> str:
    x = s.strip().split(' ')
    result = ''
    for i in range(1, len(x) + 1):
        if not x[-i]:
            continue
        if i == len(x):
            result += x[-i]
        else:
            result += x[-i] + ' '
    return result


print(reverseWords('a good   example'))
