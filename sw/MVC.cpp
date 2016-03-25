#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


class Department
{
private:
	string name;
	int num;
public:
	Department(string nam, int number){
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
	Courses(string name, string slot, int room){
		this->name = name;
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
		this->name = name;
	}
	void setSlot(string slot){
		this->timeSlot = slot;		
	}
	void setRoom(int room){
		this->roomNumber = room;
	}
};

class Professor
{
private:
	string name;
	Department *dep;
	vector<Courses*> v;
public:
	Professor(string name){
		this->name=name;
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

	void addCourses(Courses *c){
		v.push_back(c);
	}
};

class View
{
public:
	View(){}
	~View(){}
	void printCourses(string name, string Slot, int room ){
		cout << "name " << name << endl;
		cout << "Slot " << Slot << endl;
		cout << "room " << room << endl;
		 
	}
		
};


class Controller
{
	private: View *view;
public:
	Controller(View *v){
		this->view = v;
	}
	~Controller(){}
	void Printcoursescontrol(Courses* cor)
	{
		view->printCourses(cor->getName(), cor->getSlot(), cor->getRoom());
	}
	void assignCourse(Professor *prof, Courses *cor){
		prof->addCourses(cor);
	}
	void assignDep(Professor *prof, Department *dep){
		prof->setDep(dep);
	}
};

int main(){

    View *view = new View();
	Controller *cont= new Controller(view);
	Courses *math = new Courses("Math","10 to 20",201);
	Courses *compilers = new Courses("compilers","10 to 20",201);	
	Courses *sw = new Courses("sw","10 to 20",201);
	
	Department *dep = new Department("Computer", 1);


	Professor *prof = new Professor("ahmaad");

	cont->assignCourse(prof,math);
	cont->assignCourse(prof,compilers);

	cont->assignDep(prof,dep);

	cont->Printcoursescontrol(sw);
	return 0;

}