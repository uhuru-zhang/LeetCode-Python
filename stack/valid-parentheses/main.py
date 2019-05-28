"""
https://leetcode-cn.com/problems/valid-parentheses/submissions/
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true
"""
class Solution:
    def isValid(self, s):
        # lst = [ '(', ')', '{', '}', '[', ']']
        L = []
        if not s: return True

        for i in s:
            if i == "(": L.append(i)
            if i == "{": L.append(i)
            if i == "[": L.append(i)

            if len(L) == 0: return False

            if i == ")" and L.pop() != "(": return False
            if i == "}" and L.pop() != "{": return False
            if i == "]" and L.pop() != "[": return False

        return False if L else True
