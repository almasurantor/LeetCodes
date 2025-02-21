class Solution(object):
    def groupAnagrams(self, strs):
        seen = {}

        for word in strs:
            sort = "".join(sorted(word))

            if sort in seen:
                seen[sort].append(word)
            else:
                seen[sort] = [word]
        
        return list(seen.values())