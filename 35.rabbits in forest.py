import math
def findrabbits(arr):
    hash={}

    for x in arr:
        if x not in hash:
            hash[x]=0
        hash[x]+=1

    ans=0

    for x in hash:
        n=x+1
        ans+=int(math.ceil(hash[x]/n))*n
    print(ans)

arr=[2,2,3,1,0,2,2,3,1]
findrabbits(arr)
