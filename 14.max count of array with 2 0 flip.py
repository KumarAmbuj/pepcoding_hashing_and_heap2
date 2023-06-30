def findmaxlen(arr,k):
    ans=0
    count=0
    j=-1
    for i in range(len(arr)):

        if arr[i]==0:
            count+=1

        while(count>k):
            j+=1
            if arr[j]==0:
                count-=1

        ans=max(ans,i-j)

    print(ans)
arr=[1,1,0,1,0,0,1,1,0,1,0,1,1]
findmaxlen(arr,2)
