def finddistinctelements(arr,k):
    hash={}
    ans=[]
    for i in range(k-1):
        hash[arr[i]]=hash.get(arr[i],0)+1

    j=0
    for i in range(k-1,len(arr)):
        hash[arr[i]]=hash.get(arr[i],0)+1
        ans.append(len(hash))

        if hash[arr[j]]==1:
            del hash[arr[j]]
        else:
            hash[arr[j]]-=1
        j+=1
    print(ans)

arr=[2,5,5,6,3,2,3,2,4,5,2,2,2,2,3,6]
finddistinctelements(arr,4)

