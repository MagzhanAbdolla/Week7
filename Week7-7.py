fileIn = input()
l = fileIn.split()
d = dict()

for word in l:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 0
    print(d[word])
