arr = list(map(int,input().split()))
value = int(input())

for i in range(0,len(arr)):
    if value in arr:
        print('value is :-',value)
        arr.remove(value)
print(arr)
