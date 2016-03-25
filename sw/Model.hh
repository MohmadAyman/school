#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Department;
class Courses;
class Professor
{
private:
	string name;
	Department *dep;
	vector<Courses> v;
public:
	Professor(string name){
		this.name=name;
	};
	~Professor();
	string getName(){
		return name;
	}
	Department* getDep(){
		return dep;
	}	
	void setDep(Department *d){
		dep = d;
	}

	void addCourses(Courses c){
		v.push_back(c);
	}
};

class Department
{
	private:
	string name;
	int num;
public:
	Department(sting nam, int number){
		name = nam;
		num = number;
	};
	~Department();
	
};

class Courses
{
private:
	string name;
	string timeSlot;
	int roomNumber;
public:
	Courses(string slot, sting name, int room){
		this.name = name;
		timeSlot = slot;
		roomNumber = room;
	};
	~Courses();
	string getName(){
		return name;
	}
	string getSlot(){
		return timeSlot;
	}
	int getRoom(){
		return roomNumber;
	}
	void setName(string name){
		this.name = name;
	}
	void setSlot(string slot){
		this.timeSlot = slot;		
	}
	void setRoom(int room){
		this.roomNumber = room;
	}
};