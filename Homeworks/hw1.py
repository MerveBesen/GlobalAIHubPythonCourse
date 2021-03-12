odd = list()
even = list()
merge = list()
for i in range(100):
    if i%2 == 0:
        odd.append(i)
    else:
        even.append(i)


merge = odd + even

for i in merge:
    i *= 2
    print(i, type(i))

