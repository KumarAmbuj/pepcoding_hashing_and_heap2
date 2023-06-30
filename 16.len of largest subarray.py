def findmaxarray(arr):

    ans=0

    for i in range(len(arr)-1):
        mx=arr[i]
        mn=arr[i]
        unique=set()
        unique.add(arr[i])

        for j in range(i+1,len(arr)):

            if arr[j] in unique:
                break

            mx=max(mx,arr[j])
            mn=min(mn,arr[j])

            if mx-mn==j-i:
                ans=max(ans,j-i+1)
    print(ans)

arr=[9,2,7,5,6,23,24,22,23,19,17,16,18,39,0]
findmaxarray(arr)
