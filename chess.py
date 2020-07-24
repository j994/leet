def chess():
    total = 0
    for i in range(64):
        total += pow(2, i)
    return total


a = chess()
print(a)
