#include <iostream>
#include <string>

int main (){
  
  long number;
  long result;
  // prompt
  std::cout << "Input the number: ";
  std::cin >> number;
  
  result = 2*number - 9;
  
  
  std::cout << result;
  
  return 0;
}