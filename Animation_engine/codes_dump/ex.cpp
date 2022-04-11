#include<array> 
#include<vector> 
#include<iostream>
using namespace std; 

int main () { 
    array<int,5> Harrison {1,2,3,4,8};
    cout << Harrison.max_size() << endl; 
    cout << Harrison.data() << endl; 

    vector<int> Harry; 
    return 0; 
}