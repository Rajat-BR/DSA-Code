/*
                                  LeetCode 69 (Easy
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
*/

#include<iostream>
int sqrtt(int x)
{
    int low = 0, high = x >> 1;
    while(low <= high)
    {
        long int mid = (low + high) >> 1;
        if((mid*mid) <= x and (mid+1)*(mid+1) > x)
            return mid;
        else if((mid*mid) < x)
            low = mid + 1;
        else
            high = mid - 1;
        return 1;
    }
}
int main()
{
    int x;
    std :: cout << "Sqrt = " << sqrtt(12);
    return 0;
}