#We simply loop through while keeping track of our max_reach, and if max_reach is 0 it means were stuck, if not then we can always keep going.This isnt really a dp problem.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        length = len(nums)-1
        for i in range(0, length):
            max_reach = max(max_reach-1, nums[i])
            if(max_reach == 0 and i != length):
                return False
            
        return True

        
