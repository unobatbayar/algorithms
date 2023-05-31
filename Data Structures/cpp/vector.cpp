#include <iostream>
#include <vector>
using namespace std;

/**
 * Vectors are sequence containers representing arrays that can change in size.
 * https://cplusplus.com/reference/vector/vector/
 **/
int main()
{

	vector<int> v1;
	v1.push_back(10);
	v1.push_back(20); // add element to the back
	v1.pop_back();    // delete last element
	
	// while (!v1.empty())
	// {
		
	// }

	for(int i = 0; i<v1.size(); ++i){
		out << v1[i] << endl;
	}

	cout << "vector size: " << v1.size();
	return 0;
}
