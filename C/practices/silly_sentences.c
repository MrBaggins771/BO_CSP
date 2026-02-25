// BO 3 Silly Sentences
#include <stdio.h>
#include <string.h>
int main(){
    char silly_sentence[] = "This possible human, ";
    char name_1[20];
    char verb_1[20];
    char place_1[30];
    char adjective_1[20];
    char adjective_2[20];
    char object_1[20];

    printf("Please make sure all answers are ONE WORD.\n");
    
    printf("Give me a name: ");
    scanf("%s", &name_1);

    printf("\nGive me a past tence action verb: ");
    scanf("%s", &verb_1);

    printf("\nGive me a place: ");
    scanf("%s", &place_1);

    printf("\nGive me an adjective: ");
    scanf("%s", &adjective_1);

    printf("\nGive me an adjective: ");
    scanf("%s", &adjective_2);

    printf("\nGive me an object: ");
    scanf("%s", &object_1);

    strcat(silly_sentence, name_1);
    strcat(silly_sentence, ", ");
    strcat(silly_sentence, verb_1);
    strcat(silly_sentence, " to ");
    strcat(silly_sentence, place_1);
    strcat(silly_sentence, ". ");
    strcat(silly_sentence, "There they saw a ");
    strcat(silly_sentence, adjective_1);
    strcat(silly_sentence, ", ");
    strcat(silly_sentence, adjective_2);
    strcat(silly_sentence, " ");
    strcat(silly_sentence, object_1);
    strcat(silly_sentence, ".");
    
    printf("\n%s", silly_sentence);
    return 0;
}