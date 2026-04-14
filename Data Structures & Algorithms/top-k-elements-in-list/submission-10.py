class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        nums = sorted(nums)
        for num in nums:
            hashmap[num] += 1

        return heapq.nlargest(k,hashmap,key=hashmap.get)