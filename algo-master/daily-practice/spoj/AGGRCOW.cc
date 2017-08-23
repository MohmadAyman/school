#include <iostream>
#include <vector>
#include <algorithm>    // std::sort

using namespace std;

vector<int> src;

bool can_place(int aggr_cows, int d){

	int c = aggr_cows;

	int j=1;
	int i=0;
	c--;
	while(j<src.size()){
		if(src[j]-src[i] >= d){
			i=j;j++;c--;
		}
		else{
			j++;
		}
	}
	if(c==0)
		return true;
	return false;

	// for (int i = 0; i < src.size()-1; ++i)
	// {
	// 	if(!(src[i+1]-src[i] >= d )){
	// 		return false;
	// 	}
	// 	c--;
		
	// }

	// cout << c <<endl;
	// if(c==0)
	// 	return true;
	// return false;
}

int main() {
	// your code goes here
	int t,n,c,xi;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		cin>>n>>c;
		// Sort the vector:
		for (int i = 0; i < n; ++i)
		{
			cin>>xi;
			src.push_back(xi);
		}
	  	sort(src.begin(), src.end());

		for (int i = src[src.size()-1]; i > 0; --i)
		{
			// cout << can_place(c, i) << " Can Place " << i << endl;
			if(can_place(c, i)){
				cout << i <<endl;
				break;
			}
		}
	}

	return 0;
}