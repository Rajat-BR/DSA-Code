/*
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

 

Example 1:

Input: n = 31

Output: 3

Explanation:

The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.

*/

#include<iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int last, largest = 0, sec_largest = 0, product;
    while(n > 0)
    {
        last = n % 10;

        if(last > largest){
            sec_largest = largest;
            largest = last ;}
        else if(last <= largest)
            sec_largest = max(sec_largest, last);
        product = largest * sec_largest;
        n /= 10;
    }

    cout << product;
    return 0;

}