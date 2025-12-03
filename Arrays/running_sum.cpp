#include<iostream>
int main()
{
    int nums[5] = {1, 2, 3, 4, 5};
    int n = sizeof(nums) / sizeof(nums[0]);
    int sum = 0;
    int ans[5];
    for(int i = 0; i < n; i++)
    {
        sum += nums[i];
        ans[i] = sum;
    }

    std::cout << "{ ";
    for(int i = 0; i < n; i++)
    {
        std::cout << ans[i];
        if (i < n - 1) {
            std::cout << ", ";
        }
    }
    std::cout << " }" << std::endl;
}