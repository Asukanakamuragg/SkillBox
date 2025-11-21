def input_list(prompt):
    n = int(input(f"Введите количество элементов для {prompt}: "))
    lst = []
    for _ in range(n):
        lst.append(int(input("Введите число: ")))
    return lst

def merge_and_deduplicate(list_a, list_b):
    merged = list_a + list_b
    merged.sort()
    deduplicated = []
    for item in merged:
        if not deduplicated or deduplicated[-1] != item:
            deduplicated.append(item)
    return deduplicated

first_list = input_list("первого списка")
second_list = input_list("второго списка")

result = merge_and_deduplicate(first_list, second_list)
print(result)
