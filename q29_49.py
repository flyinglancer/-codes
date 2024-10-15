class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_group = {}

        for ftr in strs:
            sorted_s = ''.join(sorted(ftr))
            if sorted_s in a_group:
                a_group[sorted_s].append(ftr)
            else:
                a_group[sorted_s] = [ftr]
        return list(a_group.values())

        
