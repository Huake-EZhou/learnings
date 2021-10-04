#include<stdio.h>
int main(void) {
    int num, digital;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num >= 0 && num <= 9)
        digital = 1;
    else if(num >= 10 && num <= 99)
        digital = 2;
    else if(num >= 100 && num <= 999)
        digital = 3;
    else if (num >= 1000 && num <= 9999)
        digital = 4;

    printf("The number %d has %d digits.", num, digital);

    return 0;

}
