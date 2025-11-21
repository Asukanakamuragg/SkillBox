songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

max_songs = len(songs)

n = int(input("Сколько песен выбрать?: "))
if n > max_songs:
    print(f"Ошибка: в списке всего {max_songs} песен")
else:
    total_time = 0
    i = 1
    while i <= n:
        name = input(f"Название {i}-й песни: ").strip()
        found = False
        for song in songs:
            if song[0].lower() == name.lower():
                total_time += song[1]
                found = True
                break
        if not found:
            print(f"Песня '{name}' не найдена в списке, попробуйте ещё раз.")
        else:
            i += 1

    print(f"Общее время звучания песен — {round(total_time, 2)} минуты")
