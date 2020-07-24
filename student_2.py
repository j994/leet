def checkRecord(n: int) -> int:
    import itertools
    count = 0
    test = map(list, itertools.combinations_with_replacement(
        ['A', 'L', 'P'], n))
    for t in test:
        a = ''.join(t)
        print(a)
        if a.count('A') < 2 and a.count('LLL') < 1:
            count += 1
    return count


a = checkRecord(2)
print(a)
