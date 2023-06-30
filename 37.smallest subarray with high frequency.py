def findhighfrequency(arr):

    hash1={}
    for i in range(len(arr)):
        if arr[i] not in hash1:
            hash1[arr[i]]=i


    hash2={}
    ei=0
    si=0
    hfr=0
    ans=0
    for i in range(len(arr)):
        if arr[i] not in hash2:
            hash2[arr[i]]=0
        hash2[arr[i]]+=1

        if hash2[arr[i]]>hfr:
            si=hash1[arr[i]]
            hfr=hash2[arr[i]]
            ei=i
            ans=ei-si+1
        elif hash2[arr[i]]==hfr:
            si=hash1[arr[i]]
            ei=i
            if ei-si+1<ans:
                ans=ei-si+1
    print(ans)
    print(si)
    print(ei)
    print(arr[si])
arr=[1,3,2,4,2,3,4,2,5,6,5,5,7]
findhighfrequency(arr)



