// This is a comment in C
#include <stdio.h> // alows inputs and outputs

int main(){
    int number = 12;
    float pi = 3.14;
    char name[] = "Xavier";
    char person[50];
    int age;

    printf("Age?\n");
    scanf("%d", &age);
    printf("Name?\n");
    scanf("%s", &person);

    printf("%d\n", number); // \n makes new line
    printf("%f\n", pi);
    printf("%s is %d years old.\n", name, age);
    printf("Name is %s and is %d years old.", person, age);
    return 0; // always last line of main
}