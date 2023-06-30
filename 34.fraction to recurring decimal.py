def fraction(n1,n2):

    ans=''
    q=n1//n2
    r=n1%n2
    ans=ans+str(q)
    hash={}

    if r==0:
        return ans
    else:
        ans+='.'

        while(r!=0):
            if r in hash:
                ans=ans[:hash[r]]+'('+ans[hash[r]:]+')'
                break
            else:
                hash[r]=len(ans)

                r=r*10

                q=r//n2
                r=r%n2
                ans+=str(q)
    return ans




res=fraction(8,4)
print(res)

res=fraction(37,2)
print(res)

res=fraction(428,125)
print(res)

res=fraction(14,3)
print(res)

res=fraction(47,18)
print(res)

res=fraction(93,7)
print(res)


