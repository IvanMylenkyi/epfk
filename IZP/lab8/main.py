import sentry_sdk
import os

# 1. Налаштування Sentry
# В реальному проекті DSN краще тримати в змінних оточення
SENTRY_DSN = os.getenv(
    "SENTRY_DSN",
    "https://fc93a619aead7c7bb4c28245b1bbe761@o4511281230577664.ingest.de.sentry.io/4511281243816016",
)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Встановлюємо відсоток трасування (1.0 = 100%)
    traces_sample_rate=1.0,
)


def check_key(user_input):
    """
    Перевіряє, чи є вхідні дані непорожнім рядком.
    """
    # Перевірка на тип та порожнечу
    if not isinstance(user_input, str) or len(user_input.strip()) == 0:
        raise ValueError("Помилка: Вхідні дані мають бути непорожнім рядком!")

    return len(user_input)


if __name__ == "__main__":
    print("--- Програма перевірки ключа ---")
    data = input("Введіть ключ: ")

    try:
        result = check_key(data)
        print(f"Успіх! Довжина введеного ключа: {result}")
    except ValueError as e:
        print(f"Сталася помилка: {e}")
        # Помилка автоматично відправиться в Sentry, якщо DSN вірний.
        # Можна також відправити її явно:
        sentry_sdk.capture_exception(e)
