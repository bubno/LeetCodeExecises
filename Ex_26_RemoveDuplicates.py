def removeDuplicates(nums) -> int:
    last_el = None
    idx = 0

    while idx < len(nums):

        if nums[idx] == last_el:
            del (nums[idx])
        else:
            last_el = nums[idx]
            idx += 1

    return len(nums)


removeDuplicates([1, 2, 2, 3, 4])
