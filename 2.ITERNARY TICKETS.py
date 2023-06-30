def findtickets(hash):
    hash1={}

    for src in hash:

        des=hash[src]

        hash1[des]=False

        if src not in hash1:
            hash1[src]=True

    src=''
    for x in hash1:
        if hash1[x]==True:
            src=x
            break

    while(True):

        if src in hash:
            print(src,'->',end='')
            src=hash[src]
        else:
            print(src,'.')
            break


hash={}
hash['Chennai']='Bangalore'
hash['Bombay']='Delhi'
hash['Goa']='Chennai'
hash['Delhi']='Goa'

findtickets(hash)



