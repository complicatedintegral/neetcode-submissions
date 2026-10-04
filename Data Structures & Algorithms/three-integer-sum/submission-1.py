class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = list()
        nums.sort()
        # print(nums)

        for i in range(len(nums)-2): # -2 because only numbers to the right are compared to form triplets
            if nums[i] > 0:
                break 
                
            if i > 0 and nums[i] == nums[i-1]: # checking for i duplication 
                continue

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]: # checking for j duplication, should be while instead of if
                        j += 1

                elif nums[j] + nums[k] < target:
                    j += 1

                else:
                    k -= 1

        # this approach is smooth but need to eliminate duplicates for i and j, cause answer does not allow duplicates and set approach doesn't work because lists cannot be added into sets, final solution will remove duplicates too
        return res
