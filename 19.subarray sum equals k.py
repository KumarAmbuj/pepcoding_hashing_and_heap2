def countsubarray(arr,k):
    sum=0
    hash={}
    hash[sum]=1
    ans=0

    for i in range(len(arr)):

        sum=sum+arr[i]

        if sum-k in hash:
            ans+=hash[sum-k]

        hash[sum]=hash.get(sum,0)+1
    print(ans)

arr=[3,9,-2,4,1,-7,2,6,-5,8,-3,-7,6,2,1]
countsubarray(arr,5)
