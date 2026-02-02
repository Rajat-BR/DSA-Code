//Leetcode 49. Group Anagrams [Medium]
/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
*/

#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

vector<vector<string>> groupanagrams(vector<string> str){
    unordered_map<string, vector<string>> mp;
    
    for(string s : str){
        string key = s;
        sort(key.begin(), key.end());
        mp[key].push_back(s);
    }

    vector<vector<string>> result;
    for(auto& pair: mp){
        result.push_back(pair.second);
    }

    
    return result;


}

int main(){
    vector<string> str;
    cout<<"Enter the strings"<<endl;
    string temp;
    while(cin >> temp && temp!= "hi"){
        str.push_back(temp);
    }

    vector<vector<string>> result = groupanagrams(str);

    cout << "[\n";
    for (auto& group : result) {
        cout << "  [ ";
        for (auto& word : group) {
            cout << word << " ";
        }
        cout << "]\n";
    }
        cout << "]";

    return 0;
}