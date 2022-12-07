import string

def obtain_priorities():
    priorities = dict()

    for priority, item_type in enumerate(string.ascii_letters):
        priorities[f"{item_type}"] = priority + 1

    return priorities


def divide_str(init_str: str) -> tuple[str, str]:
    length = len(init_str)
    str_a, str_b = [init_str[:length//2], init_str[length//2:]]
    return str_a, str_b


def find_common_item(elf_group: list[str, str, str],
                     priorities: dict[str, int]) -> int:
    for item in elf_group[0]:
        if item in elf_group[1] and item in elf_group[2]:
            common_item = item
            break
    return priorities[common_item]



def parse(file: str, priorities: dict[str, int]) -> int:
    with open(f"{file}", "r") as data:
        sum_pro = 0
        thirds = 0
        elf_group = []
        for items in data:
            thirds += 1
            elf_group.append(items)
            if thirds == 3:
                sum_pro += find_common_item(elf_group, priorities)
                thirds = 0
                elf_group = []

    return sum_pro


if __name__ == "__main__":
    file = "input.txt"
    priorities = obtain_priorities()
    out = parse(file, priorities)
    print(out)
