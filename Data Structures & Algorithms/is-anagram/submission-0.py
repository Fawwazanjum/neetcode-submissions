from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#For each distinct letter in s, we need to count the number of times it occurs in s and the number of times it occurs in t. If they are equal then return True, else return False
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
    