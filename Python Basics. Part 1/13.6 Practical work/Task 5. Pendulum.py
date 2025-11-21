def pendulum_task():
    def calculate_swings(start_amplitude: float, stop_amplitude: float) -> int:
        count = 0
        amplitude = start_amplitude
        while amplitude > stop_amplitude:
            amplitude *= 0.916  # уменьшение на 8.4%
            count += 1
        return count

    def input_float_number(prompt: str) -> float:
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Ошибка: число должно быть больше нуля.")
                    continue
                return value
            except ValueError:
                print("Ошибка: введено не число.")

    start_amplitude = input_float_number("Введите начальную амплитуду маятника (см): ")
    stop_amplitude = input_float_number("Введите конечную амплитуду маятника (см): ")
    if stop_amplitude >= start_amplitude:
        print("Ошибка: конечная амплитуда должна быть меньше начальной.")
        return

    swings_count = calculate_swings(start_amplitude, stop_amplitude)
    print("Маятник качнётся раз:", swings_count)

pendulum_task()