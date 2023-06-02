def find_duplicate(nums):
    if len(nums) <= 1 or isinstance(nums, str):
        return False

    num_set = set()
    for num in nums:
        if isinstance(num, str) or num < 0:
            return False
        if num in num_set:
            return num
        num_set.add(num)

    return False
