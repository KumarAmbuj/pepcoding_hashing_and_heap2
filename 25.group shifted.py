def groupshifted(arr):

    hash={}

    for x in arr:
        key=''
        if len(x)==1:
            key='#'

            if key not in hash:
                hash[key]=[]
            hash[key].append(x)
        else:

            for i in range(1,len(x)):
                diff=ord(x[i])-ord(x[i-1])

                if diff<0:
                    diff+=26

                key=key+str(diff)+'#'
            key=key+'.'

            if key not in hash:
                hash[key]=[]
            hash[key].append(x)

    for x in hash:
        print(hash[x])

arr=['acd','dfg','wyz','yab','mop','bdfh','a','x','moqs']
groupshifted(arr)

