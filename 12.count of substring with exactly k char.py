def countsubstring(s,k):

    ans=0
    hash1={}
    hash2={}

    si=-1
    bi=-1

    j=-1

    while(True):
        f1=False
        f2=False
        f3=False

        while(bi<len(s)-1):
            f1=True
            bi+=1
            ch=s[bi]
            hash1[ch]=hash1.get(ch,0)+1

            if len(hash1)==k+1:
                del hash1[ch]
                bi-=1
                break
        while(si<bi):
            f2=True
            si+=1
            ch=s[si]
            hash2[ch]=hash2.get(ch,0)+1

            if len(hash2)==k:
                del hash2[ch]
                si-=1
                break

        while(j<si):
            f3=True

            if len(hash1)==k and len(hash2)==k-1:
                ans+=bi-si

            j+=1
            ch=s[j]

            if hash1[ch]==1:
                del hash1[ch]
            else :
                hash1[ch]-=1

            if hash2[ch]==1:
                del hash2[ch]
            else:
                hash2[ch]-=1

            if len(hash1)<k or len(hash2)<k-1:
                break
        if f1==False and f2==False and f3==False:
            break

    print(ans)



s='abcabdabbcfa'
countsubstring(s,3)
