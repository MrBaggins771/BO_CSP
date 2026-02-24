// BO 3 fincancial calculator
#include <stdio.h>
#include <math.h>
int main(){
    printf("What is your monthly income?\n");
    float monthly_income;
    scanf("%f", &monthly_income);
    
    printf("What is your monthly housing cost?\n");
    float housing_cost;
    scanf("%f", &housing_cost);
    
    printf("What is your monthly utility bill?\n");
    float utility_bill;
    scanf("%f", &utility_bill);

    printf("What is your monthly grocery bill?\n");
    float grocery_bill;
    scanf("%f", &grocery_bill);

    printf("What is your monthly transit cost?\n");
    float transit_cost;
    scanf("%f", &transit_cost);

    int housing_percent = (housing_cost / monthly_income) * 100;
    int utility_percent = (utility_bill / monthly_income) * 100;
    int grocery_percent = (grocery_bill / monthly_income) * 100;
    int transit_percent = (transit_cost / monthly_income) * 100;
    
    float savings = monthly_income * .15;
    float spending = monthly_income - (housing_cost + utility_bill + grocery_bill + transit_cost + savings);

    printf("Your housing cost is $ %f which is %d percent of your income.\n", housing_cost, housing_percent);
    printf("Your utility bill is $ %f which is %d percent of your income.\n", utility_bill, utility_percent);
    printf("Your grocery bill is $ %f which is %d percent of your income.\n", grocery_bill, grocery_percent);
    printf("Your transit cost is $ %f which is %d percent of your income.\n", transit_cost, transit_percent);
    printf("You should save $ %f which is 15 percent of your income.\n", savings);
    printf("You have $ %f left to spend.", spending);
    return 0;
}