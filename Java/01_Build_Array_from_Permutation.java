/*
 * 1920. Build Array from Permutation
 * link: https://leetcode.com/problems/build-array-from-permutation/
 */

//approach 1 TC: O(n) SC: O(n)

class Solution {
    public int[] buildArray(int[] nums) {
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            ans[i] = nums[nums[i]];
        }
        return ans;
    }
}

//approach 2 TC: O(n) SC: O(1)

class Solution2 {
    public int[] buildArray(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            nums[i] = (nums[nums[i]] % n) * n + nums[i]; // (new value)*n + (old value)
        }
        for (int i = 0; i < n; i++) {
            nums[i] /= n;
        }
        return nums;
    }
}


//approach 3 TC: O(n) SC: O(n) :
class Solution3 {
    public int[] buildArray(int[] nums) {
        return Arrays.stream(nums).map(i -> nums[i]).toArray();
    }
}

