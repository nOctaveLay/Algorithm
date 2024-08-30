#include <iostream>

using namespace std;

int main() {
    string input_num;
    long long result = 0;
    cin >> input_num;
    for (int i=0;i<input_num.length();i++){
        string temp = "";
        result += stol(input_num);
        for (int i=1; i<input_num.length(); i++){
            temp += input_num[i];
        }
        temp += input_num[0];
        input_num = temp;
    }
    cout << result;
}