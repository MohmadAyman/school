#include <iostream>
#include <algorithm>    // std::is_sorted, std::prev_permutation
#include <deque>
#include <vector>


std::deque<int> station;
std::vector<int> src;
int numberofcarots;

int solve_stack(std::vector<int> dst){
    int j = 0;

  for (int i = 1; i < numberofcarots+1; ++i)
    {
      src.push_back(i);
    }

  station.push_back(src.front());
  src.erase(src.begin());

  while(!src.empty()){
    while(!station.empty() && station.back() == dst[j]){
      station.pop_back();
      j++;
    }
    station.push_back(src.front());
    src.erase(src.begin());
  }

  while(!station.empty()){
    if(station.back() == dst[j]){
      station.pop_back();
      j++;
    }else{
      station.clear();
      src.clear();
      return 0;
    }
  }

  if(src.empty() && station.empty()){
    station.clear();
    src.clear();
    return 1;
  }

   station.clear();
   src.clear();
}

int main (){
  std::vector<int> dst;
  int order;
  bool carotsChanged = false;
  
  std::cin >> numberofcarots;

  while(numberofcarots!=0){
    if(carotsChanged){
      std::cin >> numberofcarots;
       if(numberofcarots==0){
          break;
       }
       carotsChanged = false;
  }

    for (int i = 0; i < numberofcarots; ++i)
      {
              std::cin >> order;
              if(order==0){
                carotsChanged = true;
                break;
              }
              dst.push_back(order);
      }
      if(!carotsChanged){
        if(solve_stack(dst)){
          std::cout << "Yes" << '\n';
        }else{
         std::cout << "No" << '\n';
        }
    }else{
        std::cout << '\n';
    }

      dst.clear();
    }
  return 0;
}
 