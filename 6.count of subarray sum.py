def findcountsubarraysum(arr):
    hash={}
    hash[0]=1

    ans=0
    sum=0

    for i in range(len(arr)):

        sum+=arr[i]

        if sum not in hash:
            hash[sum]=1
        else:
            ans+=hash[sum]
            hash[sum]+=1
    print(ans)
    print(hash)

arr=[2,8,-3,-5,2,-4,6,1,2,1,-3,4]
findcountsubarraysum(arr)

