class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "cadbzabcd"
        n = len(s)
        left,right = 0,0
        mpp = {}#sc:-0(N)
        maxLen = 0
        while(right<n): #tc:-0(N)
            #shrink a
            if(s[right] in mpp and mpp[s[right]]>=left):
                left = mpp[s[right]]+1
            maxLen = max(maxLen,right-left+1)
            mpp[s[right]] = right
            right+=1
        return maxLen    
