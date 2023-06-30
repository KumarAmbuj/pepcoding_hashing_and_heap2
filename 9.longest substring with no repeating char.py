def findlongestsubstring(s):
    ans=0
    hash={}

    i=-1
    j=-1


    while(True):

        f1=False
        f2=False

        while(i<len(s)-1):
            f1=True
            i+=1
            ch=s[i]
            hash[ch]=hash.get(ch,0)+1

            if hash[ch]==2:
                break
            else:
                ans=max(ans,i-j)
        while(j<i):
            f2=True
            j+=1
            ch=s[j]

            if hash[ch]==1:
                del hash[ch]
            else:
                hash[ch]-=1

            if hash.get(ch,0)==1:
                break
        if f1==False and f2==False:
            break
    print(ans)

s='abbacbcdbadbdbbdcb'
findlongestsubstring(s)


