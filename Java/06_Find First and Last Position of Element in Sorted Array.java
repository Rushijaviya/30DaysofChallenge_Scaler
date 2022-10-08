/*
 * 34. Find First and Last Position of Element in Sorted Array
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 */

class Solution {
  public int[] searchRange(int[] nums, int target) {
    int ans[] = {-1, -1};
    if (nums.length == 0) {
      return ans;
    }
    int start = 0, end = nums.length - 1, mid;
    while (start <= end) {
      mid = start + (end - start) / 2;
      if (target <= nums[mid]) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }
    if (start < nums.length && nums[start] == target) {
      ans[0] = start;
    }
    start = 0;
    end = nums.length - 1;
    while (start <= end) {
      mid = start + (end - start) / 2;
      if (target >= nums[mid]) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
    if (end >= 0 && nums[end] == target) {
      ans[1] = end;
    }
    return ans;
  }
}
