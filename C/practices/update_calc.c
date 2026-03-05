// BO 3 update calc
#include <stdio.h>
#include <math.h>

float question(char*cost){
    float answer;
    printf("What is your monthy %s?\n", cost);
    scanf("%f", &answer);
    return answer;
}

int percent_calc(int cost, int income){
    int percent = (cost / income) * 100;
    return percent;
}

void print(char*cost_name, float cost, int cost_percent){
    printf("Your monthly %s is %.2f which is %d percent of your income.", cost_name, cost, cost_percent)
}

int main(){
    float income = question("income");
    float housing = question("housing");
    float utilities = question("utilities");
    float groceries = question("groceries");
    float transit = question("transit");
    
    int housing_p = percent_calc(housing, income);
    int utilities_p = percent_calc(utilities, income);
    int groceries_p = percent_calc(groceries, income);
    int transit_p = percent_calc(transit, income);
    return 0;
}