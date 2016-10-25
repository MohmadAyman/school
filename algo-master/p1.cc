#include <iostream>
#include <string>

long hamming_distance(std::string& fs, std::string& ss){
    long hm_distance = 0;
    
    if((fs.length() == ss.length())){
      
      for(int i = 0; i < fs.length(); i++){
        if(!(fs[i] == ss[i])){
          hm_distance++;
        }
      }
      
    }else{
      hm_distance = -1;  
    }
    return hm_distance;
}

int main (){
  
  std::string s1, s2;
  long hm_distance;
  
  // prompt
  std::cout << "Input First String: ";
  getline(std::cin, s1);
  std::cout << "Input Second String: ";
  getline(std::cin, s2);
  
  hm_distance = hamming_distance(s1, s2); // get the value
  
  // check and display
  if(hm_distance %2 == 0){
    std::cout << "YES";
  }else{
    std::cout << "NO";
  }
  
  return 0;
}
 