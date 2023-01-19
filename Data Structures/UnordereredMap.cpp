#include <iostream>
#include <unordered_map>
using namespace std;

/**
 *  * @author code_report
 * https://www.youtube.com/watch?v=24VAm8gzWq4
 * 
 * Stores in any order, faster than Map but methods are same
 * 
 * Common methods
 * insert() O(1)
 * find() O(1)
 * [] -> bracket operator O(1)
 * size() O(1) 
 **/

int main() {
    
	// Let's map employee id
	unordered_map<string, int> m1;
	m1.insert(make_pair("John", 172397)); // m = {"John", 172397} 
	
	auto it = m1.find("John");
	cout << (it != m1.end() ? "Employee found!" : "Not found.") << endl;

	cout << "John's employee ID: " << m1["John"] << endl;
	
	// We can directly increment the value like array
	m1["John"]++;  // m = {"John", 172398} 

	return 0;
}


