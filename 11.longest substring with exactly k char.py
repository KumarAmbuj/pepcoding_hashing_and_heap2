def findlongestsubstring(s,k):

    hash={}
    ans=0

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

            if len(hash)<k:
                continue
            elif len(hash)==k:
                if ans==0 or ans<i-j:
                    ans=i-j
            else:
                break

        while(j<i):
            f2=True

            j+=1
            ch=s[j]

            if hash[ch]==1:
                del hash[ch]
            else:
                hash[ch]-=1

            if len(hash)==k:
                ans=max(ans,i-j)
                break

        if f1==False and f2==False:
            break
    print(ans)

s='aabcbcdbca'
findlongestsubstring(s,2)
