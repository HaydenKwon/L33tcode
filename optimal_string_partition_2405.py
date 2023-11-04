#I think this is simple since if you start from the first character u have to make a split whenever the first duplicate comes up then you can just repeat that process recursively since its the same problem

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_set = {""}
        substrings = []
        current_string = ""
        for i in s:
            if i in current_set:
                substrings.append(current_string)
                current_string = i 
                current_set = {i}
            else:
                current_string += i
                current_set.add(i)
        #this last part could be a little cleaner
        if current_string != "":
            substrings.append(current_string)
        return len(substrings)
