#include <iostream>

int getHighestHeight(int (&testTubeHeights)[500]) {
    int highest = 0;
    for (int i : testTubeHeights) {
        if (i > highest){
            highest = i;
        }
    }
    return highest;
}

int main() {
    int Height[500] = {}; //set the heights here (must have 500 elements) here
    std::cout << getHighestHeight(Height);
}