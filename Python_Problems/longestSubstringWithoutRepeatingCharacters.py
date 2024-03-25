# would be better to use dictionary

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l, r = 0, 0
        chars = set()

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                maxLength = max(maxLength, len(chars))
                r += 1
            elif s[r] in chars:
                    while s[r] in chars and l != r:
                        chars.remove(s[l])
                        l += 1
                    # r -= 1
            # r += 1


if __name__ == '__main__':
    dog = Solution()
    dog.lengthOfLongestSubstring("anviaj")