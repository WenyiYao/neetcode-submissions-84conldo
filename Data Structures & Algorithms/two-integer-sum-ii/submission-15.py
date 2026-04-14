class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_i = 0
        right_i = len(numbers) - 1

        while left_i < right_i:
            value = numbers[left_i] + numbers[right_i]
            if value == target:
                return [left_i + 1, right_i + 1]
            
            elif value < target:
                left_i += 1

            elif value > target:
                right_i -= 1
        