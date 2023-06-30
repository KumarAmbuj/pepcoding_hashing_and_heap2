def findcontiguousarray(arr):
    hash={}

    sum=0
    ans=0
    hash[sum]=-1

    for i in range(len(arr)):
        x=arr[i]
        if x==0:
            sum+=-1
        else:
            sum+=1

        if sum in hash:
            if ans==0 or i-hash[sum]>ans:
                ans=i-hash[sum]
        else:
            hash[sum]=i

    print(ans)

arr=[0,0,1,0,1,0,1,1,0,0,1,1,1]
findcontiguousarray(arr)
