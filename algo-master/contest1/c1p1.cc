#include <bits/stdc++.h>
#include <string>         // std::string

using namespace std;

int main(){

	int tc,n;
	stack <string> cur;
	stack <string> cur2;
	string path;
	string output;
	std::string dots ("../");
	cin>>tc;
	while(tc--){
		cin>>n;
		getline(cin,path);
		for(int i=0;i<n;i++){
			getline(cin,path);
			if(path == "cd" ){
				while(cur.top()!="/")
					cur.pop();
			}
			else if(path == "cd .."){
				if(!cur.empty())
					cur.pop();
			}
			else if(path=="pwd"){
				while(cur.empty()!=true){
					cur2.push(cur.top());
					cur.pop();
				}
				while(cur2.empty()!=true){
					output=cur2.top();
					cur.push(output);
					cur2.pop();
					cout<<output<< "/";
				}
			}
			else{
				int i =0;
				path = path.substr(3);
				std::size_t foundslash;
				std::size_t found = path.find(dots);
				while(found!=string::npos){
					foundslash = path.find_last_of("/",found-2);
					if(foundslash!=string::npos){
						if(!cur.empty())
							cur.pop();
					}else{
						path = path.substr(0,foundslash) + path.substr(found+3);
					}
					found = path.find(dots);
				}

				foundslash = path.find('/',1);
				while(foundslash!=string::npos){
					string p = path.substr(0,foundslash);
					cout << p<<endl;
					cur.push(p);
					path = path.substr(foundslash+1);
					foundslash = path.find("/");
				}
					string p = path.substr(0,foundslash);
					cout << p<<endl;
					cur.push(p);
			}

		}
	}
	return 0;
}
