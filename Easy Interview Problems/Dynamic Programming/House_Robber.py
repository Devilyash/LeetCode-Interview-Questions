class Solution:
    def rob(self, nums: List[int]) -> int:
        
        even_sum = 0
        odd_sum = 0
        
        for i in range(len(nums)):
            if i%2 == 0:
                even_sum = max(even_sum + nums[i], odd_sum)
            else:
                odd_sum = max(odd_sum + nums[i], even_sum)
            # print('i: ',i,'nums[i]: ',nums[i],'even_sum: ',even_sum,'odd_sum: ',odd_sum)
                
        return max(even_sum, odd_sum)


obj = Solution()
print(obj.rob([2,1,1,2]))
