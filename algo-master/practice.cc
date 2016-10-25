#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iterator>
#include <cstdio>

int numberof_moves = 0;
int k;

int solve(int count, char source, char destination, char intermediate) {
  std::cout << k;
  if (count == 1)
  {
    for (int i = 0; i < k; ++i)
    {
        numberof_moves++;
        printf("Move top disc from pole %c to pole %c\n", source, destination);
      /* code */
    }
  }
  else {
    solve(count-k, source, intermediate, destination);
    solve(1, source, destination, intermediate);
    solve(count-k, intermediate, destination, source);
  }
}
int main() {
  int plates;
  int kk;
  std::cin >> kk;
  k = kk;
  std::cin >> plates;
  solve(plates, 'A', 'C', 'B'); // try larger value for the first parameter
  std::cout << "number of moves is " << numberof_moves << '\n';
  return 0;
} // return 0;