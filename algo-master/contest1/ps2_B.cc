#include <iostream>
#include <vector>

using namespace std;

std::vector<long> src;
std::vector<unsigned long long> dst;
std::vector<int> result;

unsigned long long int max_max(unsigned long long int i, unsigned long long int j){
  if(i>j)
    return i;
  return j;
}
void solve(int number, std::vector<long> src, int array_size){
  unsigned long long int v = 0;
    cout << endl;
    dst[0] = 0;
    dst[1] = src[0];
    int j = 2;
    for (int i = 1; i < src.size(); ++i)
    {
      cout << src[i]+dst[j-2];
      dst[j] = max_max(src[i]+dst[j-2],dst[j-1]);
      j++;
    }
  unsigned long long vu = -1;
    for (int i = dst.size()-1; i > 0;)
    {
      if(dst[i]!=vu){
          while(dst[i-1]==dst[i])
          {
            i -=1;  
          }
           result.push_back(i);
           vu = dst[i];
           i = i-2;
        }
    }
    for (int i = 0; i < result.size(); ++i)
    {
      v+=src[result[i]-1];
    }
    cout << "Case " << number<< ": "<< v << endl;
    result.clear();
    dst.clear();
    src.clear();
}

int main (){
  string s;
  long value;
  int numberoftests;
  int array_size;
  std::cin >> numberoftests;
  for (int i = 0; i < numberoftests; ++i)
  {
    cin>>array_size;
    for (int i = 0; i < array_size; ++i)
    {
        cin>>value;
        src.push_back(value);
    }
    src.resize(array_size);
    dst.resize(array_size+1);
    solve(i+1 ,src, array_size);
    src.clear();
  }
  return 0;
}