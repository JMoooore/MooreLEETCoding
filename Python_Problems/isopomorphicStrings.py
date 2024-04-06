class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mipMap = {}
        mopMip = set()

        if len(s) != len(t):
            return False

        for i, val in enumerate(s):
            if val not in mipMap and t[i] not in mopMip:
                mipMap[val] = t[i]
                mopMip.add(t[i])
            elif val not in mipMap or mipMap[val] != t[i]:
                return False

        return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))
