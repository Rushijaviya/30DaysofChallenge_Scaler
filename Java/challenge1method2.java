class Solution {
    public int[] buildArray(int[] nums) {
        return Arrays.stream(nums).map(i -> nums[i]).toArray();
    }
}
