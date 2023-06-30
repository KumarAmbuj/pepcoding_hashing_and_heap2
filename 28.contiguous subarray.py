def findcontiguousarray(arr):
    hash={}
    hash[0]=1
    sum=0
    ans=0
    for x in arr:
        if x==0:
            sum-=1
        else:
            sum+=x
        if sum in hash:
            ans+=hash[sum]
            hash[sum]+=1
        else:
            hash[sum]=1

    print(ans)

arr=[0,0,1,0,1,0,1,1,0,0,1,1,1]
findcontiguousarray(arr)