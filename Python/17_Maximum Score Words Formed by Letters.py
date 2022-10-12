# 1255. Maximum Score Words Formed by Letters
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        words_score=[sum (score[ord(char)-97] for char in word) for word in words]
        words_counter=[Counter(word) for word in words]
        length=len(words)
        self.ans=0

        def dfs(idx,curr_score,counter):
            if curr_score+sum(words_score[idx:])<=self.ans:
                return 
            self.ans=max(self.ans,curr_score)
            if idx==length:
                return
            if all(count<=counter.get(char,0) for char,count in words_counter[idx].items()):
                dfs(idx+1,curr_score+words_score[idx],counter-words_counter[idx])
            dfs(idx+1,curr_score,counter)
        
        dfs(0,0,Counter(letters))
        return self.ans