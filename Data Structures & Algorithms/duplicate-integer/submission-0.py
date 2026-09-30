class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#Need to loop through the array and check whether any specific number is repeated twice.
#Start from position 1, and check whether it equals any other position
#Repeat for all positions in the array
#If no repition then return false, otherwise return true

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False