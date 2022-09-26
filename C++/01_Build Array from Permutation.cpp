# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans;
        
        for(auto &val : nums)
            ans.push_back(nums[val]);
        
        return ans;
    }
};
