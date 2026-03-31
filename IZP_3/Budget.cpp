#include "Budget.h"

void Budget::addExpense(const Expense& e) {
    expenses.push_back(e);
}

double Budget::getTotal() const {
    double total = 0;
    for (const auto& e : expenses) total += e.amount;
    return total;
}