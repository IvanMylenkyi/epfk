#include <iostream>
#include "Budget.h"

int main() {
    Budget myBudget;
    myBudget.addExpense(Expense("Food", 250.50));
    myBudget.addExpense(Expense("Internet", 150.00));

    std::cout << "--- Expense Tracking System ---" << std::endl;
    std::cout << "Total Expenses: " << myBudget.getTotal() << " UAH" << std::endl;
    return 0;
}