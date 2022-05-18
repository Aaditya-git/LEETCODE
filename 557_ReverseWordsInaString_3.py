'''
Code Link : https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''

'''
Problem Statement :

Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # to store splitted and reversed words from sentence
        words = []
        # for each word in string.split() e.g.:- ["lets", "Leetcode", "crack","it"]
        for i in s.split():
            #reverse each word and store it in the "words" array.
            words.append(i[::-1])

        # this formatting is used to add double quotes to final answer as
        # it was required in output condition.
        # join the spliited and reversed words in words array using ' '.join method.
        b="{}".format(' '.join(words))
        return b
