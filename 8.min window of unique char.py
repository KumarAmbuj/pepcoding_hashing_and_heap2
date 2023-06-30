def finduniquechar(s1):
    ans=len(s1)

    hash={}

    i=-1
    j=-1

    unique=set()
    for x in s1:
        unique.add(x)


    while(True):
        f1=False
        f2=False

        while(i<len(s1)-1 and len(hash)<len(unique)):

            f1=True
            i+=1
            ch=s1[i]

            if ch not in hash:
                hash[ch]=0
            hash[ch]+=1


        while(j<i and len(unique)==len(hash)):
            f2=True



            ans=min(ans,i-j)

            j+=1
            ch=s1[j]

            if hash[ch]==1:
                del hash[ch]
            else:
                hash[ch]-=1
        if f1==False and f2==False:
            break
    print(ans)


s='bbacacdcbbcaadcdca'
finduniquechar(s)
