def sizes(prompt_count: str, prompt_size: str) -> list[int]:
    count = int(input(prompt_count))
    sizes = []
    for i in range(1, count + 1):
        size = int(input(f"{prompt_size} {i}: "))
        sizes.append(size)
    return sizes

def max_people(rolelrs: list[int], feet_sizes: list[int]) -> int:
    rolelrs.sort()
    feet_sizes.sort()
    roller_index = foot_index = 0
    count = 0
    while roller_index < len(rolelrs) and foot_index < len(feet_sizes):
        if rolelrs[roller_index] == feet_sizes[foot_index]:
            count += 1
            roller_index += 1
            foot_index += 1
        elif rolelrs[roller_index] < feet_sizes[foot_index]:
            roller_index += 1
        else:
            foot_index += 1
    return count

rolelrs = sizes("Количество роликов: ", "Размер пары")
feet_sizes = sizes("Количество людей: ", "Размер ноги человека")

print(f"Наибольшее количество людей, которые могут взять ролики: {max_people(rolelrs, feet_sizes)}")
