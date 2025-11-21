def counting_game(total_people: int, step: int) -> int:
    people = list(range(1, total_people + 1))
    current_index = 0

    while len(people) > 1:
        current_index = (current_index + step - 1) % len(people)
        print(f"Выбывает человек под номером {people[current_index]}")
        people.pop(current_index)
        print(f"Текущий круг людей: {people}")
        print()

    return people[0]

n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))

print(f"Остался человек под номером {counting_game(n, k)}")
