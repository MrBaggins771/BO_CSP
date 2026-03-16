// BO, EA, 3 Final C project
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void row_one (char spot1, char spot2, char spot3){
    printf("_%c_|_%c_|_%c_\n", spot1, spot2, spot3);
}
void row_two (char spot4, char spot5, char spot6){
    printf("_%c_|_%c_|_%c_\n", spot4, spot5, spot6);
}
void row_three (char spot7, char spot8, char spot9){
    printf(" %c | %c | %c \n", spot7, spot8, spot9);
}

int bot(){
    srand(time(NULL));
    int x = rand() % 9;
    return x;
}

int player(){
    int answer;
    printf("what spot do you want to enter (1-9):");
    scanf("%d", &answer);
}

int main(){







    
    



    
    //input and outputs areaa of rodot
    srand(time(NULL));
    int x = rand() % 9;
    printf("%d\n", x);

    //player input
    int player;
    printf("what spot do you want to enter (1-9):");
    scanf("%d", &player);
    
   
    
    

    return 0;
}