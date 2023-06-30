def iskanagram(s1,s2,k):

    if len(s1)!=len(s2):
        print(False)
        return

    hash={}
    for x in s1:
        hash[x]=hash.get(x,0)+1

    for x in s2:
        if x in hash and hash[x]>0:
            hash[x]-=1

    count=0

    for x in hash:
        if hash[x]>0:
            count+=1
    print(count<=k)

s1='aabbbc'
s2='badaba'
iskanagram(s1,s2,2)
