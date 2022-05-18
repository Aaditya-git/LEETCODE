'''
Code Link: https://leetcode.com/problems/valid-parentheses/
'''

'''
Problem Statement:

Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        openn = set('({[')
        matches = set([('(',')'), ('[',']' ), ('{','}')])


        stack = []

        for i in s:
            if i in openn:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False

                top = stack.pop()

                if (top,i) not in matches:
                    return False
        return len(stack)==0
