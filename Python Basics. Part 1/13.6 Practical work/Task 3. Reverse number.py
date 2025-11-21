def reverse_number_task():
    def reverse_number(number: int) -> int:
        return int(str(number)[::-1])

    def input_int_number(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введено не число.")

    first_number = input_int_number("Введите первое число: ")
    second_number = input_int_number("Введите второе число: ")

    print("Первое число наоборот:", reverse_number(first_number))
    print("Второе число наоборот:", reverse_number(second_number))

reverse_number_task()