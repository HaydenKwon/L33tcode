#Fill dp array while checking if each word in the dictionary matches and if it does then checks if the dp slot of length that word away is true, proof by induction
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]* (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in wordDict:
                if(i-len(j) >= 0):
                    if(s[i-len(j):i] == j and dp[i-len(j)] == True):
                        dp[i] = True

        return dp[len(s)]     
