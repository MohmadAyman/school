#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>


int main (){
  
  int n;
  std::vector<std::vector<int> > pricess_vector;

  // prompt
  std::cout << "Input test cases: ";
  std::cin >> n;

  for (int ii = 0; ii < n; ++ii)
  {
  /* code */
    int m, c, k, p;
    std::cin >> m;
    std::cin >> c;
    int i =0;

    for (i = 0; i < c; ++i)
    {
      std::cin >> k;
      for (int j = 0; j < k; ++j)
      {
        std::cin >> p;
        pricess_vector[i].push_back(p);
        /* code */
      }
      std::sort (pricess_vector[i].begin(), pricess_vector[i].end());
      std::reverse (pricess_vector[i].begin(), pricess_vector[i].end());
      /* code */
    }
    int sum = 0;
    for (int o = 0; o < c; ++o)
    {
      std::vector<int>::iterator it = pricess_vector[o].begin(); //minimum price
      sum = sum + *it;
      std::cout << sum;
      std::cout << *it;
      /* code */
    }
    if(sum>m){
        std::cout << "no solution";
      }else{
        std::cout << "solution";
      }

  }

  

  
  
  
  return 0;
}
 