#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(){

    stack<char> front_result;
    stack<char> end_result;
    string input_string;
    int num_of_operation;
    
    // operator라고 하니 오류가 났다. 이미 만들어진 명령어라서 그렇다고 한다.
    char operation; 
    
    cin >> input_string;
        
    // 초기 조건
    for (int i = 0; i < input_string.length(); i++){
        front_result.push(input_string[i]);
    }

    cin >> num_of_operation;

    for (num_of_operation; num_of_operation > 0; num_of_operation--) {

        cin >> operation;

        switch (operation){
            // 커서를 왼쪽으로 한 칸 옮김 (커서가 맨 앞이면 무시됨)
            case 'L':
                if (front_result.size() != 0){
                    end_result.push(front_result.top());
                    front_result.pop();
                }
                break;

            // 커서를 오른쪽으로 한 칸 옮김 (커서가 맨 뒤면 무시됨)
            case 'D':
                if (end_result.size() != 0){
                    front_result.push(end_result.top());
                    end_result.pop();
                }
                break;
            // 커서 왼쪽에 있는 문자를 삭제함
            case 'B':
                if (front_result.size() != 0){
                    front_result.pop();
                }
                break;

            // 커서 왼쪽에 문자를 더함
            case 'P':
                char new_char;
                cin >> new_char;
                front_result.push(new_char);
                break;
        }
    }

    while (!front_result.empty()){
        end_result.push(front_result.top());
        front_result.pop();
    }

    while (!end_result.empty()) {
        cout << end_result.top();
        end_result.pop();        
    }
    return 0;
    
    
}