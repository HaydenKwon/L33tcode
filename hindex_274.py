#Just sort and loop through until h_index < position, took roughly around 10 minutes need to gain more experience so I can hopefully solve these in 30 seconds to 5 minutes, I am just very lazy most times
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        for idx, i in enumerate(citations):
            if(i < idx + 1):
                return idx
        return idx+1
