//Leetcode 136 SINGLE NUMBER [Easy]
/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1


Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
*/

#include<iostream>
#include<vector>
using namespace std;

int singlenumber(vector<int> nums)
{
    int ans = 0;
    for(int i = 0; i < nums.size() ; i++){
        ans = ans ^ nums[i];
    }

    return ans;
}

int main(){
    vector<int> nums;
    int temp;
    cout<<"Enter the Array Values (enter 'q' to stop input)"<<endl;

    while(cin>>temp){
        nums.push_back(temp);
    }
    
    cout<<"Answer = "<<singlenumber(nums);
    return 0;
}