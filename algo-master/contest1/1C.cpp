#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n,t;
vector <int> arr;
vector <int> vec;
map <vector<int>,bool> sums;


void summation(vector <int> vec,int k,int m,int sum){
	    //cout<<"In Func"<<endl;
	if(sum==t){
		if(sums[vec]==true)
			return;
		sums[vec]=true;

		for(int i=0;i<k;i++){
				if(i>0)
				cout<<"+";
				cout<<vec[i];
				
		}
		//cout<<"\b \b";
		cout<<endl;
		return;
	}
	
	if(sum>t|| m==n)
	return;
	
	for(int i=m;i<n;i++){
		vec.push_back(arr[i]);
		summation(vec,k+1,i+1,sum+arr[i]);
		vec.pop_back();
	}
}


int main()
{
    	while(cin>>t>>n){
    		
    		if(t==0)
    		break;
		//cout<<"In Main"<<endl;
		//cin>>n>>t;
		arr.resize(n);
		//vector<int> numbars;
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		//cout<<"Took Input"<<arr[0]<<endl;
		//opt=0;
		sums.clear();
		cout<<"Sums of "<<t<<":"<<endl;
			//cout<<"In Loop"<<endl;
			summation(vec,0,0,0);
		if(sums.size()==0)
		cout<<"NONE"<<endl;
	}

    return 0;
}

