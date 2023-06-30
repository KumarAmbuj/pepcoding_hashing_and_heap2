def countofsubarray(s,k):
    hash={}
    i=-1
    j=-1
    ans=0

    while(True):

        f1=False
        f2=False

        while (i < len(s) - 1):
            f1=True

            i += 1
            ch = s[i]
            hash[ch] = hash.get(ch, 0) + 1

            if len(hash) == k:
                ans += len(s) - i
                break
        while (j < i):
            f2=True
            j += 1
            ch = s[j]

            if hash[ch] == 1:
                del hash[ch]
            else:
                hash[ch] -= 1

            if len(hash) == k:
                ans += len(s) - i
            else:
                break
        if f1==False and f2==False:
            break
    print(ans)
s='2535241314'
countofsubarray(s,5)


