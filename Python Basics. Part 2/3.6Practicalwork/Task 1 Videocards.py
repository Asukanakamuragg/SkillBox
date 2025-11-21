COUNT_VIDEOCARDS = int(input('Введите количество видеокарт: '))
videocards = []

for i in range(COUNT_VIDEOCARDS):
    card = input(f'Видеокарта {i+1}: ')
    videocards.append(card)

def remove_max_values(numbers: list[int]) -> None:
    max_value = max(numbers)
    for _ in range(numbers.count(max_value)):
        numbers.remove(max_value)

remove_max_values(videocards)
print("Список после удаления максимальных видеокарт:", videocards)
