#ifndef EXPENSE_H
#define EXPENSE_H
#include <string>

class Expense {
public:
    std::string category;
    double amount;
    Expense(std::string cat, double amt);
};
#endif