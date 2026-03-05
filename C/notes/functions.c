// BO 3 function notes
#include <stdio.h>

//cannot write funtions in other funtions
// EX 1
int add(int num_1, int num_2){
    return num_1 + num_2;
}
// EX 2
void greeting(char* name){
    printf("hello %s, welcome to my program.\n", name);
}
// EX 3
float area(int side1, int side2){
    return (float) side1 * side2;
}
int main(){
    // EX 1 cont
    int total = add(40, 2);
    printf("%d\n", total);
    // EX 2 cont
    greeting("alex");
    greeting("kaitie");
    greeting("andrew");
    greeting("tia");
    // EX 3 cont
    float rectangle = area(10,5);
    printf("The area is %.2f\n", rectangle);
    printf("The area is %.2f\n", area(4, 6));

    //funtion == method == procedure

    return 0;
}