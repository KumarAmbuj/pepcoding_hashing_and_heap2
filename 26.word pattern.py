def wordpattern(arr,p):

    hash1={}
    hash2={}

    for i in range(len(p)):

        if p[i] not in hash1:
            if hash2.get(arr[i],False)==True:
                return False
            else:
                hash1[p[i]]=arr[i]
                hash2[arr[i]]=True

        else:
            if arr[i]!=hash1[p[i]]:
                return False

    return True

p='abbcaa'
arr=['the','pep','pep','coding','the','the']
res=wordpattern(arr,p)
print(res)


p='abbcaa'
arr=['the','pep','pep','coding','that','the']
res=wordpattern(arr,p)
print(res)
