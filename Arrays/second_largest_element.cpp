//find the second largest element in an array
#include<iostream>
#include<climits>
using namespace std;

int main(){
    int arr[] = {1 ,34 , 43 , 45, 2, 45, 67, 76, 54, 34, 21, 69, 99, 23, 89, 76};
    int largest = INT_MIN, sec_largest = INT_MIN;
    int n = sizeof(arr)/sizeof(arr[0]);
    for(int i = 0 ; i < n ; i++){
        if(arr[i] > largest){
            sec_largest = largest;
            largest = arr[i];
        }
        else if(arr[i] > sec_largest and arr[i]!=largest){
            sec_largest = arr[i];
        }
    }

    if(sec_largest == INT_MIN){
        cout << "No Second Largest" << endl;
    }
    else cout << sec_largest;
    return 0;
}