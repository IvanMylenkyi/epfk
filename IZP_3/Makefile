all: app

app: main.o Expense.o Budget.o
	g++ main.o Expense.o Budget.o -o app

main.o: main.cpp
	g++ -c main.cpp

Expense.o: Expense.cpp
	g++ -c Expense.cpp

Budget.o: Budget.cpp
	g++ -c Budget.cpp

clean:
	rm -f *.o app