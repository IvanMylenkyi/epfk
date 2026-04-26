

## Як запустити проєкт

1. Переконайтеся, що у вас встановлено Python 3.10+.
2. Склонуйте репозиторій:
   ```bash
   git clone https://github.com/IvanMylenkyi/epfk.git
   cd lab7
3. (Опціонально) Створіть віртуальне середовище:


python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
4. Встановіть необхідні залежності (для форматування):


pip install black
5. Як запустити тести
Unit-tests:


python -m unittest test_app.py
Doctests:


python -m doctest -v app.py
6. Налаштування Git Hook (Pre-commit)
У проєкті передбачено Git Hook, який перевіряє форматування коду за допомогою black перед кожним комітом. Щоб його активувати, виконайте наступні кроки:

Скопіюйте файл pre-commit у приховану папку Git:


cp pre-commit .git/hooks/pre-commit
Зробіть файл виконуваним (для Linux/Mac):


chmod +x .git/hooks/pre-commit
Тепер при спробі зробити git commit код буде автоматично перевірено.

