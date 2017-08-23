#include <iostream>
using namespace std;

int arr[200000];

bool jump(int sum, int* d, int n, int x){

	cout << sum  << endl;
	if(sum==x){
		return true;
	}
	else if(sum < x){
		for (int i = 0; i < n; ++i)
		{
			jump(sum+=arr[i],arr, n, x);
		}
	}else{
		return false;
	}
}

int main() {
	// your code goes here
	int n,x,xi;

	cin>>n>>x;
	for (int i = 0; i < n; ++i)
	{
		cin>>xi;
		arr[i]=xi;
	}

	cout << "Can Jump is " << jump(0, arr, n, x);	
	return 0;
}