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

char printtrig(int n){
  if(n==1){
    cout << "*" << '\n';
  }
  else{
    printtrig(n-1);
    for (int i = 0; i < n; ++i)
    {
      cout << '*' ;
      /* code */
    }
    cout << '\n';
  }
}
int main (){
  
  int n;
  std::vector<int> pricess_vector;

  // prompt
  std::cin >> n;

  char r = printtrig(n);

  int p;
  for (int i = 0; i < n; ++i)
  {
    /* code */
    std::cin >> p;
    pricess_vector.push_back(p);
  }

  int result = mulReccursive(n);
  
  cout << "result is : " << result << '\n';
  return 0;
}
 