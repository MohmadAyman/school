#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int sumReccursive(int y){
  if(y == 1){
    return 1;
  }
  return y + sumReccursive(y-1);
}

int main (){
  
  int n;

  // prompt
  std::cin >> n;

  int result = sumReccursive(n);
  
  cout << "result is : " << result << '\n';
  return 0;
}
 