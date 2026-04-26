# Документація лабораторних робіт
### Дисципліна: Інструментальні засоби програмування

---

## Зміст

- [Лабораторна робота №1 — Робота з Git](#лабораторна-робота-1)
- [Лабораторна робота №2 — Аудит безпеки залежностей (npm audit + Safety)](#лабораторна-робота-2)
- [Лабораторна робота №3 — Система обліку витрат на C++](#лабораторна-робота-3)
- [Лабораторна робота №4 — Лінтер та форматер коду (flake8 + black)](#лабораторна-робота-4)
- [Лабораторна робота №5 — Тестування (unittest + doctest)](#лабораторна-робота-5)

---

<a name="лабораторна-робота-1"></a>
## Лабораторна робота №1
### Тема: Робота з системою контролю версій Git

**Мета:** навчитися користуватися Git — ініціалізувати репозиторій, робити коміти, працювати з гілками та підключати віддалений репозиторій на GitHub.

---

### Що використовував

- Git
- GitHub
- Термінал (bash / cmd)

---

### Основні команди Git

**Ініціалізація та перший коміт:**

```bash
git init
git add .
git commit -m "first commit"
```

**Підключення до GitHub та пуш:**

```bash
git remote add origin https://github.com/username/repo.git
git branch -M main
git push -u origin main
```

**Робота з гілками:**

```bash
# Створити нову гілку і перейти на неї
git checkout -b feature/my-feature

# Злити гілку в main
git checkout main
git merge feature/my-feature
```

**Перегляд стану і логів:**

```bash
git status
git log --oneline
git diff
```

---

### Типовий workflow

1. Зробив зміни у файлах
2. `git add .` — додав до стейджингу
3. `git commit -m "опис змін"` — зафіксував
4. `git push` — відправив на GitHub

---

### Результат

Створено репозиторій на GitHub, відпрацьовано базові команди Git: `init`, `add`, `commit`, `push`, `branch`, `merge`.

---

<a name="лабораторна-робота-2"></a>
## Лабораторна робота №2
### Тема: Аудит безпеки залежностей (npm audit + Safety scan)

**Мета:** навчитися перевіряти залежності проекту на наявність відомих вразливостей — у JavaScript-проектах через `npm audit`, у Python-проектах через `Safety`.

---

### Частина 1 — JavaScript (npm audit)

Написано простий скрипт на Node.js, який робить GET-запит до публічного API. Але головна мета — не сам запит, а перевірка безпеки пакетів через `npm audit`.

#### Вихідний код (index.js)

```js
const fetch = require('node-fetch');

async function getData() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
        console.log("Статус код:", response.status);
        const data = await response.json();
        console.log("Данні від сервера:", data);
    } catch (error) {
        console.error("Помилка:", error);
    }
}

getData();
```

#### Запуск аудиту

```bash
npm audit
```

#### Результат npm audit

```
found 0 vulnerabilities
```

Версія проекту: `2.7.0` — жодних вразливостей у залежностях не виявлено.

---

### Частина 2 — Python (Safety scan)

Написано аналогічний скрипт на Python. Для перевірки безпеки використовується інструмент `Safety`, який сканує файл `requirements.txt` по базі відомих CVE.

#### Вихідний код (index.py)

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print("Статус код:", response.status_code)
print("респонс сервера:", response.json())
```

#### Запуск сканування

```bash
safety check -r requirements.txt
```

#### Результат Safety scan

```
Safety v3.7.0 is scanning for Vulnerabilities...

  -> requirements.txt

  Using open-source vulnerability database
  Found and scanned 45 packages
  Timestamp 2026-03-31 17:57:35
  0 vulnerabilities reported
  0 vulnerabilities ignored
```

Просканованих пакетів: **45**  
Виявлено вразливостей: **0**

---

### Порівняння інструментів

| | npm audit | Safety (Python) |
|---|---|---|
| Мова | JavaScript / Node.js | Python |
| Що сканує | `package.json` / `node_modules` | `requirements.txt` |
| База даних | npm Advisory Database | PyPI vulnerability database |
| Результат | кількість вразливостей по severity | список CVE або "0 vulnerabilities" |

---

### Висновок

Обидва інструменти дозволяють швидко перевірити, чи немає у залежностях проекту відомих вразливостей. Це важлива частина безпечної розробки — краще перевіряти до деплою, ніж після.

---

<a name="лабораторна-робота-3"></a>
## Лабораторна робота №3
### Тема: Система обліку витрат (C++ + Docker)

**Мета:** розробити об'єктно-орієнтовану програму на C++, навчитися збирати проект через `Makefile` та упакувати його у Docker-контейнер.

---

### Що використовував

- C++ / g++
- Makefile (GNU Make)
- Docker + docker-compose 3.8
- Образ збірки: `gcc:latest`
- Образ запуску: `debian:stable-slim`

---

### Структура проекту

```
lab3/
├── main.cpp
├── Expense.h
├── Expense.cpp
├── Budget.h
├── Budget.cpp
├── Makefile
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

### Опис класів

**`Expense`** — одна витрата:
- `category` (string) — категорія
- `amount` (double) — сума

**`Budget`** — список витрат:
- `addExpense(const Expense& e)` — додає витрату
- `getTotal() const` — повертає загальну суму

---

### Вихідний код

**Expense.h:**
```cpp
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
```

**Budget.cpp:**
```cpp
#include "Budget.h"

void Budget::addExpense(const Expense& e) {
    expenses.push_back(e);
}

double Budget::getTotal() const {
    double total = 0;
    for (const auto& e : expenses) total += e.amount;
    return total;
}
```

**main.cpp:**
```cpp
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
```

---

### Makefile

```makefile
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
```

---

### Dockerfile (двоетапна збірка)

```dockerfile
# Етап 1: компіляція
FROM gcc:latest AS build
WORKDIR /usr/src/app
COPY . .
RUN make

# Етап 2: легкий образ для запуску
FROM debian:stable-slim
WORKDIR /app
COPY --from=build /usr/src/app/app .
CMD ["./app"]
```

---

### Запуск

```bash
docker-compose up --build
```

---

### Результат

```
--- Expense Tracking System ---
Total Expenses: 400.5 UAH
```

---

<a name="лабораторна-робота-4"></a>
## Лабораторна робота №4
### Тема: Лінтер та форматер коду (flake8 + black)

**Мета:** навчитися використовувати інструменти статичного аналізу та автоматичного форматування Python-коду — `flake8` (лінтер) і `black` (форматер). Зрозуміти різницю між ними та навчитися їх налаштовувати.

---

### Що використовував

- Python 3
- `flake8` версії `7.3.0` — перевіряє код на відповідність PEP 8 та шукає помилки
- `black` версії `26.3.1` — автоматично переформатовує код
- Файл `.flake8` — конфігурація лінтера

---

### Різниця між flake8 і black

| | flake8 | black |
|---|---|---|
| Що робить | **перевіряє** і показує помилки | **виправляє** форматування автоматично |
| Чи змінює файли | ні, тільки звітує | так, переписує файл |
| Стиль | PEP 8 | власний стиль black (сумісний з PEP 8) |
| Коли зупиняє збірку | якщо є порушення | — |

---

### Структура проекту

```
lab4/
├── main.py           # програма-приклад для перевірки
├── requirements.txt  # залежності
├── .flake8           # конфігурація лінтера
└── README.md
```

---

### Конфігурація (.flake8)

```ini
[flake8]
max-line-length = 88
extend-ignore = E203
```

`max-line-length = 88` — узгоджено з `black`, щоб вони не конфліктували між собою.  
`extend-ignore = E203` — ігноруємо правило про пробіли перед `:`, бо `black` їх ставить.

---

### Програма для демонстрації (main.py)

Як приклад написана система бронювання кінотеатру:

```python
movies = {}


def addMovie(title: str, price: float):
    movies[title] = price
    print(f"Фільм '{title}' додано. Ціна квитка: {price} грн")


def calculateTicketPrice(movie_title: str, seats: int) -> float:
    if movie_title in movies:
        return movies[movie_title] * seats
    else:
        print(f"Помилка: Фільм '{movie_title}' не знайдено!")
        return 0.0


def bookSeat(movie_title: str, seats: int):
    total_price = calculateTicketPrice(movie_title, seats)
    if total_price > 0:
        print(
            f"Бронювання успішне! {seats} квитків на '{movie_title}'."
            f" До сплати: {total_price} грн"
        )


if __name__ == "__main__":
    print("--- Система бронювання кінотеатру ---")
    addMovie("Dune: Part Two", 180.0)
    addMovie("Deadpool & Wolverine", 200.0)
    bookSeat("Dune: Part Two", 3)
    bookSeat("Avatar 3", 2)
```

---

### Запуск інструментів

```bash
# Встановити залежності
pip install -r requirements.txt

# Перевірити код лінтером
flake8 main.py

# Якщо все добре — виведе нічого (тиша = успіх)
# Якщо є проблеми — покаже, наприклад:
# main.py:3:1: E302 expected 2 blank lines, found 1

# Відформатувати код автоматично
black main.py
# Виведе: reformatted main.py  або  1 file left unchanged
```

---

### Приклад що виявляє flake8

Якщо написати код без пробілів між функціями або з довгими рядками:

```python
# погано — flake8 буде лаятись
def foo():
    x = 1
def bar():   # E302: expected 2 blank lines
    pass
```

```python
# добре — після виправлення або запуску black
def foo():
    x = 1


def bar():
    pass
```

---

### Залежності (requirements.txt)

| Пакет | Версія | Для чого |
|---|---|---|
| flake8 | 7.3.0 | лінтер — перевірка стилю |
| black | 26.3.1 | форматер — автовиправлення |
| pyflakes | 3.4.0 | виявлення логічних помилок |
| pycodestyle | 2.14.0 | перевірка PEP 8 (використовується flake8) |
| mccabe | 0.7.0 | аналіз складності коду |
| click | 8.3.1 | CLI для black |

---

### Висновок

`flake8` і `black` добре працюють разом: `black` форматує код, а `flake8` перевіряє що все відповідає стандарту. Головне — узгодити конфігурацію (зокрема `max-line-length = 88`), щоб вони не суперечили один одному.

---

<a name="лабораторна-робота-5"></a>
## Лабораторна робота №5
### Тема: Тестування Python-коду (unittest + doctest)

**Мета:** навчитися писати автоматичні тести для Python-програм — використовувати `doctest` для простих перевірок прямо у коментарях до функцій, та `unittest` для повноцінного тестування з різними сценаріями.

---

### Що використовував

- Python 3
- `unittest` — вбудований модуль для unit-тестування
- `doctest` — вбудований модуль, запускає приклади з docstring-ів

---

### Структура проекту

```
lab5/
├── calc.py      # калькулятор + doctests
├── tests.py     # unit-тести
└── README.md
```

---

### Програма (calc.py)

Калькулятор вартості електроенергії. Дві основні функції з вбудованими doctests:

```python
def calculate_consumption(previous_reading: float, current_reading: float) -> float:
    """
    Обчислює кількість спожитої електроенергії (у кВт-год).

    >>> calculate_consumption(100.0, 150.0)
    50.0
    >>> calculate_consumption(200.5, 300.5)
    100.0
    >>> calculate_consumption(150.0, 100.0)
    Traceback (most recent call last):
        ...
    ValueError: Поточні показники не можуть бути меншими за попередні.
    """
    if current_reading < previous_reading:
        raise ValueError("Поточні показники не можуть бути меншими за попередні.")
    return current_reading - previous_reading


def calculate_energy_bill(consumption: float, rate: float = 4.32) -> float:
    """
    Обчислює суму до оплати за спожиту електроенергію.
    (За замовчуванням тариф 4.32 грн за кВт-год).

    >>> calculate_energy_bill(50.0, 4.32)
    216.0
    >>> calculate_energy_bill(100.0, 4.32)
    432.0
    >>> calculate_energy_bill(-10.0, 4.32)
    Traceback (most recent call last):
        ...
    ValueError: Споживання не може бути від'ємним.
    """
    if consumption < 0:
        raise ValueError("Споживання не може бути від'ємним.")
    return consumption * rate


def main():
    print("=== Калькулятор вартості електроенергії ===")
    try:
        prev = float(input("Введіть попередні показники лічильника (кВт-год): "))
        curr = float(input("Введіть поточні показники лічильника (кВт-год): "))
        rate_input = input("Введіть тариф (грн за кВт-год, натисніть Enter для 4.32): ")

        rate = float(rate_input) if rate_input else 4.32

        consumption = calculate_consumption(prev, curr)
        bill = calculate_energy_bill(consumption, rate)

        print("\n--- Рахунок за електроенергію ---")
        print(f"Спожито: {consumption:.2f} кВт-год")
        print(f"Тариф: {rate:.2f} грн/кВт-год")
        print(f"Сума до оплати: {bill:.2f} грн")
        print("---------------------------------")
    except ValueError as e:
        print(f"Помилка: {e}. Будь ласка, вводьте коректні числові значення.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
```

---

### Різниця між doctest і unittest

| | doctest | unittest |
|---|---|---|
| Де пишеться | прямо у docstring функції | окремий файл |
| Синтаксис | як у Python-інтерпретаторі (`>>>`) | методи класу `TestCase` |
| Для чого підходить | прості приклади, документація | повноцінне тестування, багато сценаріїв |
| Чи перевіряє винятки | так (`Traceback...`) | так (`assertRaises`) |

---

### Unit-тести (tests.py)

```python
import unittest
from calc import calculate_consumption, calculate_energy_bill

class TestElectricityCalculator(unittest.TestCase):

    def test_calculate_consumption_normal(self):
        # звичайний випадок
        self.assertEqual(calculate_consumption(100.0, 150.0), 50.0)

    def test_calculate_consumption_zero(self):
        # якщо показники однакові — споживання 0
        self.assertEqual(calculate_consumption(150.0, 150.0), 0.0)

    def test_calculate_consumption_error(self):
        # поточне менше за попереднє — має кинути ValueError
        with self.assertRaises(ValueError):
            calculate_consumption(200.0, 150.0)

    def test_calculate_energy_bill_normal(self):
        self.assertEqual(calculate_energy_bill(50.0, 4.32), 216.0)

    def test_calculate_energy_bill_zero(self):
        # нульове споживання — рахунок теж 0
        self.assertEqual(calculate_energy_bill(0.0, 4.32), 0.0)

    def test_calculate_energy_bill_error(self):
        # від'ємне споживання — має кинути ValueError
        with self.assertRaises(ValueError):
            calculate_energy_bill(-10.0, 4.32)

if __name__ == '__main__':
    unittest.main()
```

---

### Таблиця тест-кейсів

| Тест | Вхід | Очікуваний результат | Тип перевірки |
|---|---|---|---|
| `test_calculate_consumption_normal` | prev=100.0, curr=150.0 | 50.0 | `assertEqual` |
| `test_calculate_consumption_zero` | prev=150.0, curr=150.0 | 0.0 | `assertEqual` |
| `test_calculate_consumption_error` | prev=200.0, curr=150.0 | `ValueError` | `assertRaises` |
| `test_calculate_energy_bill_normal` | consumption=50.0, rate=4.32 | 216.0 | `assertEqual` |
| `test_calculate_energy_bill_zero` | consumption=0.0, rate=4.32 | 0.0 | `assertEqual` |
| `test_calculate_energy_bill_error` | consumption=-10.0, rate=4.32 | `ValueError` | `assertRaises` |

---

### Запуск тестів

```bash
# Запустити unit-тести
python -m unittest tests.py

# Запустити doctests з детальним виводом
python -m doctest -v calc.py

# Або запустити основну програму (doctests запустяться автоматично)
python calc.py
```

---

### Результат unittest

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Всі 6 тестів пройшли без помилок.

---

### Результат doctest -v

```
Trying:
    calculate_consumption(100.0, 150.0)
Expecting:
    50.0
ok
Trying:
    calculate_consumption(150.0, 100.0)
Expecting:
    Traceback (most recent call last):
        ...
    ValueError: Поточні показники не можуть бути меншими за попередні.
ok
...
5 items passed all tests
```

---

### Приклад роботи програми

```
=== Калькулятор вартості електроенергії ===
Введіть попередні показники лічильника (кВт-год): 1200
Введіть поточні показники лічильника (кВт-год): 1350
Введіть тариф (грн за кВт-год, натисніть Enter для 4.32):

--- Рахунок за електроенергію ---
Спожито: 150.00 кВт-год
Тариф: 4.32 грн/кВт-год
Сума до оплати: 648.00 грн
---------------------------------
```

---

## Зведена таблиця

| № | Тема | Мова | Головний інструмент | Результат |
|---|---|---|---|---|
| 1 | Робота з Git | — | Git, GitHub | Репозиторій, коміти, гілки |
| 2 | Аудит залежностей | JS + Python | npm audit, Safety | 0 вразливостей у обох проектах |
| 3 | Облік витрат | C++ | Makefile, Docker | Контейнеризований застосунок |
| 4 | Лінтер і форматер | Python | flake8, black | Чистий код за PEP 8 |
| 5 | Тестування | Python | unittest, doctest | 6 тестів — OK |
