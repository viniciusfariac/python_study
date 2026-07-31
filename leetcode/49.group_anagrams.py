class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strs = []
        hash_words = []
        for i in strs:
            hash_temp = {}
            for j in i:
                if j in hash_temp:
                    hash_temp[j] += 1
                else:
                    hash_temp[j] = 1
            index = -1
            
            for j, d in enumerate(hash_words):
                if d == hash_temp:
                    index = j
                    break          
            
            if index != -1:
                hash_strs[j].append(i)
            else:
                hash_strs.append([i])
                hash_words.append(hash_temp)
        return hash_strs