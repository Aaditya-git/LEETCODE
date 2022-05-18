size , target = map(int,input().split())
arr = list(map(int,input().split()[:size]))

for i in range(0,len(arr)):
    for j in range(1,len(arr)-1):
        if arr[j]+arr[j+1]==target:
            flag = 1

if flag == 1:
    print(j-1,j)
