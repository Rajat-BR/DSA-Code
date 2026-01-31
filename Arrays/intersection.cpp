// Leetcode 349 Intersection of Two Arrays [Easy]
/*
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
*/

#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

vector<int> intersection(vector<int> nums1, vector<int> nums2){
    unordered_set<int> set1, set2;
    for(int x : nums1){
        set1.insert(x);
    }

    for(int x : nums2){
        if(set1.count(x)) set2.insert(x);
    }

    return vector<int>(set2.begin(), set2.end());
}

int main(){
    vector<int> nums1 , nums2;
    int temp, temp1;

    cout<<"Enter nums1 elements"<<endl;
    while(cin>>temp && temp != -1){
        nums1.push_back(temp);
    }

    cout<<"Enter nums2 elements"<<endl;
    while(cin>>temp1 && temp1 != -1){
        nums2.push_back(temp1);
    }
    
    vector<int> result = intersection(nums1, nums2);

    for(int x : result){
        cout<<x<<endl;
    }
    return 0;
}
