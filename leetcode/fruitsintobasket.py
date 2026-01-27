class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left,right = 0,0
        n = len(fruits)
        maxLen = 0
        mpp = {}
        while(right<n):
            if(fruits[right] in mpp):
                mpp[fruits[right]]+=1
            else:
                mpp[fruits[right]] = 1
            #shrink
            while(len(mpp)>2):
                mpp[fruits[left]]-=1
                if(mpp[fruits[left]] == 0):
                    del mpp[fruits[left]]
                left+=1
            maxLen = max(maxLen,right-left+1)
            right+=1
        return maxLen
