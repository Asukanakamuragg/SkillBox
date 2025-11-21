def maximum_task():
    def maximum_of_two(first_number: int, second_number: int) -> int:
        return first_number if first_number > second_number else second_number

    def maximum_of_three(first_number: int, second_number: int, third_number: int) -> int:
        return maximum_of_two(maximum_of_two(first_number, second_number), third_number)

    def input_int_number(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введено не число.")

    first_number = input_int_number("Введите первое число: ")
    second_number = input_int_number("Введите второе число: ")
    third_number = input_int_number("Введите третье число: ")

    print("Самое большое число:", maximum_of_three(first_number, second_number, third_number))

maximum_task()