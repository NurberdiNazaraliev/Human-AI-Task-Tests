def task1ai(nums, target):
  num_map = {}
  for i, num in enumerate(nums):
    complement_as_first = target + num
    if complement_as_first in num_map:
      return [num_map[complement_as_first], i]
    complement_as_second = num - target
    if complement_as_second in num_map:
      return [i, num_map[complement_as_second]]
    num_map[num] = i
