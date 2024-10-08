class Solution:
    def compute_arr(self,needle:str) -> list:
        length =0
        lps = [0] * len(needle)

        i = 1

        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i +=1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        lps = self.compute_arr(needle)
        i = j = 0

        while i <len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j +=1
            if j == len(needle):
                return i-j

            elif i <len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1

