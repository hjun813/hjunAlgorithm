#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int test = x;
    int hacade = 0;
    while(x>0){
        hacade += (x % 10);
        x /= 10;
    }
    if(test % hacade != 0){
        answer = false;
    }
    return answer;
}