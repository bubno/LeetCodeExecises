from typing import List


class Solution:
    params = {'nums': [1, 2, 3, 4, 5], 'val': 2}

    def removeElement(self, nums: List[int], val: int) -> int:

        idx = 0

        while idx < len(nums):

            if nums[idx] == val:
                del (nums[idx])
            else:
                idx += 1

        return nums

    def removeElementOptimal(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                # partition
                nums[k] = nums[i]
                k += 1
        return nums


sol = Solution()
print(sol.removeElement(**sol.params))
