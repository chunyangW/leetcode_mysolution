**str是无法修改长度与内容的需要先转换为列表，最后再拼接起来**

在Python中，`str` 类型是用于表示文本数据的。它提供了大量的方法来进行各种操作。以下是一些常用的 `str` 类型操作：

1. **访问字符**：

   - `s[i]`：获取字符串 `s` 中索引为 `i` 的字符。
   - `s[start:end]`：获取从索引 `start` 到 `end`（不包括 `end`）的子字符串。
2. **字符串连接**：

   - `s1 + s2`：将两个字符串 `s1` 和 `s2` 连接起来。
3. **字符串重复**：

   - `s * n` 或 `n * s`：将字符串 `s` 重复 `n` 次。
4. **大小写转换**：

   - `s.upper()`：将字符串 `s` 中的所有小写字母转换为大写。
   - `s.lower()`：将字符串 `s` 中的所有大写字母转换为小写。
   - `s.capitalize()`：将字符串 `s` 的首字母转换为大写，其余字母转换为小写。
   - `s.title()`：将字符串 `s` 中的每个单词的首字母转换为大写。
5. **去除空白**：

   - `s.strip()`：去除字符串 `s` 两端的空白字符（包括空格、换行符等）。
   - `s.lstrip()`：去除字符串 `s` 左侧的空白字符。
   - `s.rstrip()`：去除字符串 `s` 右侧的空白字符。
6. **查找和替换**：

   - `s.find(sub)`：查找子字符串 `sub` 在 `s` 中的索引，如果未找到则返回 `-1`。
   - `s.index(sub)`：查找子字符串 `sub` 在 `s` 中的索引，如果未找到则抛出 `ValueError`。
   - `s.replace(old, new)`：将字符串 `s` 中所有出现的子字符串 `old` 替换为 `new`。
7. **长度和成员关系测试**：

   - `len(s)`：返回字符串 `s` 的长度。
   - `sub in s`：检查子字符串 `sub` 是否是 `s` 的子串。
8. **字符串分割**：

   - `s.split(sep=None)`：按照分隔符 `sep` 将字符串 `s` 分割成子字符串列表，默认分隔符为空格。
   - `s.splitlines()`：按照行分隔符将字符串 `s` 分割成行的列表。
9. **字符串连接**（使用 `join` 方法）：

   - `sep.join(iterable)`：将 `iterable` 中的元素以 `sep` 作为分隔符连接起来。
10. **格式化**：

    - `s.format(*args, **kwargs)`：使用 `str.format()` 方法格式化字符串。
    - 使用 f-string（Python 3.6+）：例如 `f"Hello, {name}!"`。
11. **编码和解码**：

    - `s.encode(encoding='utf-8')`：将字符串 `s` 编码为指定编码的字节串，默认编码为 `'utf-8'`。
    - `bytes.decode(encoding='utf-8')`：将字节串解码为字符串，默认编码为 `'utf-8'`。
12. **检查字符串内容**：

    - `s.isdigit()`：检查字符串 `s` 是否只包含数字。
    - `s.isalpha()`：检查字符串 `s` 是否只包含字母。
    - `s.isspace()`：检查字符串 `s` 是否只包含空白字符。
    - `s.islower()`：检查字符串 `s` 是否只包含小写字母。
    - `s.isupper()`：检查字符串 `s` 是否只包含大写字母。

这些是 `str` 类型的一些主要操作，Python 的字符串非常灵活且功能强大，还有许多其他方法和操作可以用于处理文本数据。
