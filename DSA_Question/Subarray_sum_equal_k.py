class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_map={0:1}
        prefix_sum=[nums[0]]
        for i in  range(1,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[-1])
        for num in prefix_sum:
            if num-k in prefix_map:
                count+=prefix_map[num-k]
            prefix_map[num]=prefix_map.get(num,0)+1
        return count

        