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

    print("\n--- Спроба бронювання ---")
    bookSeat("Dune: Part Two", 3)
    bookSeat("Avatar 3", 2)
