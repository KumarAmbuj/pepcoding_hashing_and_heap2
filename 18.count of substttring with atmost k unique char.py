def findcountsubarray(s,k):
    ans=0
    hash={}
    i=-1
    j=-1

    while(True):

        while (i < len(s) - 1):
            i += 1
            ch = s[i]
            hash[ch] = hash.get(ch, 0) + 1

            if len(hash) <= k:
                ans += i - j
            else:
                break

        if i==len(s)-1 and len(hash)<=k:
            break
        while(j<i):
            j+=1
            ch=s[j]

            if hash[ch]==1:
                del hash[ch]
            else:
                hash[ch]-=1

            if len(hash)>k:
                continue
            else:
                ans+=i-j
                break
    print(ans)

s='aabcbcdbca'
findcountsubarray(s,2)

