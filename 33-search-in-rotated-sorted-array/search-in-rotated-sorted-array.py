class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pattern: sorted rotated array => binary search
        # --- find the pivot index
        # the pivot point is the greatest number in the array
        # if the pivot index of this.point is at the end, then we search the whole array

        # if the pivot point is somewhere in the middle, then we have to figure out if target is before the pivotpoint or after. if the pivot point is less than nums[0] then we know we need to be in the other half 

        def find_pivot_index():
            last_number = nums[0]
            idx = 0
            for i in range(1, len(nums)):
                if nums[i] > last_number:
                    idx = i
                    last_number = nums[i]   
            return idx
        idx = find_pivot_index()
        start, end = 0, len(nums) - 1
        if target < nums[0]:
            start = idx + 1
        else:
            end = idx
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
