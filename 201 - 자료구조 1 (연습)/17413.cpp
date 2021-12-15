#include <iostream>
#include <stack>
#include <string>

using namespace std;

void print_stack(stack <char>&input_stack){
    while (!input_stack.empty()){
        cout << input_stack.top();
        input_stack.pop();
    }
}

int main(){

    string input_string;

    getline(cin,input_string);
    stack<char> temp;
    bool check = 0;

    for (char ch : input_string){
        if (ch == '<'){
            print_stack(temp);
            check = 1;
            cout << ch;
        }
        else if (check == 1) {
                if (ch == '>'){
                    check = 0;
                }
                cout << ch;
            }

        else if (ch == ' '){
            print_stack(temp);
            cout << ch;
        }

        else{
            temp.push(ch);
        }
    }
    print_stack(temp);
    return 0;
}