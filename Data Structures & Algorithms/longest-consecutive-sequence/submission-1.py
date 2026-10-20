class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_list = sorted(nums)
        length = 1
        lengths = []

        if len(nums) == 0:
            return 0

        for i in range(len(sorted_list) - 1):
            if sorted_list[i+1] == sorted_list[i] + 1:
                length += 1
            elif sorted_list[i+1] == sorted_list[i]:
                continue
            else:
                lengths.append(length)
                length = 1
            
        
        lengths.append(length)

        return max(lengths)


        