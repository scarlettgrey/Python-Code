lcount = int(input())
arr = []

arr = list(map(int, input().split()))

for b in range(int(lcount/2)):
    temp = arr[b]
    arr[b] = arr[lcount - b - 1]
    arr[lcount - b - 1] = temp

print(arr) 