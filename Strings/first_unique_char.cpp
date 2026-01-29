// Leetcode 387 Easy
/*
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
*/

#include<iostream>
#include<string>

int firstUniqChar(std::string s){
    int i, j;
    int arr[26] = {0};
    for(i = 0; i<s.length();i++){
        arr[s[i] - 'a']++;
    }
    for(j = 0 ; j < s.length() ; j++){
        if(arr[s[j] - 'a'] == 1){
            return j;
        }
    }
    return -1;
}

int main(){
    std::string s;
    std::cout << "Enter the string" << std::endl;
    std::getline(std::cin, s);
    std::cout << "Index = " << firstUniqChar(s);
    return 0;
}
