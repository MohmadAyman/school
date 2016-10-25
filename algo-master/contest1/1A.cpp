#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;


bool isDescending(vector <int> arr, int size) {
    for (int i = 0; i < size - 1; i++) {
        if (arr[i] < arr[i+1]) {
            return false;
        }
    }
    return true;
}

int main()
{
	int n;
	vector <int> train;

	while(1){
		cin>>n;
	//	cout<<"In first while"<<endl;
		if(n==0)
			break;

		while(1){
		//	cout<<"In Second while"<<endl;
			train.resize(n);
			cin>>train[0];
			if (train[0]==0){
				cout<<endl;
				break;
			}
			
			
			for(int i=1;i<n;i++)
				cin>>train[i];
		//	cout<<"Took Train"<<endl;

			stack<int> station;
			int coach=1; int count=0;

			while(coach<=n){
			//	cout<<"Counting Coach"<<endl;
				station.push(coach);
				
			//cout<<train[0]<<" "<<train[1]<<" "<<train[2]<<" "<<train[3]<<" "<<endl;
			//cout<<train[count]<<endl;
			//cout<<station.top()<<endl;
			//cout<<station.empty()<<endl;
			while(station.empty()==false && station.top() == train[count]){
			//	cout<<"In Fourth while"<<endl;
				station.pop();
				//cout<<"Popped"<<endl;
				count++;
				//cout<<"Counting"<<endl;
				if(count>=n)
					break;
			}
			//cout<<"Done"<<endl;
			coach++;
		}

			if(station.empty()==true)
				cout<<"Yes"<<endl;
			else
				cout<<"No"<<endl;

		}
	}

	/*//cout<<"Went UP"<<endl;
		while(cin>>n){
		stack<int> sIN;
		//stack<int> sOUT;
		vector<int> v(n);
		
		for(int i=0;i<n;i++){
			cin>>train;
			if(train==0){
				cout<<endl;
				//break;
			}
			sIN.push(train);
		}

		for(int i=0;i<n;i++){
			v[i]=sIN.top();
			if(v[i]==0)
			break;
			cout<<v[i]<<" ";
			//cout<<v[i]<<" ";
			if(sIN.empty()!=true)
			sIN.pop();
		}
		if(is_sorted(v.begin(), v.end())==true || isDescending(v,n)==true)
			cout<<"Yes"<<endl;
		else
			cout<<"No"<<endl;


	//	int trial;
	//	cin>>trial;
	//	if(trial==0)
	//		return 0;
	//	else
	//	goto start_again;
	}*/
	return 0;
}