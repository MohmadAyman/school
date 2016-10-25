// Recursive backtracking
#include <stdio.h>
#include <iostream>
#include <set>
#include <vector>
#include <list>
#include <numeric>      // std::accumulate

std::vector<int> v;

std::set<int> output;
std::vector<int> input;
std::vector<int> temp;
std::vector<int>::iterator it;
std::list<int> soFar;
int t,n;
int sum =0;

void RecPermuteSub(std::list<int> soFar, std::vector<int> rest, int sum){
	if(rest.size()==0){
		// for (std::list<int>::iterator i = soFar.begin(); i != soFar.end(); ++i)
		// {
		// 	printf("%d", *i);			
		// }
		// printf("\n");
		// sum = 0;
		soFar.clear();
		// return;
	}
	// if(sum==t){
	// 	printf("sum equal t \n");
	// 	for (std::list<int>::iterator i = soFar.begin(); i != soFar.end(); ++i)
	// 	{
	// 		printf("%d +", *i);			
	// 	}
	// 	printf("\n");
	// 	soFar.clear();
	// 	sum = 0;
	// 	return ;
	// }else if(sum>t){
	// 	printf("sum > t  t \n");
	// 	sum = 0;
	// 	return ;
	// }
	else{
		// for (std::list<int>::iterator i = soFar.begin(); i != soFar.end(); ++i)
		// {
		// 	printf("%d ", *i);			
		// }
		// printf("\n");
			for (int i=0;i<rest.size();i++)
			{
				temp.clear();
				soFar.push_back(rest[i]);
				sum+=rest[i];
				temp.insert( temp.end(), rest.begin(), rest.end() );
				it = temp.begin();
				temp.erase(i+it);
				for (std::vector<int>::iterator i = temp.begin(); i != temp.end(); ++i)
				{
					printf("%d", *i);			
				}
				printf("\n");
				RecPermuteSub(soFar, temp, sum);
			}
	}
}

int main(){
    	while(std::cin>>t>>n){    		
    		if(t==0)
    		break;
		input.resize(n);
		soFar.resize(n);
		for(int i=0;i<n;i++){
			std::cin>>input[i];
		}
		output.clear();
		printf("Sums of %d\n",t );
		RecPermuteSub(soFar,input,0);
		if(output.size()==0)
			printf("NONE");
		temp.clear();
		input.clear();
		soFar.clear();
	}
	return 0;
}

// #include <iostream>
// #include <string>
// #include <vector>
// #include <iterator>
// #include <algorithm>
// #include <list>
// #include <stdio.h>
// using namespace std;

// std::vector<int>::iterator it;
// std::vector<int> input;

// int n,t;
// int sum =0;
// void permute(vector<int> list, int level, vector<vector<int> >& v, int sum){
//     if(level == list.size()){
//         v.push_back(list);
//         return;
//     }
//     for(int i=level;list[i];++i){
//         swap(list[level], list[i]);
//         permute(list, level + 1, v, sum);
//         swap(list[level], list[i]);
//     }
// }

// int main(){
//     int a;
//     vector<int> list;
//     vector<vector<int> > v;
//       	while(std::cin>>t>>n){    		
//     		if(t==0)
//     		break;
// 		input.resize(n);
// 		v.resize(2^n);
// 		for(int i=0;i<n;i++){
// 			std::cin>>input[i];
// 		}
// 		printf("Sums of %d\n",t);
// 		permute(input, 0, v, 0);
// 		for (int i = 0; i < v.size(); ++i)
// 		{
// 			// sum = 0;
// 			for (int j = 0; j < v[i].size(); ++j)
// 			{
// 				if(sum == t){
// 					for (int k = 0; k < j; ++k)
// 					{
// 						printf("%d +",v[i][k]);
// 					}
// 					printf("\n");
// 					break;
// 				}
// 				sum+=v[i][j];
// 				printf("%d +",v[i][j]);
// 			}
// 			printf("\n");
// 		}
// 	}
// 	return 0;
// }