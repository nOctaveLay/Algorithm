#include <iostream>
#include <queue>
#include <list>

using namespace std;

int main(){

	// 큐 생성
	queue<int> q;
    list<int> result;
    int n,k;
    cin >> n >> k;


	// push
    for (int i = 1; i<n+1; i++){
        q.push(i);
    }

    while (!q.empty()) {
        for (int i = 0; i < k-1; i++){
            q.push(q.front());
            q.pop();
        }
        result.push_back(q.front());
        q.pop();
    }

    list<int>::iterator iter;
    cout << '<';
    iter = result.begin();
    while (result.size()>1){
        cout << *iter << ", ";
        result.erase(iter);
        iter = result.begin();
    }
    cout << *iter << '>';
	return 0;

}