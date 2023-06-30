def findsumdivisiblebyk(arr,k):
    hash={}
    hash[0]=-1
    sum=0
    rem=0
    ans=0
    for i in range(len(arr)):
        sum+=arr[i]
        rem=sum%k

        if rem<0:
            rem+=k

        if rem in hash:

            if ans==0 or i-hash[rem]>ans:
                ans=i-hash[rem]
        else:
            hash[rem]=i

    print(ans)
arr=[2,4,8,1,7,3,6,1,9,2,7,3]
findsumdivisiblebyk(arr,5)
