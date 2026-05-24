class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> duplicates = new HashMap<>();
        for(int i=0; i<nums.length;i++){
            if(duplicates.get(nums[i])!=null){
                return true;
            }
            duplicates.put(nums[i],1);
        }
        return false;
    }
}
