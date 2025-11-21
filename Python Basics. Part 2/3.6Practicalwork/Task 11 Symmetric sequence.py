def numbers_to_make_symmetric(sequence: list[int]) -> list[int]:
    for i in range(len(sequence)):
        if sequence[i:] == sequence[i:][::-1]:
            return sequence[:i][::-1]
    return sequence[:-1][::-1]

length = int(input("Количество чисел: "))
sequence = [int(input("Число: ")) for _ in range(length)]

to_add = numbers_to_make_symmetric(sequence)

print(f"Последовательность: {sequence}")
print(f"Нужно приписать чисел: {len(to_add)}")
print(f"Сами числа: {to_add}")
