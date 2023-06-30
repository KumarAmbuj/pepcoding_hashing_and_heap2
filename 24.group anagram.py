def groupanagram(arr):

    hash={}

    for x in arr:

        map=[0 for i in range(26)]

        for z in x:

            map[ord(z)-ord('a')]+=1

        key=''

        for i in range(len(map)):
            if map[i]!=0:
                key=key+chr(i+ord('a'))+str(map[i])

        if key not in hash:
            hash[key]=[]
        hash[key].append(x)

    for x in hash:
        print(hash[x])

arr=['abcc','acbc','badc','abcd','dabb','babd','dbca','cabc']
groupanagram(arr)
