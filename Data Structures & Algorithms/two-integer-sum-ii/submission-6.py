class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in numbers:
                return [i+1,numbers.index(complement)+1]
        