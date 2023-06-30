def findpairsum(arr,k):

    hash={}

    for x in arr:
        rem=x%k
        hash[rem]=hash.get(rem,0)+1

    for x in arr:
        rem=x%k

        if rem==0:
            if hash[rem]%2==1:
                print('False ')
                break
        elif 2*rem==k:
            if hash[rem]%2==1:
                print('False')
                break
        else:
            orem=k-rem
            if hash[rem]!=hash[orem]:
                print('False')
                break

    else:
        print('True')

arr=[9,56,25,52,72,44,80,36,96,71,55]
findpairsum(arr,8)


