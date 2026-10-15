class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list = list(s)
        t_list = list(t)

        return sorted(s) == sorted(t)
        