shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300],
    ['педаль', 100], ['седло', 1500], ['рама', 12000],
    ['обод', 2000], ['шатун', 200], ['седло', 2700]
]

def count_and_sum(shop_list: list[list], detail: str) -> tuple[int, int]:
    count = 0
    total = 0
    for name, price in shop_list:
        if name == detail:
            count += 1
            total += price
    return count, total

detail = input("Название детали: ")
count, total = count_and_sum(shop, detail)

print(f"Количество деталей: {count}")
print(f"Общая стоимость: {total}")
