//Calculates a broker's commission

#include<stdio.h>
int main(void) {
    /*
    qty: the quantity of stock
    price: the price of stock
    commission1: the commision of broker
    commission2: the commision of competitor
    */
    int qty, value;
    float price, commission1, commission2;

    printf("Enter the quantity and price of stock:");
    scanf("%d%f", &qty, &price);
    // 整数 * 浮点数的结果是浮点数。
    value = qty * price;

    /*题目佣金费用那里保留两位小数，所以这里也保留两位小数*/
    if (value < 2500.00f)
        commission1 = 30 + 0.017 * value;
    else if (value < 6250)
        commission1 = 56 + 0.0066 * value;
    else if (value < 20000)
        commission1 = 76 + 0.0034 * value;
    else if (value < 50000)
        commission1 = 100 + 0.0022 * value;
    else if (value < 500000)
        commission1 = 155 + 0.0011 * value;
    else
        commission1 = 255 + 0.0009 * value;

    if (commission1 < 39.00f)
        commission1 = 39.00f;

    if (qty < 2000)
        commission2 = 33 + 0.30f * qty;
    else
        commission2 = 33 + 0.20f * qty;
    printf("The commission is: $%.00f and rival broker's commission is: $%.00f", commission1, commission2);
    return 0;

}
