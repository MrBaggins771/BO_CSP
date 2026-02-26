// BO conditional notes
#include <stdio.h>
#include <string.h>
#include <stdbool.h> // required for a bool variable.
int main(){
    int grade = 97;
    bool admin = 0;
    if (grade >= 90){
        printf("You have an A!\n");
    }else if (grade >= 80){
        printf("You have a B!\n");
    }else if (grade >= 70){
        printf("You have a C.\n");
    }else if (grade >= 60){
        printf("You have a d.\n");
    }else{
        printf("You are failing.\n");
    };

    int num = 4;
    if (num%2 == 0 && (num < 10 && num > -10)){
        printf("%d is a single digit even number.\n", num);
    }else if (num%2 != 0 && (num < 10 && num > -10)){
        printf("%d is a single digit odd number.\n", num);
    }else{
        printf("%d is not a single digit number.\n", num);
    };

    char name[] = "Cora";
    if (strcmp(name, "Cora") == 0){
        printf("Welcome Admin\n");
    }else{
        printf("Hello %s.\n", name);
    };

    return 0;
}