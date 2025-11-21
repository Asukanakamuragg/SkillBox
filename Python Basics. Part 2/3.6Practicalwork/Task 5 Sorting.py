numbers = []

repetitions = int(input('Введите количество элементов: '))
for _ in range(repetitions):
    number = int(input('Введите целое число: '))
    numbers.append(number)
numbers.sort()
print(f'Отсортированный список - {numbers}')