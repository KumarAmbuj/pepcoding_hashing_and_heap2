def check(hash1,hash2):

    for x in hash2:
        if hash2[x]!=hash1.get(x,0):
            return False
    return True

def findnoanagram(s,p):
    hash1={}
    hash2={}

    for i in range(len(p)):
        hash2[p[i]]=hash2.get(p[i],0)+1


    for i in range(len(p)):
        hash1[s[i]]=hash1.get(s[i],0)+1


    count=0

    for i in range(len(p),len(s)):
        if check(hash1,hash2):
            count+=1

        if hash1[s[i-len(p)]]==1:
            del hash1[s[i-len(p)]]
        else:
            hash1[s[i-len(p)]]-=1

        hash1[s[i]]=hash1.get(s[i],0)+1
    if check(hash1, hash2):
        count += 1

    print(count)


s='cbaebabacd'
p='abc'
findnoanagram(s,p)
