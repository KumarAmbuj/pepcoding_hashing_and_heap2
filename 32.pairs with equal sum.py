def findpairsum(arr):

    hash=set()

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):

            sum=arr[i]+arr[j]

            if sum in hash:
                return True
            else:
                hash.add(sum)
    return False
arr=[2,9,3,5,8,6,4]
res=findpairsum(arr)
print(res)