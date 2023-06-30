def findnoemployee(dic):
    ceo=''

    hash={}

    for x in dic:

        if dic[x]==x:
            ceo=x
            continue

        if dic[x] not in hash:
            hash[dic[x]]=[]
            hash[dic[x]].append(x)
        else:
            hash[dic[x]].append(x)


    hash2={}

    findemployee(ceo,hash2,hash)

    for x in hash2:
        print(x,hash2[x])

def findemployee(node,hash2,hash):
    if node not in hash:
        hash2[node]=0
        return 1

    no=0

    for x in hash[node]:
        c=findemployee(x,hash2,hash)
        no+=c

    hash2[node]=no
    return no+1


hash={}
hash['A']='C'
hash['B']='C'
hash['C']='F'
hash['D']='E'
hash['E']='F'
hash['F']='F'

findnoemployee(hash)





