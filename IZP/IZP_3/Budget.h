#ifndef BUDGET_H
#define BUDGET_H
#include <vector>
#include "Expense.h"

class Budget {
private:
    std::vector<Expense> expenses;
public:
    void addExpense(const Expense& e);
    double getTotal() const;
};
#endif