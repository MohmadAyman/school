#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
using namespace std;

	int n,t,tc,track,opt;
	//string place;
	vector <int> arr;
	vector <int> opt_track;
	//int arr_sums[401]={-1};
	//string arr_strings[401]="";
	

void cd(vector<int> tracks,int sum,int N){
	//cout<<"In Func"<<endl;
    sum+=arr[N];
    tracks.push_back(arr[N]);
    if(sum>opt||(sum==opt && tracks.size()>opt_track.size())){
        opt=sum;
        opt_track=tracks;
    }
    for(int i=N+1;i<t;i++){
        if(sum+arr[i]<=n)
            cd(tracks,sum,i);
    }
}

int main()
{
	//tc=5;
	while(cin>>n>>t){
		//cout<<"In Main"<<endl;
		//cin>>n>>t;
		arr.resize(t);
		vector<int> track;
		for(int i=0;i<t;i++){
			cin>>arr[i];
		}
		//cout<<"Took Input"<<arr[0]<<endl;
		opt=0;
		for(int i=0;i<t;i++){
			//cout<<"In Loop"<<endl;
			cd(track,0,i);
		}
		
		int len=opt_track.size();
		for(int i=0;i<len;i++){
			cout<<opt_track[i]<<" ";
		}
		cout<<"sum:"<<opt<<endl;
	}

	return 0;
}