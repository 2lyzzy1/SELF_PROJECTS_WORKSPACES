// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    printf(" ::::::: CALCULATRICE_SIMPLE ::::::: ");
    int N[2] = {};
    char operators[] = {'+', '-', '*', '/'};
    char operat;
    
    printf(" Entrez deux nombres (sep=' ') : \n");
    for (int n = 0; n < 2; n++) {
        scanf(" %d ", N[n]);
    }
    printf(" Opération à effectuer (between %s) :", operators);
    scanf(" %s ", operat);
    //
    switch (operat) {
        case '+' :
            printf("Good Day");
        default :
            break;
    }
    
    return 0;
}