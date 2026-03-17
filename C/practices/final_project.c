// BO, EA, 3 Final C project
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void grid (){
    printf("_%c_|_%c_|_%c_\n", spot1, spot2, spot3);
    printf("_%c_|_%c_|_%c_\n", spot4, spot5, spot6);
    printf("_%c_|_%c_|_%c_\n", spot7, spot8, spot9);
}

int bot(){
    srand(time(NULL));
    int x = rand() % 9;
    return x;
}

int player(){
    int answer;
    printf("What spot do you want to enter (1-9):");
    scanf("%d", &answer);
    return answer;
}

void big_spot_check(int answer, int bot_or_player){
        if (answer = 1){
            int check = spot_check(spot1);
            if (check = 1 && bot_or_player = 0){
                char spot1 = "X"
            }else if (check = 1 && bot_or_player = 1){
                char spot1 = "O"
            }else{
                printf("not valid")
            }
        }else if (player_answer = 2){
            int check = spot_check(spot2);
        }else if (player_answer = 3){
            int check = spot_check(spot3);
        }else if (player_answer = 4){
            int check = spot_check(spot4);
        }else if (player_answer = 5){
            int check = spot_check(spot5);
        }else if (player_answer = 6){
            int check = spot_check(spot6);
        }else if (player_answer = 7){
            int check = spot_check(spot7);
        }else if (player_answer = 8){
            int check = spot_check(spot8);
        }else if (player_answer = 9){
            int check = spot_check(spot9);
        }else{
            printf("Please put a valid input.")
        }
}

int spot_check(char spot_value){
    if (spot_value != "_"){
        return 0;
    }else{
        return 1;
    }
}

int main(){
    char spot1 = "_";
    char spot2 = "_";
    char spot3 = "_";
    char spot4 = "_";
    char spot5 = "_";
    char spot6 = "_";
    char spot7 = "_";
    char spot8 = "_";
    char spot9 = "_";

    int round = 0;

    while(round <= 10){
        int player_answer = player();
    }

    //input and outputs area of rodot
    srand(time(NULL));
    int x = rand() % 9;
    printf("%d\n", x);
    
    //player input
    int player;
    printf("what spot do you want to enter (1-9):");
    scanf("%d", player);

    return 0;
}