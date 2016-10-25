// #include <iostream>
// #include <string>
// #include <vector>
// #include <algorithm>
// #include <set>

// std::vector<std::string> first;
// std::vector<std::string>::iterator it;
// std::set<std::string> second;
// std::vector<std::string> Gs;
// std::vector<std::string> Ts;

// void RecPermute(std::string soFar, std::string rest){
// 	if(rest ==""){
// 		first.push_back(soFar);
// 		Ts.push_back(soFar);
// 		Gs.push_back(soFar);
// 	}else{
// 		for (int i = 0; i < rest.length(); ++i)
// 		{
// 			std::string next = soFar + rest[i];
// 			if (second.find(next)!=second.end())
// 			{
// 			}else{
// 				std::string remain = rest.substr(0,i)+rest.substr(i+1);
// 				second.insert(next);
// 				RecPermute(next,remain);
// 			}
// 		}
// 	}
// }

// int main(){
// 	int m,g,k,s;
// 	char space;
// 	std::cin >> m;
// 	std::string s1, s2,s3;
// 	std::string Cs;
	
// 	for (int i = 0; i < m; ++i)
// 	{
//         std::cin >> g;
//         std::cin >> k;
// 	  getline(std::cin, s3);
// 	  getline(std::cin, s2);
// 		  for (int i = 0; i < k; ++i)
// 		  {
// 		  	Cs+='C';
// 		  }
// 	for (int i = 0; i < g-k; ++i)
// 	{
// 		s1+=s2[i];
// 	}

// 	  RecPermute("",s1+Cs);
// 		second.clear();

// 	 s = first.size();
// 	 std::cout << s*3+1 << '\n' << s2 << '\n';

// 	for (int i =0; i<Gs.size();i++)
// 	{
// 		std::replace( Gs[i].begin(), Gs[i].end(), 'C', 'G'); // replace all 'x' to 'y'
// 		std::replace( Ts[i].begin(), Ts[i].end(), 'C', 'T'); // replace all 'x' to 'y'
//     		std::cout << first[i] << '\n';
//     		std::cout << Gs[i] << '\n';
//     		std::cout << Ts[i] << '\n';
// 	}

// 	Gs.clear();
// 	Ts.clear();
// 	first.clear();
// 	s1 = "";
// 	}
// 	return 0;
// }



#include <stdio.h>
#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cstring>
using namespace std;

char buf[20];
int t, n, k, ans;
int K =2;
string input;
std::vector<string> s;
static char bases[] = { 'A', 'C', 'G', 'T' };
int b = 0;

