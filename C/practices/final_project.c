// BO, EA, 3 Final C project
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdbool.h>

// Variables for later
char spot1 = '_';
char spot2 = '_';
char spot3 = '_';
char spot4 = '_';
char spot5 = '_';
char spot6 = '_';
char spot7 = '_';
char spot8 = '_';
char spot9 = '_';
int p_win_check = 0;
int b_win_check = 0;

// Prints the board
void grid (){
    printf("\n_%c_|_%c_|_%c_\n", spot1, spot2, spot3);
    printf("_%c_|_%c_|_%c_\n", spot4, spot5, spot6);
    printf(" %c | %c | %c \n", spot7, spot8, spot9);
}

// Creates the bot's input
int bot(){
    srand(time(NULL));
    int x = rand() % 9;
    return x;
}

// Takes the player's input
int player(){
    int answer;
    printf("\nWhat spot do you want to enter (1-9): ");
    scanf("%d", &answer);
    return answer;
}

// spot_check checks if the spot is taken or not and returns a 1 if the spot is open
int spot_check(char spot_value){
    if (spot_value != '_'){
        return 0;
    }else{
        return 1;
    }
}

// big_spot_check makes sure that the spot inputed by the player or bot and makes it an X or O
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
        int check = spot_check(spot9);
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

// Checks if the player won
int check_win(){
    if (spot1 == 'X' && spot2 == 'X' && spot3 == 'X'){
        printf("Player wins!");
        return 1;
    }else if (spot4 == 'X' && spot5 == 'X' && spot6 == 'X'){
        printf("Player wins!");
        return 1;
    }else if (spot7 == 'X' && spot8 == 'X' && spot9 == 'X'){
        printf("Player wins!");
        return 1;
    }else if (spot1 == 'X' && spot4 == 'X' && spot7 == 'X'){
        printf("Player wins!");
        return 1;
    }else if (spot2 == 'X' && spot5 == 'X' && spot8 == 'X'){
        printf("Player wins!");
        return 1;
    }else if (spot3 == 'X' && spot6 == 'X' && spot9 == 'X'){
        printf("Player wins!");
        return 1;
    }else if (spot1 == 'X' && spot5 == 'X' && spot9 == 'X'){
        printf("Player wins!");
        return 1;
    }else if (spot3 == 'X' && spot5 == 'X' && spot7 == 'X'){
        printf("Player wins!");
        return 1;
    }else{
        return 0;
    }
}

// Checks if the bot won
int bot_check_win(){
     if (spot1 == 'O' && spot2 == 'O' && spot3 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else if (spot4 == 'O' && spot5 == 'O' && spot6 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else if (spot7 == 'O' && spot8 == 'O' && spot9 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else if (spot1 == 'O' && spot4 == 'O' && spot7 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else if (spot2 == 'O' && spot5 == 'O' && spot8 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else if (spot3 == 'O' && spot6 == 'O' && spot9 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else if (spot1 == 'O' && spot5 == 'O' && spot9 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else if (spot3 == 'O' && spot5 == 'O' && spot7 == 'O'){
        printf("Bot wins! It's random gentor you bum.");
        return 1;
    }else{
        return 0;
    }
}

int main(){
    int round = 0;
// The main game loop
    while(round <= 10){
        // Game loop for player's turn
        while(true){
            if (p_win_check == 1 || b_win_check == 1){
                round += 10;
                break;
            }
            int player_answer = player();
            int big_check = big_spot_check(player_answer, 0);
            if (big_check == 1){
                grid();
                int p_win_check = check_win();
                if (p_win_check == 1 || b_win_check == 1){
                    round += 10;
                    break;
                }
                round++;
                break;
            }else{
                printf("Not valid\n");
            }
        }
        // Game loop for bot's turn
        while (true){
            if (p_win_check == 1 || b_win_check == 1){
                round += 10;
                break;
            }
            int bot_answer = bot();
            int big_check_bot = big_spot_check(bot_answer, 1);
            if (big_check_bot == 1){
                grid();
                int b_win_check = bot_check_win();
                if (p_win_check == 1 || b_win_check == 1){
                    round += 10;
                    break;
                }
                round++;
                break;
            }
        }
        
    }

    return 0;
}
