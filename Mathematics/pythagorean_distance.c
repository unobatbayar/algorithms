#include <stdio.h>
#include <math.h>

int main() 
{
    int x1 = 0;
    int x2 = 0;
    int y1 = 4;
    int y2 = 4;

    int distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
    printf("%d", distance);
    return 0;
}
