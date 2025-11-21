def float_format_task():
    def float_format(number: float) -> str:
        exponent = 0
        while number >= 10:
            number /= 10
            exponent += 1
        while number < 1:
            number *= 10
            exponent -= 1
        return f"x = {number} * 10 ** {exponent}"

    while True:
        try:
            number = float(input("Введите положительное число для формата плавающей точки: "))
            if number <= 0:
                print("Ошибка: число должно быть больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка: введено не число.")

    print("Формат плавающей точки:", float_format(number))

    
float_format_task()