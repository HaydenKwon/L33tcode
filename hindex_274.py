#Just sort and loop through until h_index < position
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
