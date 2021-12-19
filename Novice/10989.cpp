#include <iostream>
#include <algorithm>

using namespace std;

/*
처음에 이 문제를 quick sort로 계산했더니, 메모리 에러가 났다. 
counting sort로 풀면 풀린다라는 말이 있어서 그렇게 계산한다.
*/

int main(void){
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    cin >> n;

    int max = 10001;
    int count_array[max];

    fill_n(count_array,max,0); //0으로 배열 초기화

    // 숫자를 세기만 하는 배열
    for (int i = 0; i < n; i ++){
        int num;
        cin >> num;
        count_array[num] += 1;
    }

    int sum = 0;
    for (int i = 0; i < max; i++){
        for (int j = count_array[i]; j>0; j--){
            if (sum == n-1){cout << i;}
            else{cout << i << '\n';}
            sum ++;
        }
    }
}
