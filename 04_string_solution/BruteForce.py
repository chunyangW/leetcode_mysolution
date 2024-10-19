
# 暴力搜索
class Solution(object):
    def BruteForce(self, s: str, p: str) -> int:
        m = len(s)
        n = len(p)
        i, j = 0, 0
        while i < m and j < n: # i, j 到了某一个位置后停止搜索
            if s[i] == p[j]:
                i += 1
                j += 1
            else:
                # 从头开始遍历
                i = i - j + 1
                j = 0
        if j == n:
            return i - j
        else:
            return -1

test = Solution()
print(test.BruteForce("abcdefg", "a"))