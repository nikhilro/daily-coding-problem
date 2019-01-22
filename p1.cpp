#include <iostream>
#include <vector>
using namespace std;

bool two_sum (vector<int> arr, int sum) {
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 1; j < arr.size(); j++) {
            if (sum == arr[i] + arr[j]) return true;
        };
    };
    return false;
};

int main (int argc, char** argv) {
    vector<int> arr = {10, 15, 3, 7};
    int sum = 17;
    cout << two_sum(arr, sum) << endl;
    return 0;
}