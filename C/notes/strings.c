// BO strings notes
#include <stdio.h>
#include <string.h>
int main(){
    char variable_name[] = "String Value.";
    char variable_name_2[30];
    printf("Printing String\n");
    printf("%s\n", variable_name);

    char subject[] = "CSP";
    char book[50];
    printf("%s\n", subject);
    
    //printf("Write a 1 word book name: ");
    //scanf("%s", book);
    
    printf("Write a book title: ");
    fgets(book, sizeof(book), stdin); //this is for multiple words & makes new line after input.
    
    printf("The book is %s\n", book);
    
    //concatination
    char name[] = "Brody";
    char last[] = "Olson";
    strcat(name, " ");
    strcat(name, last);
    printf("%s\n", name);

    // length of string
    printf("%lu", strlen(name));
    return 0;
}