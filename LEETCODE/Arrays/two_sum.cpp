#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;

int main(){
    vector<int> nums = {2, 3, 7, 8, 23, 12, 67, 54, 23};
    int target = 61;

    unordered_map<int, int> mp;
    for(int i = 0 ; i < nums.size(); i++){
        if(mp.find(target - nums[i]) == mp.end()){
            mp[nums[i]] = i;
        }
        else{
            cout << "(" << mp[target - nums[i]] << " , " << i << ")";
        }
    }

    return 0;

}