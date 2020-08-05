lcount = int(input())

for a in range(lcount):
    str1 = str(input())
    strlen = len(str1)
    count = 0
    for b in range(strlen):
        if(str1[b] == " "):
            break
        count = count + 1
    x = 0
    y = 0
    for c in range(count):
        if str1[x] == str1[y + count + 1]:
            x = x + 1
            y = y + 1
        elif str1[x] != str1[y + count + 1]:
            x = x + 1
            y = 0
        if y == strlen - count -1:
            print("Yes")
            break
    if y != strlen - count - 1:
        print("No")