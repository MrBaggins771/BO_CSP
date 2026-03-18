// BO, EA, 3 Final C project
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


char spot1 = '_';
char spot2 = '_';
char spot3 = '_';
char spot4 = '_';
char spot5 = '_';
char spot6 = '_';
char spot7 = '_';
char spot8 = '_';
char spot9 = '_';

void grid (){
    printf("_%c_|_%c_|_%c_\n", spot1, spot2, spot3);
    printf("_%c_|_%c_|_%c_\n", spot4, spot5, spot6);
    printf(" %c | %c | %c \n", spot7, spot8, spot9);
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

int spot_check(char spot_value){
    if (spot_value != '_'){
        return 0;
    }else{
        return 1;
    }
}

int big_spot_check(int answer, int bot_or_player){
    if (answer == 1){
        int check = spot_check(spot1);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot1 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot1 = 'O';
            return 1;
        }
    }else if (answer == 2){
        int check = spot_check(spot2);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot2 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot2 = 'O';
            return 1;
        }
    }else if (answer == 3){
        int check = spot_check(spot3);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot3 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot3 = 'O';
            return 1;
        }
    }else if (answer == 4){
        int check = spot_check(spot4);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot4 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot4 = 'O';
            return 1;
        }
    }else if (answer == 5){
        int check = spot_check(spot5);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot5 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot5 = 'O';
            return 1;
        }
    }else if (answer == 6){
        int check = spot_check(spot6);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot6 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot6 = 'O';
            return 1;
        }
    }else if (answer == 7){
        int check = spot_check(spot7);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot7 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot7 = 'O';
            return 1;
        }
    }else if (answer == 8){
        int check = spot_check(spot8);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot8 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot8 = 'O';
            return 1;
        }
    }else if (answer == 9){
        int check = spot_check(spot3);
        if (check == 0){
            return 0;
        }else if (check == 1 && bot_or_player == 0){
            spot9 = 'X';
            return 1;
        }else if (check == 1 && bot_or_player == 1){
            spot9 = 'O';
            return 1;
        }
    }
}

void check_win(){
    if ())
}

int main(){
    int round = 0;

    while(round <= 10){
        int player_answer = player();
        int big_check = big_spot_check(player_answer, 0);
        if (big_check == 1){
            grid();
            round++;
        }else{
            printf("")
        }
    }

    //input and outputs area of rodot
    srand(time(NULL));
    int x = rand() % 9;
    printf("%d\n", x);

    int player;
    printf("what spot do you want to enter (1-9):");
    scanf("%d", player);


    return 0;
}