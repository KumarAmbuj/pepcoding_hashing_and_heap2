def findsmallestwindow(s1,s2):
    map1={}
    map2={}

    dcount=len(s2)

    count=0
    ans=0

    for i in range(len(s2)):
        if s2[i] not in map2:
            map2[s2[i]]=0
        map2[s2[i]]+=1

    i=-1
    j=-1

    while(True):

        f1=False
        f2=False

        while (i < len(s1) - 1 and count < dcount):
            f1=True

            i+=1
            ch=s1[i]
            if ch not in map1:
                map1[ch] = 0
            map1[ch] += 1

            if map1[ch] <= map2.get(ch,0):
                count += 1


        while(j<i and count==dcount):

            f2=True

            if ans==0 or i-j<ans:
                ans=i-j

            j+=1

            ch=s1[j]

            if map1[ch]==1:
                del map1[ch]
            else:
                map1[ch]-=1

            if map1.get(ch,0)<map2.get(ch,0):
                count-=1

        if f1==False and f2==False:
            break
    print(ans)

s1='dbaecbbabdcaafbddcabgba'
s2='abbcdc'

findsmallestwindow(s1,s2)



