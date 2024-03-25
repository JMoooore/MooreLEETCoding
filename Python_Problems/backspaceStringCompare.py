class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Iterate from front to back
        i, j = len(s) - 1, len(t) - 1
        iteration = 1
        while (i >= 0 and j >= 0):
            print()
            print(iteration)
            print('s and i')
            print(i)
            print(s[i])
            print('t and j')
            print(j)
            print(t[j])
            backspace1, backspace2 = 0, 0

            while (s[i] == '#' or backspace1 > 0) and i >= 0:
                if s[i] == '#':
                    backspace1 += 2
                backspace1 -= 1
                i -= 1

            while (t[j] == '#' or backspace2 > 0) and j >= 0:
                if t[j] == '#':
                    backspace2 += 2
                backspace2 -= 1
                j -= 1

            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1
            iteration += 1

        return True



if __name__ == '__main__':
    test = Solution()

    print(test.backspaceCompare("ab#c", "ad#c"))
    print(test.backspaceCompare("ab##", "c#d#"))
    print(test.backspaceCompare("ab#c", "ad#c"))
