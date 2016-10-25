#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int mulReccursive(int y){
  if(y == 1){
    return 1;
  }
  return y * mulReccursive(y-1);
}

int main (){
  
  int n;

  // prompt
  std::cin >> n;

  int result = mulReccursive(n);
  
  cout << "result is : " << result << '\n';
  return 0;
}
 