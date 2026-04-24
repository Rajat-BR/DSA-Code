//Given an array, find the maximum sum of subarrays of length k

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int> nums{1, 3, 2, 4, 6, 6, 7, 4, 7, 8, 2};

    int k = 2;
    int sum = 0;
    int n = nums.size();
    if(k > n) return -1;

    for(int i = 0 ; i < k; i++){
        sum += nums[i];
    }

    int maxSum = sum;

    for(int i = 1; i <= n - k; i++){
        sum = sum - nums[i-1] + nums[i+k-1];
        maxSum = max(sum, maxSum);
    }
    cout << maxSum;
    return 0;
}
