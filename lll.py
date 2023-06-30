class Solution:
    def findAnagrams(self, s: str, p: str) :
        hash1 = {}
        hash2 = {}
        res = []

        def issame(hash1, hash2):
            for x in hash2:
                if hash2[x] != hash1.get(x, 0):
                    return False
            return True

        for i in range(len(p)):

            if s[i] not in hash1:
                hash1[s[i]] = 0
            hash1[s[i]] += 1

            if p[i] not in hash2:
                hash2[p[i]] = 0
            hash2[p[i]] += 1



        print(hash1)
        print(hash2)

        i = len(p)
        while (i < len(s)):

            if issame(hash1, hash2):
                res.append(i-len(p))

            if hash1[s[i-len(p)]] == 1:
                del hash1[s[i-len(p)]]
            else:
                hash1[s[i-len(p)]] -= 1



            ch = s[i]
            hash1[ch] = hash1.get(ch, 0) + 1
            i += 1
        if issame(hash1, hash2):
            res.append(i-len(p))
        return res

s="cbaebabacd"
p="abc"
x=Solution()
res=x.findAnagrams(s,p)
print(res)

