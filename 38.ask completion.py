def taskcompletion(arr):
    hash=set()

    for x in arr:
        hash.add(x)

    p1=[]
    p2=[]

    flag=False
    for i in range(1,16):
        if i not in hash:
            hash.add(i)

            if flag:
                p1.append(i)
            else:
                p2.append(i)
            flag=not flag
    print(p1)
    print(p2)
arr=[2,5,6,7,9,4]
taskcompletion(arr)
