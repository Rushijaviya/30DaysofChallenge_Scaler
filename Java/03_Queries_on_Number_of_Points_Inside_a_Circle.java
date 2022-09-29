/*
 * 1828. Queries on Number of Points Inside a Circle
 * https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
 */

class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int n = queries.length, temp, xd, yd;
        int ans[] = new int[n];
        double dis;
        for (int i = 0; i < n; i++) {
            temp = 0;
            for (int j = 0; j < points.length; j++) {
                xd = queries[i][0] - points[j][0];
                yd = queries[i][1] - points[j][1];
                dis = Math.sqrt(xd * xd + yd * yd);
                if (dis <= queries[i][2]) {
                    temp++;
                }
            }
            ans[i] = temp;
        }
        return ans;
    }
}


/*another way of solving*/
class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] answer = new int[queries.length];
        int i=0;
        for(int ansquery[]: queries){
            int a=ansquery[0];
            int b=ansquery[1];
            int r=ansquery[2];
            int sum=0;
            for(int[] p:points){
                int x1=p[0];
                int y1=p[1];
                if(r * r>= (a-x1)*(a-x1) + (b-y1)*(b-y1)){
                    sum++;
                }
            }
            answer[i++] = sum;
            
        }
        return answer;
        
    }
}
