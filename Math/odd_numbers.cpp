/*
                         LeetCode 1523 (Easy)
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
*/

#include<iostream>
int main()
{
    int low, high;
    std :: cout<<"Enter Low and High\n";
    std :: cin >> low >> high;
    std :: cout << "Odd Numbers between " << low << " and " << high << " is " << ((high+1) / 2) - (low/2);
    return 0;
}

/*
Approach - odd nos between low and high is = total odd nos from 1 to high - odd nos from 1 to low

Odd nos from 1 to high = (high + 1) / 2
Odd nos from 1 to low (low excluded) = low / 2

Odd nos = ((high + 1) / 2) - (low/2)
        
*/