// BO 3 update calc
#include <stdio.h>
#include <math.h>

//Function for obtaining information
float question(char*cost){
    float answer;
    printf("\nWhat is your monthy %s? $", cost);
    scanf("%f", &answer);
    return answer;
}

//Function for percent calculations
float percent_calc(float cost, float income){
    float percent = (cost / income) * 100;
    return percent;
}

//Function giving information back
void printc(char*cost_name, float cost, float cost_percent){
    printf("\nYour monthly %s bill is $%.2f which is %.2f percent of your income.", cost_name, cost, cost_percent);
}

int main(){
    float income = question("income");
    float housing = question("housing");
    float utilities = question("utilities");
    float groceries = question("groceries");
    float transit = question("transit");
    
    float housing_p = percent_calc(housing, income);
    float utilities_p = percent_calc(utilities, income);
    float groceries_p = percent_calc(groceries, income);
    float transit_p = percent_calc(transit, income);

    printc("housing", housing, housing_p);
    printc("utilities", utilities, utilities_p);
    printc("grocery", groceries, groceries_p);
    printc("transit", transit, transit_p);
    
    float savings = income * 0.15;
    float spending = income - (housing + utilities + groceries + transit + savings);
    printf("\nYou should save $%.2f, which is 15 percent of your income.", savings);
    printf("\nYou have $%.2f left to spend.", spending);
    
    return 0;
}