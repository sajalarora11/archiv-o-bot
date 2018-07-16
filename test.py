x = [51, 21, 66, 43, 71]
for i in x:
    if i < 40:
        print(i)
    else:
        rem = 5-(i%5)
        res = i + rem
        if res - i < 3:
            print(res)
    