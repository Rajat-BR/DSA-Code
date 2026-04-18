#include<iostream>
#include<vector>
using namespace std;

int main(){
    int drops = 0;
    vector<int> nums{3, 4, 5, 1, 2};
    for(int i = 0 ; i < nums.size() - 1; i++){
        if(nums[i] > nums[i+1]) drops++;
    }
    if(nums[nums.size()-1] > nums[0]) drops++;
    cout << (drops <= 1 ? "true" : "false");
    return 0;
}