def findequalno(arr):
    hash={}

    c0=0
    c1=0
    c2=0
    ans=0

    key=str(c1-c0)+'#'+str(c2-c1)

    hash[key]=-1

    for i in range(len(arr)):

        if arr[i]==0:
            c0+=1
        elif arr[i]==1:
            c1+=1
        elif arr[i]==2:
            c2+=1

        key=str(c1-c0)+'#'+str(c2-c1)

        if key in hash:
            if ans==0 or i-hash[key]>ans:
                ans=i-hash[key]
        else:
            hash[key]=i
    print(ans)
arr=[1,1,2,0,1,0,1,2,1,2,2,0,1]
findequalno(arr)