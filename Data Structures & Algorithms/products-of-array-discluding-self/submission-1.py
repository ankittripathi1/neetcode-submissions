class Solution:
    def get_prefix_product_arr(self, nums: List[int]) -> List[int]:
        arr = [] 
        arr.insert(0, 1)
        for i in range(1,len(nums)):
            arr.insert(i, nums[i-1] * arr[i-1])
        return arr

    def get_suffix_product_arr(self, nums: List[int]) -> List[int]:
        arr = [1] * (len(nums) - 1)
        arr.insert(len(nums) - 1, 1)
        for i in range(len(nums) - 2, -1, -1):
          arr[i] = nums[i+1] * arr[i+1]
        return arr

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        prefix_product_arr  = self.get_prefix_product_arr(nums)
        suffix_product_arr = self.get_suffix_product_arr(nums)
        for i in range(len(nums)):
            output[i] = prefix_product_arr[i] * suffix_product_arr[i]
        return output
