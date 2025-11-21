ACCEPTABLE_FILMS = [
    "крепкий орешек", "назад в будущее", "таксист", "леон",
    "богемская рапсодия", "город грехов", "мементо",
    "отступники", "деревня"
]

films = []

repetitions = int(input('Введите количество добавления фильмов: '))

for _ in range(repetitions):
    film = input('Введите название фильма: ').strip().lower()

    if film not in ACCEPTABLE_FILMS:
        print('ERROR: Данного фильма нет')

    if film in films:
        print("Ошибка: фильм уже добавлен")

    films.append(film)

print(f"Ваш список фильмов:", *films)
