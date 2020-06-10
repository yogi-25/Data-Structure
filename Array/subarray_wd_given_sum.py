for i in range(int(input())):
    n,s=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    flag=0
    for st in range(n):
        for e in range(s,n):
            if sum(arr[s:e+1]==s):
                print(s+1,e+1)
                flag=1
                break
        if(flag==1):
            break
    if(flag==0):
        print(-1)