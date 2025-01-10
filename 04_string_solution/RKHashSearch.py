'''
 使用滚动哈希匹配的方法
 滚动哈希是在前面子串的基础上，减去最左边的，然后加上右边的，时间复杂度是O（1）
 同时哈希值是通过类似二进制的方法，26^n * ord(s[n]) 
 取模是为了不会太大
'''
def RabinKarp(pattern, text, base=256, mod=101):
    if len(pattern) > len(text):
        return -1

    # 计算模式串的哈希值
    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod

    # 计算第一个子文本串的哈希值
    text_hash = 0
    for i in range(len(pattern)):
        text_hash = (text_hash * base + ord(text[i])) % mod

    # 后面要减去最高位的权值
    pattern_hash_base = pow(base, len(pattern) - 1) % mod

    # 遍历文本串，比较哈希值
    for i in range(len(text) - len(pattern) + 1):
        if text_hash == pattern_hash:
            # 如果哈希值相同，进一步比较字符串
            is_match = True
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    is_match = False
                    break
            if is_match:
                return i  # 返回匹配的起始位置

        # 更新文本串的哈希值
        if i < len(text) - len(pattern):
            text_hash = (text_hash - ord(text[i]) * pattern_hash_base) % mod
            text_hash = (text_hash * base + ord(text[i + len(pattern)])) % mod

    return -1  # 如果没有找到匹配，返回-1

# 使用RK哈希算法
pattern = "B"
text = "ABCDABD"
base = 256  # 假设字符集大小为256
mod = 101  # 选择一个质数作为模数

# 调用函数
index = RabinKarp(pattern, text, base, mod)
if index != -1:
    print(f"Pattern found at index {index}")
else:
    print("Pattern not found")