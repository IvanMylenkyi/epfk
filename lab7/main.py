def analyze_room_usage(lessons: list[dict]) -> dict:
    a = 0
    """
    Аналізує використання аудиторій, підраховуючи кількість занять у кожній.

    :param lessons: Список занять (словників з ключами 'room', 'date', 'time').
    :return: Словник, де ключ - номер аудиторії, значення - кількість занять.

    Приклади (doctests):
    >>> analyze_room_usage([])
    {}
    >>> lessons = [
    ...     {"room": "101", "date": "2023-10-01", "time": "08:30"},
    ...     {"room": "102", "date": "2023-10-01", "time": "10:00"},
    ...     {"room": "101", "date": "2023-10-02", "time": "08:30"}
    ... ]
    >>> analyze_room_usage(lessons)
    {'101': 2, '102': 1}
    """
    usage = {}
    for lesson in lessons:
        # Використовуємо .get(), щоб уникнути помилок, якщо ключ 'room' відсутній
        room = lesson.get("room")
        if room:
            usage[room] = usage.get(room, 0) + 1
    return usage


if __name__ == "__main__":
    # Запуск doctests при прямому виконанні файлу
    import doctest

    doctest.testmod(verbose=True)
