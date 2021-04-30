#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int x1 = 0;
    int x2 = 0;
    int y1 = 4;
    int y2 = 4;

    // Pythagorean theorem to find distance of (x1, y1) and (x2, y2) coordinates
    // 𝑑=√(𝑥2−𝑥1)2+(𝑦2−𝑦1)2
    int distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
    prinft("%d", distance);
    return 0;
}
