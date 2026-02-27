// BO 3 Time o' day
#include <stdio.h>
int main(){
    printf("What is the time of day in military time (please write HHMM with no colin): ");
    int time;
    scanf("%d", &time);
    if (time >= 0 && time < 600){
        printf("Why are you up at this hour?");
    }else if (time >= 600 && time < 1100){
        printf("Good morning.");
    }else if (time >= 1100 && time < 1600){
        printf("Good day to you.");
    }else if (time >= 1600 && time < 2000){
        printf("Good evening.");
    }else if (time >= 2000 && time < 2400){
        printf("Good night.");
    }else{
        printf("Please put a valid time");
    }
    return 0;
}