void populate(int length, string base, string& in)
{
	// cout << in[length-1] << in[length-2];
    if(k>0)
    {
    	int i =0;
		if (in[length-1]=='A'){
			s[i].replace(length-1, 1, "C");
			s[i+1].replace(length-1, 1, "G");
			s[i+2].replace(length-1, 1, "T");
		}else if(in[length-1]=='C'){
			s[i].replace(length-1, 1, "A");
			s[i+1].replace(length-1, 1, "G");
			s[i+2].replace(length-1, 1, "T");
		}else if(in[length-1]=='G'){
			s[i].replace(length-1, 1, "A");
			s[i+1].replace(length-1, 1, "C");
			s[i+2].replace(length-1, 1, "T");
		}else if(in[length-1]=='T'){
			s[i].replace(length-1, 1, "A");
			s[i+1].replace(length-1, 1, "C");
			s[i+2].replace(length-1, 1, "G");
		}
    }
    if(k>1){ // k=2
    		for (int i = 0; i < s.size()-3;++i)
    		{
    			s[i+3] = s[i];
    		}

    		for (int i = 0; i < 3; ++i)
    		{
	    		if (in[length-2]=='A'){
				s[i].replace(length-2, 1, "C");
				s[i+3].replace(length-2, 1, "G");
				s[i+6].replace(length-2, 1, "T");
			}else if(in[length-2]=='C'){
				s[i].replace(length-2, 1, "A");
				s[i+3].replace(length-2, 1, "G");
				s[i+6].replace(length-2, 1, "T");
			}else if(in[length-2]=='G'){
				s[i].replace(length-2, 1, "A");
				s[i+3].replace(length-2, 1, "C");
				s[i+6].replace(length-2, 1, "T");
			}else if(in[length-2]=='T'){
				s[i].replace(length-2, 1, "A");
				s[i+3].replace(length-2, 1, "C");
				s[i+6].replace(length-2, 1, "G");
			}		
    		}
    }
    if(k>2){
   	    	for (int i = 0; i < s.size()-9;++i)
    		{
    			s[i+9] = s[i];
    		}
    		b = length-3;
    		for (int i = 0; i < 9; ++i) // to be fixed
    		{
	    		if (in[b]=='A'){
				s[i].replace(b, 1, "C");
				s[i+9].replace(b, 1, "G");
				s[i+18].replace(b, 1, "T");
			}else if(in[b]=='C'){
				s[i].replace(b, 1, "A");
				s[i+9].replace(b, 1, "G");
				s[i+18].replace(b, 1, "T");
			}else if(in[b]=='G'){
				s[i].replace(b, 1, "A");
				s[i+9].replace(b, 1, "C");
				s[i+18].replace(b, 1, "T");
			}else if(in[b]=='T'){
				s[i].replace(b, 1, "A");
				s[i+9].replace(b, 1, "C");
				s[i+18].replace(b, 1, "G");
			}		
    	}
    }
    if(k>3){
   	    	for (int i = 0; i < s.size()-27;++i)
    		{
    			s[i+27] = s[i];
    		}
    		b = length-4;
    		for (int i = 0; i < 27; ++i) // to be fixed
    		{
	    		if (in[b]=='A'){
				s[i].replace(b, 1, "C");
				s[i+27].replace(b, 1, "G");
				s[i+54].replace(b, 1, "T");
			}else if(in[b]=='C'){
				s[i].replace(b, 1, "A");
				s[i+27].replace(b, 1, "G");
				s[i+52].replace(b, 1, "T");
			}else if(in[b]=='G'){
				s[i].replace(b, 1, "A");
				s[i+27].replace(b, 1, "C");
				s[i+52].replace(b, 1, "T");
			}else if(in[b]=='T'){
				s[i].replace(b, 1, "A");
				s[i+27].replace(b, 1, "C");
				s[i+52].replace(b, 1, "G");
			}		
    	}
    }
    if(k>4){
   	    	for (int i = 0; i < s.size()-81;++i)
    		{
    			s[i+81] = s[i];
    		}
    		b = length-5;
    		for (int i = 0; i < 81; ++i) // to be fixed
    		{
	    		if (in[b]=='A'){
				s[i].replace(b, 1, "C");
				s[i+81].replace(b, 1, "G");
				s[i+162].replace(b, 1, "T");
			}else if(in[b]=='C'){
				s[i].replace(b, 1, "A");
				s[i+81].replace(b, 1, "G");
				s[i+162].replace(b, 1, "T");
			}else if(in[b]=='G'){
				s[i].replace(b, 1, "A");
				s[i+81].replace(b, 1, "C");
				s[i+162].replace(b, 1, "T");
			}else if(in[b]=='T'){
				s[i].replace(b, 1, "A");
				s[i+81].replace(b, 1, "C");
				s[i+162].replace(b, 1, "G");
			}		
    	}
    }
}

int main() {
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &n, &k);
		cin >> input;
		s.resize(pow(n,k+1));
		for(size_t i = 0; i < pow(n,k+1); ++i) 
		      s[i]=input;
		populate(input.size(), bases, input);
	}
	for (int i = 0; i < s.size(); ++i)
	{
		cout << s[i];
		cout << endl;
	}
	return 0;
}