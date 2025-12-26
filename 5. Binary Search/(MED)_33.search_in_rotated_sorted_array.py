class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Key intuition: at each step, 1 half is sorted and 1 is not

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # If left is sorted
            elif nums[left] <= nums[mid]:
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # If right is sorted
            elif nums[mid] <= nums[right]:
                if nums[mid] > target or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return -1

# December 26th, 2025