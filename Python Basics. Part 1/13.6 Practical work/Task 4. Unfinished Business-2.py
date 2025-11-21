def swap_numbers_task():
    def count_digits(number: int) -> int:
        return len(str(number))

    def swap_first_last_digits(number: int) -> int:
        digits = str(number)
        if len(digits) == 1:
            return number
        return int(digits[-1] + digits[1:-1] + digits[0])

    def input_int_number(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введено не число.")

    first_number = input_int_number("Введите первое число (не менее 3 цифр): ")
    if count_digits(first_number) < 3:
        print("В первом числе меньше трёх цифр.")
        return
    first_number = swap_first_last_digits(first_number)
    print("Изменённое первое число:", first_number)

    second_number = input_int_number("Введите второе число (не менее 4 цифр): ")
    if count_digits(second_number) < 4:
        print("Во втором числе меньше четырёх цифр.")
        return
    second_number = swap_first_last_digits(second_number)
    print("Изменённое второе число:", second_number)

    print("Сумма чисел:", first_number + second_number)

