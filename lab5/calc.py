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
