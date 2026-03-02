//BO loops and strings
#include <stdio.h>
#include <string.h>
// for random
#include <stdlib.h>
#include <time.h>

int main(){
    // while EX 1
    int i = 1;
    while (i <= 10){
        printf("%d\n", i);
        i++;
    }
    //generate random num
    srand(time(NULL));
    printf("%d\n", rand());
    printf("%d\n", rand() % 10); // modulo makes it the largest number.
    printf("%d\n", (rand() % 9)+1); // adding makes it the minimun number but you have to adjust with the max as well

    // while EX 2
    int goose = (rand() % 9) + 1;
    int count =1; 
    while (count < goose){
        printf("Duck\n");
        count++;
    }
    printf("Goose");

    // while EX 3
    int timer = 30;
    while (timer > 0){
        printf("%d\n", timer);
        timer = timer - 2;
    }
    printf("Times up\n");

    // LISTS
    // list EX 1
    int num_list[] = {74, 88, 95, 87, 98};
    printf("%d\n", num_list[2]);
    
    // list EX 2
    float sizes[] = {3.57, 24.95, 36.1, 5.99};
    printf("%.2f\n", sizes[0]);
    sizes[0] = 10.45;
    printf("%.2f\n", sizes[0]);

    // list EX 3
    char names[][20] = {"ALex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake"}; // first box is number of items second is max characters in the strings (required).
    printf("%s\n", names[5]);
    return 0;
}