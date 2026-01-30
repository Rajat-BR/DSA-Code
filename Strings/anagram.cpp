// Leetcode 242 Valid Anagram 
/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
*/

#include<iostream>
#include<string>

bool isAnagram(std :: string s, std :: string t) {

    if(s.length() != t.length()) // if both strings are not equal in length -> return false
        return false;

    int i;
    int arr[26] = {0};

    for(i = 0; i < s.length(); i++)
    {
        arr[s[i] - 'a']++;
    }
    
    for(i = 0; i < s.length(); i++)
    {
        arr[t[i] - 'a']--;
        
        if(arr[t[i] - 'a'] < 0) // if frequency is negative then return false.
            return false;
    }

    /*  for(i = 0; i < 26; i++).           3rd pass to check.
        {
            if(arr[i] != 0)
                return false;
        }
    */

    return true;
}

int main(){
    std::string s, t;
    std::cout<<"Enter two strings s and t"<<std::endl;
    std::getline(std::cin, s);
    std::getline(std::cin, t);
    std::cout<<isAnagram(s, t);
    return 0;
}