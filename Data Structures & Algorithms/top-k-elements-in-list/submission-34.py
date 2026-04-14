class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = count.get(n, 0) + 1  # key:value -> value:count
        
        for n in count:
            freq[count[n]].append(n)
        
        li = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                li.append(n)
            if len(li) == k:
                return li

        