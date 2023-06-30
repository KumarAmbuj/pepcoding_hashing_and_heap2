def findsequence(arr):
    hash=set()

    mn=arr[0]
    mx=arr[0]
    hash.add(arr[0])

    for  x in arr:
        mx=max(mx,x)
        mn=min(mn,x)
        hash.add(x)

    d=(mx-mn)//(len(arr)-1)

    for i in range(len(arr)):
        ne=mn+i*d
        if ne not in hash:
            return False

    return True


arr=[17,9,5,29,1,25,13,37,21,33]
res=findsequence(arr)
print(res)