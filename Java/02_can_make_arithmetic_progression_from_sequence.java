/*
 * 1502. Build Array from Permutation
 * https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
 */


class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int dif=arr[1] - arr[0];
        for(int i=2; i<arr.length; ++i){
            if(arr[i]-arr[i-1] != dif){
                return false;
            }
        }
        return true;
    }
}
