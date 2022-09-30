class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int st=0;
        int en=nums.size()-1;
        while(st<=en)
        {
            int mid=(st+en)/2;
            int diff=nums[mid]-target;
            if(diff==0)
            {
                return mid;
            }
            else if(diff>0)
            {
                en--;
            }
            else st++;
        }
        return st;
    }
};