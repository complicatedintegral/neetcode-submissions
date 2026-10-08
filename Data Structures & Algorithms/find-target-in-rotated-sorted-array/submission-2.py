class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(arr, i, j, target):

            while i <= j:

                middle = (i+j) // 2

                if arr[middle] == target:
                    return middle

                elif arr[middle] > target:
                    j = middle - 1

                else:
                    i = middle + 1

            return -1
        
        def findPivot(arr, i, j):

            while i <= j:

                if nums[i] <= nums[j]:
                    return i

                middle = (i+j) // 2

                if nums[middle] > nums[j]:
                    i = middle + 1
                else: 
                    j = middle

            return i

        p = findPivot(nums, 0, len(nums)-1)

        if target == nums[p]:
            return p

        if p == 0:
            return binarySearch(nums, 0, len(nums)-1, target)

        if nums[0] <= target: # if first element is lesser, target should be within the lower pivot range
            return binarySearch(nums, 0, p-1, target)

        return binarySearch(nums, p+1, len(nums)-1, target)
