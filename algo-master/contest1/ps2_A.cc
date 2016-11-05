#include <iostream>
#include <vector>

using namespace std;

std::vector<string> src;

int main (){
  string s;
  int value = 0;
  int numberoflines;
  std::cin >> numberoflines;
  for (int i = 0; i < numberoflines; ++i)
  {
    cin>>s;
    src.push_back(s);
  }
  for (int i = 0; i < src.size(); ++i)
  {
    if(src[i]=="++X" ||src[i]=="X++")
      value++;
    else
      value--;
  }
  cout <<  value<<endl;
  return 0;
}
 