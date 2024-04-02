# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])

# Faster solution using rsplit so you only need to grab one item instead of multiples
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit(None,1)[-1])