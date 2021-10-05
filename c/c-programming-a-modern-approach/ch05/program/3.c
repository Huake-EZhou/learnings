//Calculates a broker's commission

#include<stdio.h>
int main(void) {
    /*
    qty: the quantity of stock
    price: the price of stock
    commission1: the commision of broker
    commission2: the commision of competitor
    */
    int qty;
    float price, commission1, commission2;

    printf("Enter the quantity and price of stock:");
    scanf("%d%f", &qty, &price);

    printf("%d, %f", qty, price);
    return 0;

}
