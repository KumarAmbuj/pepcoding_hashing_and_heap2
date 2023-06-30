def findlargestsubarray(arr):
    hash={}
    hash[0]=-1

    ans=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]

        if sum  in hash:
            ans=max(ans,i-hash[sum])
        else:
            hash[sum]=i

    print(ans)

arr=[2,8,-3,-5,2,-4,6,1,2,1-3,4]
findlargestsubarray(arr)


