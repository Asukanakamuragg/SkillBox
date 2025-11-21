def input_numbers(repetitions: int) -> list[int]:
    numbers = []
    for i in range(repetitions):
        while True:
            try:
                number = int(input(f'Введите число {i + 1}: '))
                numbers.append(number)
                break
            except ValueError:
                print("Ошибка: введите число.")
    return numbers

def shift_numbers(numbers: list[int], shift: int) -> None:
    if not numbers:
        return
    shift %= len(numbers)
    numbers[:] = numbers[-shift:] + numbers[:-shift]

numbers = []
shift = int(input('Введите сдвиг: '))
repetitions = int(input('Введите количество элементов: '))

numbers = input_numbers(repetitions)
shift_numbers(numbers, shift)

print(numbers)
